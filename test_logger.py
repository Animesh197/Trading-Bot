from bot.logging_config import setup_logger

logger = setup_logger()

logger.info("Application started successfully.")
logger.info("Testing logging system.")
logger.error("This is a sample error log.")

print("\nLogs written successfully!")
print("Check logs/trading_bot.log")