from pathlib import Path

# settings
BOT_NAME = 'pep_parse'
SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'
ROBOTSTXT_OBEY = True

# dir
BASE_DIR = Path(__file__).parent.parent
RESULTS_FOLDER = 'results'

# format
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

# feeds
FEEDS = {
    f'{RESULTS_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

# pipelines
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}
