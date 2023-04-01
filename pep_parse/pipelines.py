import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER


class PepParsePipeline:

    def open_spider(self, spider):
        self.count_statuses = defaultdict(int)
        self.results_dir = BASE_DIR / RESULTS_FOLDER
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.count_statuses[item.get('status')] += 1
        return item

    def close_spider(self, spider):
        now_formatted = dt.now().strftime(DATETIME_FORMAT)
        filename = f'status_summary_{now_formatted}.csv'
        file_dir = self.results_dir / filename
        with open(file_dir, mode='w', encoding='utf-8') as f:
            csv.writer(
                f, dialect=csv.unix_dialect
            ).writerows([
                ('Статус', 'Количество'),
                *self.count_statuses.items(),
                ('Total', sum(self.count_statuses.values()))
            ])
