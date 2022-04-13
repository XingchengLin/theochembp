"""A sample repo for the TheoChem best practices workshop."""

# Add imports here
from .theochembp import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
