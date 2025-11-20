import logging 
import sys


LOG_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_LEVEL = logging.DEBUG
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter(LOG_FORMAT))
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
if not root_logger.hasHandlers():
    root_logger.addHandler(handler)

def get_logger(name: str = None) -> logging.Logger:
    """Get a logger with the given name, or the root logger if no name is provided."""
    return logging.getLogger(name)