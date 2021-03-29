import logging


def test_logging():

    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # file handler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("information statement")
    logger.warning("Warning statements are here")
    logger.error("Error statements")
    logger.critical("The critical statements are here")

