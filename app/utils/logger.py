
from loguru import logger
from pathlib import Path

import sys


LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()
logger.add(sys.stdout, level="DEBUG", format="<green>{time}</green> | <level>{level}</level> | {message}")
logger.add(LOGS_DIR / "app.log", rotation="1 MB", retention="1 days", level="INFO", format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}")

