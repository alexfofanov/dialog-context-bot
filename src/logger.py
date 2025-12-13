import logging

from src.config import LOG_DIR


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler(LOG_DIR / 'bot.log', encoding='utf-8'),
            logging.StreamHandler(),
        ],
    )
    return logging.getLogger('bot')
