"""
Stratum — Multi-Audience Documentation Framework
Material design optimized for clean, professional aesthetics.
"""

__version__ = "0.3.0"
__author__ = "Stratum Contributors"
__license__ = "MIT"

from .audience_plugin import StratumAudiencePlugin
from .config_generator import generate_audience_configs

__all__ = [
    "StratumAudiencePlugin",
    "generate_audience_configs",
    "get_plugin",
    "__version__",
]

def get_plugin() -> StratumAudiencePlugin:
    return StratumAudiencePlugin()