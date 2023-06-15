import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Environment
TESTING_ENVIRONMENT = 'testing'
DEVELOPMENT_ENVIRONMENT = 'development'
STAGING_ENVIRONMENT = 'staging'
PRODUCTION_ENVIRONMENT = 'production'

# API Tags
TAG_COMMON = 'Common'
TAG_PROBES = 'Probes'
TAG_METRIC = 'Metric'

# Other
P99_DEFAULT_VALUE = 99


def get_default_environment():
    if 'test' in sys.argv:
        return TESTING_ENVIRONMENT
    return DEVELOPMENT_ENVIRONMENT
