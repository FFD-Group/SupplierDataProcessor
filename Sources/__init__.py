import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="logs/Sources.log", level=logging.DEBUG)
logger.info("Sources package initialised.")
