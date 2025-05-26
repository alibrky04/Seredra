import logging
import sys

# Configure root logger at module load
logging.basicConfig(
    level=logging.INFO,  # Default log level can be adjusted
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # Log to stdout (console)
    ]
)

def log_info(message: str) -> None:
    """Log an info level message."""
    logging.info(message)

def log_error(message: str) -> None:
    """Log an error level message."""
    logging.error(message)

def log_debug(message: str) -> None:
    """Log a debug level message."""
    logging.debug(message)