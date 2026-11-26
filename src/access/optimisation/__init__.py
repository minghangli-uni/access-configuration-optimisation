"""
access-configuration-optimisation package.

Closed-loop, model-based optimisation of how an ACCESS model is run. Starting from a
configuration as production runs it, the loop measures, models, proposes and verifies
changes to the cores, layouts, decompositions and I/O, and returns two answers judged on
a simulated year against production:

1. the cheapest configuration that is not slower, and
2. the fastest one whose year costs at most a set allowance more.
"""

from contextlib import suppress
from importlib.metadata import PackageNotFoundError, version

__version__ = "unknown"
with suppress(PackageNotFoundError):
    __version__ = version("access-configuration-optimisation")

__all__ = ["__version__"]
