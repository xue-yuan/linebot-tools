import logging


def create_logger(name, level):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    return logger


def create_handler(handler, level, format="%(message)s", filters=[]):
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(format))

    for f in filters:
        handler.addFilter(f)

    return handler


handler = create_handler(
    handler=logging.StreamHandler(),
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)1s %(module)s %(message)s",
)

logger = create_logger("app", logging.INFO)
logger.addHandler(handler)
