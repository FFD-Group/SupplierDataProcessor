import logging

logger = logging.getLogger(__name__)
logging.getLogger("faker").setLevel(logging.ERROR)
logging.basicConfig(
    filename="logs/Sources.log",
    format="%(asctime)s %(message)s",
    level=logging.DEBUG,
)
