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


def get_default_environment():
    if 'test' in sys.argv:
        return TESTING_ENVIRONMENT
    return DEVELOPMENT_ENVIRONMENT
