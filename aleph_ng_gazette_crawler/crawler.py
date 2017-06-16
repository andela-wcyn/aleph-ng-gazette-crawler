from aleph.crawlers import DocumentCrawler
import os
import requests
import urlparse
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Crawler(DocumentCrawler):
    COLLECTION_ID = 'NG_gazettes'
    COLLECTION_LABEL = 'Nigerian Government Gazettes'
    SCHEDULE = DocumentCrawler.DAILY
    ARCHIVE_URI = os.environ.get('NG_GAZETTE_ARCHIVE_URI')

    def crawl(self):
        index_url = urlparse.urljoin(
            self.ARCHIVE_URI, 'gazettes_index.jsonlines')
        logger.info("Fetching %s" % index_url)
        r = requests.get(index_url)
        r.raise_for_status()
        for idx, line in enumerate(r.text.splitlines()):
            gazette = json.loads(line)

            if self.skip_incremental(gazette.get('filename')):
                continue

            meta = self.make_meta({
                'foreign_id': gazette.get('filename'),
                'title': gazette.get('gazette_title'),
                'extension': 'pdf',
                'mime_type': 'application/pdf',
                'file_name': os.path.basename(gazette.get('files')[0]['path']),
                'source_url': gazette.get('gazette_link'),
                'publication_date': gazette.get('publication_date'),
            })
            logger.info("Emitting %s" % gazette.get('filename'))
            self.emit_url(meta, urlparse.urljoin(self.ARCHIVE_URI,
                          gazette.get('files')[0]['path']))
