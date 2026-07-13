"""
Logging Utilities
=================

Provides a configured logger for the project.
"""

import logging


def get_logger(name):
    """
    Return a configured logger.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger(name)