import logging
import os


def setup_logger():
    """
    Configure and return application logger.
    """

    # Create logs directory if not exists
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("trading_bot")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Log file path
    log_file = "logs/trading_bot.log"

    # File handler
    file_handler = logging.FileHandler(log_file)

    # Log format
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)

    # Attach handler to logger
    logger.addHandler(file_handler)

    return logger