#!/usr/bin/env python3
"""
knowledge_updater.py — Self-improving knowledge pipeline for pet-health-care-assessment

Crawls authoritative veterinary sources using crawl4ai, scores entries by recency
and domain relevance, and appends new, de-duplicated entries to SECOND-KNOWLEDGE-BRAIN.md.

Schedule: Weekly (cron). Cluster: lifestyle-personal. Idea #82.

Dependencies:
    pip install crawl4ai requests beautifulsoup4 arxiv

Usage:
    python knowledge_updater.py [--force] [--dry-run]

    --force: Run even if last run was <7 days ago
    --dry-run: Show what would be added without writing
"""

import os
import re
import json
import hashlib
import argparse
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Set, Optional
from dataclasses import dataclass, asdict
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('knowledge_updater.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
BRAIN_FILE = Path(__file__).parent.parent / "SECOND-KNOWLEDGE-BRAIN.md"
STATE_FILE = Path(__file__).parent / "knowledge_state.json"

# Minimum days between runs
MIN_RUN_INTERVAL_DAYS = 7

# ArXiv categories for veterinary/biological research
ARXIV_CATEGORIES = [
    'q-bio.QM',  # Quantitative Methods
    'q-bio.TO',  # Tissues and Organs
    'q-bio.CB',  # Cell Behavior
]

# Search queries for companion animal research
SEARCH_QUERIES = [
    'companion animal preventive care guidelines',
    'pet nutrition body condition scoring',
    'veterinary vaccination schedule AAHA WSAVA',
    'canine life stage care guidelines',
    'feline life stage care guidelines',
    'pet welfare Five Domains model',
    'companion animal behavior enrichment',
    'veterinary nutrition assessment',
]

# Authoritative domain sources
DOMAIN_SOURCES = {
    'aaha': {
        'name': 'American Animal Hospital Association',
        'base_url': 'https://www.aaha.org',
        'search_paths': ['/guidelines/', '/pet-care/'],
        'weight': 1.0  # Highest authority
    },
    'wsava': {
        'name': 'World Small Animal Veterinary Association',
        'base_url': 'https://www.wsava.org',
        'search_paths': ['/guidelines/', '/educational-resources/'],
        'weight': 1.0
    },
    'avma': {
        'name': 'American Veterinary Medical Association',
        'base_url': 'https://www.avma.org',
        'search_paths': ['/resources/pet-owners/', '/news/'],
        'weight': 0.95
    },
    'aspca': {
        'name': 'ASPCA',
        'base_url': 'https://www.aspca.org',
        'search_paths': ['/pet-care/'],
        'weight': 0.9
    },
    'merckvet': {
        'name': 'Merck Veterinary Manual',
        'base_url': 'https://www.merckvetmanual.com',
        'search_paths': ['/'],
        'weight': 0.95
    },
    'rcvs': {
        'name': 'Royal College of Veterinary Surgeons',
        'base_url': 'https://www.rcvs.org.uk',
        'search_paths': ['/advice-and-communications/'],
        'weight': 0.9
    },
    'fda': {
        'name': 'FDA - Center for Veterinary Medicine',
        'base_url': 'https://www.fda.gov',
        'search_paths': ['/animal-veterinary/'],
        'weight': 0.9
    },
}

# Domain keywords for relevance scoring
DOMAIN_KEYWORDS = [
    'companion animal', 'pet health', 'veterinary', 'canine', 'feline',
    'dog', 'cat', 'rabbit', 'preventive care', 'nutrition', 'vaccination',
    'life stage', 'welfare', 'behavior', 'enrichment', 'body condition',
    'guidelines', 'assessment', 'scoring', 'screening', 'red flag'
]

@dataclass
class KnowledgeEntry:
    """Structured knowledge entry with metadata."""
    title: str
    authors: str
    year: str
    venue: str  # Source/publisher
    url: str
    abstract: str = ""
    key_finding: str = ""
    relevance_score: float = 0.0
    recency_score: float = 0.0
    overall_score: float = 0.0
    evidence_tier: str = ""  # Tier 1-6
    entry_hash: str = ""
    crawled_at: str = ""

    def to_markdown_row(self) -> str:
        """Format as markdown table row."""
        title_short = self.title[:70] + "..." if len(self.title) > 70 else self.title
        authors_short = self.authors[:40] + "..." if len(self.authors) > 40 else self.authors
        return (
            f"| {title_short} | {authors_short} | {self.year} "
            f"| {self.venue[:30]} | {self.url[:60]} | "
            f"auto-scored {self.overall_score:.1f} | <!--h:{self.entry_hash}-->"
        )

class StateManager:
    """Manage run state to prevent excessive crawling."""

    def __init__(self, state_file: Path):
        self.state_file = state_file
        self.state = self._load_state()

    def _load_state(self) -> Dict[str, Any]:
        """Load state from file."""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                logger.warning(f"Corrupted state file, starting fresh")
        return {
            'last_run': None,
            'last_entries_count': 0,
            'total_entries_added': 0,
            'run_history': []
        }

    def save_state(self):
        """Save state to file."""
        with open(self.state_file, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, indent=2, default=str)

    def should_run(self, force: bool = False) -> bool:
        """Check if enough time has passed since last run."""
        if force:
            return True

        if not self.state['last_run']:
            return True

        last_run = datetime.fromisoformat(self.state['last_run'])
        days_since = (datetime.now() - last_run).days
        return days_since >= MIN_RUN_INTERVAL_DAYS

    def update_run(self, entries_added: int):
        """Update state after a run."""
        self.state['last_run'] = datetime.now().isoformat()
        self.state['last_entries_count'] = entries_added
        self.state['total_entries_added'] += entries_added
        self.state['run_history'].append({
            'timestamp': datetime.now().isoformat(),
            'entries_added': entries_added
        })
        self.save_state()

class ArXivFetcher:
    """Fetch recent papers from ArXiv."""

    def __init__(self, categories: List[str], max_results: int = 25):
        self.categories = categories
        self.max_results = max_results
        self.base_url = "http://export.arxiv.org/api/query"

    def fetch(self) -> List[Dict[str, Any]]:
        """Fetch papers from specified categories."""
        entries = []
        import urllib.request
        import urllib.parse

        for category in self.categories:
            params = urllib.parse.urlencode({
                "search_query": f"cat:{category}",
                "sortBy": "submittedDate",
                "sortOrder": "descending",
                "max_results": self.max_results,
            })
            url = f"{self.base_url}?{params}"

            try:
                logger.info(f"Fetching ArXiv category: {category}")
                with urllib.request.urlopen(url, timeout=30) as response:
                    raw = response.read().decode("utf-8", "ignore")

                # Parse XML response
                for match in re.finditer(r"<entry>(.*?)</entry>", raw, re.DOTALL):
                    entry_block = match.group(1)
                    entry = self._parse_entry(entry_block, category)
                    if entry and entry.get('title'):
                        entries.append(entry)
                        logger.debug(f"Parsed: {entry['title'][:50]}...")

            except Exception as e:
                logger.error(f"Failed to fetch {category}: {e}")

        logger.info(f"ArXiv fetch complete: {len(entries)} entries")
        return entries

    def _parse_entry(self, block: str, category: str) -> Optional[Dict[str, Any]]:
        """Parse a single ArXiv entry."""
        def extract_tag(tag_name: str) -> str:
            pattern = rf"<{tag_name}[^>]*>(.*?)</{tag_name}>"
            match = re.search(pattern, block, re.DOTALL)
            if match:
                return re.sub(r"\s+", " ", match.group(1)).strip()
            return ""

        def extract_all_tags(tag_name: str) -> List[str]:
            pattern = rf"<{tag_name}[^>]*>(.*?)</{tag_name}>"
            matches = re.findall(pattern, block, re.DOTALL)
            return [re.sub(r"\s+", " ", m).strip() for m in matches]

        title = extract_tag("title")
        if not title:
            return None

        authors = ", ".join(extract_all_tags("name"))
        published = extract_tag("published")
        year = published[:4] if published else ""
        url = extract_tag("id")
        abstract = extract_tag("summary")

        return {
            'title': title,
            'authors': authors,
            'year': year,
            'venue': f'arXiv:{category}',
            'url': url,
            'abstract': abstract,
        }

class WebCrawler:
    """Crawl authoritative veterinary websites using crawl4ai."""

    def __init__(self, domain_sources: Dict[str, Dict]):
        self.domain_sources = domain_sources

    def crawl(self) -> List[Dict[str, Any]]:
        """Crawl configured domain sources."""
        entries = []

        try:
            from crawl4ai import AsyncWebCrawler
            import asyncio

            async def crawl_all():
                all_entries = []
                async with AsyncWebCrawler(verbose=True) as crawler:
                    for domain_id, config in self.domain_sources.items():
                        logger.info(f"Crawling {config['name']}...")
                        try:
                            domain_entries = await self._crawl_domain(
                                crawler, domain_id, config
                            )
                            all_entries.extend(domain_entries)
                            logger.info(f"  Got {len(domain_entries)} entries")
                        except Exception as e:
                            logger.error(f"  Failed to crawl {domain_id}: {e}")
                return all_entries

            entries = asyncio.run(crawl_all())

        except ImportError:
            logger.warning("crawl4ai not installed, using fallback mode")
            entries = self._fallback_crawl()

        logger.info(f"Web crawl complete: {len(entries)} entries")
        return entries

    async def _crawl_domain(self, crawler, domain_id: str, config: Dict) -> List[Dict]:
        """Crawl a single domain."""
        entries = []
        base_url = config['base_url']

        for path in config['search_paths']:
            url = base_url + path
            try:
                result = await crawler.arun(url=url)
                if result.success:
                    # Extract relevant links/content from the page
                    # This is simplified - real implementation would parse HTML
                    # and extract article/guide links
                    entry = {
                        'title': f"{config['name']} - {path.strip('/')}",
                        'authors': config['name'],
                        'year': str(datetime.now().year),
                        'venue': config['name'],
                        'url': url,
                        'abstract': result.markdown[:500] if result.markdown else "",
                    }
                    entries.append(entry)
            except Exception as e:
                logger.warning(f"    Failed to crawl {url}: {e}")

        return entries

    def _fallback_crawl(self) -> List[Dict[str, Any]]:
        """Fallback when crawl4ai is not available."""
        # Return placeholder entries that would be filled by manual/WebSearch
        logger.info("Using placeholder entries - requires manual WebSearch integration")
        return []

class EntryScorer:
    """Score knowledge entries by relevance and recency."""

    def __init__(self, keywords: List[str]):
        self.keywords = [k.lower() for k in keywords]

    def score_entry(self, entry: Dict[str, Any]) -> KnowledgeEntry:
        """Score a single entry."""
        knowledge_entry = KnowledgeEntry(
            title=entry.get('title', ''),
            authors=entry.get('authors', ''),
            year=entry.get('year', ''),
            venue=entry.get('venue', ''),
            url=entry.get('url', ''),
            abstract=entry.get('abstract', ''),
            key_finding=entry.get('key_finding', ''),
            entry_hash=self._compute_hash(entry.get('url', '') or entry.get('title', '')),
            crawled_at=datetime.now().isoformat()
        )

        # Calculate scores
        knowledge_entry.recency_score = self._score_recency(knowledge_entry.year)
        knowledge_entry.relevance_score = self._score_relevance(knowledge_entry)
        knowledge_entry.overall_score = (
            knowledge_entry.recency_score * 0.4 +
            knowledge_entry.relevance_score * 0.6
        )
        knowledge_entry.evidence_tier = self._determine_evidence_tier(knowledge_entry)

        return knowledge_entry

    def _score_recency(self, year: str) -> float:
        """Score by recency (more recent = higher score)."""
        try:
            year_int = int(year)
            years_old = datetime.now().year - year_int
            if years_old < 0:
                return 0.0  # Future date
            # Max score 5.0 for papers <1 year old, decays over time
            return max(0, 5.0 - (years_old * 0.5))
        except (ValueError, TypeError):
            return 0.0

    def _score_relevance(self, entry: KnowledgeEntry) -> float:
        """Score by keyword relevance."""
        text = (
            entry.title.lower() + " " +
            entry.abstract.lower() + " " +
            entry.key_finding.lower()
        )

        score = 0.0
        for keyword in self.keywords:
            if keyword in text:
                score += 1.0

        # Bonus for multiple matches
        if score >= 3:
            score *= 1.2

        return min(score, 5.0)

    def _determine_evidence_tier(self, entry: KnowledgeEntry) -> str:
        """Determine evidence tier based on venue."""
        venue_lower = entry.venue.lower()

        # Systematic review/meta-analysis
        if any(term in venue_lower for term in ['systematic review', 'meta-analysis', 'cochrane']):
            return "Tier 1"
        # Randomized controlled trial
        if any(term in venue_lower for term in ['randomized', 'rct', 'controlled trial']):
            return "Tier 2"
        # Cohort study
        if 'cohort' in venue_lower or 'longitudinal' in venue_lower:
            return "Tier 3"
        # Expert consensus/guidelines
        if any(term in venue_lower for term in ['guideline', 'aaha', 'wsava', 'avma', 'consensus']):
            return "Tier 4"
        # Case reports/opinion
        if any(term in venue_lower for term in ['case report', 'opinion', 'editorial']):
            return "Tier 5"
        # Unverified
        return "Tier 6"

    def _compute_hash(self, value: str) -> str:
        """Compute hash for deduplication."""
        return hashlib.sha256(value.encode()).hexdigest()[:12]

class KnowledgeBaseUpdater:
    """Update the SECOND-KNOWLEDGE-BRAIN.md file."""

    def __init__(self, brain_file: Path):
        self.brain_file = brain_file

    def load_existing_hashes(self) -> Set[str]:
        """Load existing entry hashes from brain file."""
        if not self.brain_file.exists():
            logger.warning(f"Brain file not found: {self.brain_file}")
            return set()

        with open(self.brain_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract existing hashes
        hashes = set(re.findall(r'<!--h:([0-9a-f]{12})-->', content))
        logger.info(f"Found {len(hashes)} existing entries")
        return hashes

    def append_entries(self, entries: List[KnowledgeEntry], dry_run: bool = False) -> int:
        """Append new entries to brain file."""
        existing_hashes = self.load_existing_hashes()
        new_entries = [e for e in entries if e.entry_hash not in existing_hashes]

        if not new_entries:
            logger.info("No new entries to add")
            return 0

        if dry_run:
            logger.info(f"[DRY RUN] Would add {len(new_entries)} entries:")
            for entry in new_entries[:5]:
                logger.info(f"  - {entry.title[:50]}...")
            if len(new_entries) > 5:
                logger.info(f"  ... and {len(new_entries) - 5} more")
            return len(new_entries)

        # Sort by overall score
        new_entries.sort(key=lambda e: e.overall_score, reverse=True)

        # Prepare append block
        today = datetime.now().date().isoformat()
        rows = [e.to_markdown_row() for e in new_entries]

        block = (
            f"\n- **{today}** — Auto-crawl added {len(new_entries)} entries. "
            f"Scores range {new_entries[-1].overall_score:.1f}-{new_entries[0].overall_score:.1f}.\n"
            + "\n".join(rows) + "\n"
        )

        # Append to file
        with open(self.brain_file, 'r', encoding='utf-8') as f:
            content = f.read()

        with open(self.brain_file, 'w', encoding='utf-8') as f:
            f.write(content.rstrip() + block)

        logger.info(f"Appended {len(new_entries)} entries to {self.brain_file}")
        return len(new_entries)

def main():
    """Main execution."""
    parser = argparse.ArgumentParser(description='Update pet health knowledge base')
    parser.add_argument('--force', action='store_true', help='Run even if <7 days since last')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without writing')
    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("Pet Health Knowledge Updater Starting")
    logger.info("=" * 60)

    # Check if we should run
    state_manager = StateManager(STATE_FILE)
    if not state_manager.should_run(args.force):
        days_since = (datetime.now() - datetime.fromisoformat(state_manager.state['last_run'])).days
        logger.info(f"Skipping - last run was {days_since} days ago (min {MIN_RUN_INTERVAL_DAYS} days)")
        logger.info("Use --force to override")
        return

    logger.info("Starting knowledge update...")

    # Fetch from ArXiv
    arxiv_fetcher = ArXivFetcher(ARXIV_CATEGORIES, max_results=25)
    arxiv_entries = arxiv_fetcher.fetch()
    logger.info(f"ArXiv: {len(arxiv_entries)} entries")

    # Crawl web sources
    web_crawler = WebCrawler(DOMAIN_SOURCES)
    web_entries = web_crawler.crawl()
    logger.info(f"Web: {len(web_entries)} entries")

    # Combine all entries
    all_entries = arxiv_entries + web_entries
    logger.info(f"Total raw entries: {len(all_entries)}")

    # Score entries
    scorer = EntryScorer(DOMAIN_KEYWORDS)
    scored_entries = [scorer.score_entry(e) for e in all_entries if e.get('title')]
    logger.info(f"Scored entries: {len(scored_entries)}")

    # Filter by minimum score
    MIN_SCORE = 1.0
    filtered_entries = [e for e in scored_entries if e.overall_score >= MIN_SCORE]
    logger.info(f"Filtered entries (score >={MIN_SCORE}): {len(filtered_entries)}")

    # Update knowledge base
    updater = KnowledgeBaseUpdater(BRAIN_FILE)
    added_count = updater.append_entries(filtered_entries, dry_run=args.dry_run)

    # Update state
    if not args.dry_run:
        state_manager.update_run(added_count)
        logger.info(f"Run complete. Total entries in history: {state_manager.state['total_entries_added']}")
    else:
        logger.info(f"[DRY RUN] Would have added {added_count} entries")

    logger.info("=" * 60)
    logger.info("Knowledge Updater Complete")
    logger.info("=" * 60)

if __name__ == "__main__":
    main()
