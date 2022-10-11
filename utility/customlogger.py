import logging
import sys


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(".\\Logs\\automation.log")
        # ch = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s',
                                      datefmt="%a, %d %b %Y %H:%M:%S")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        # logger.addHandler(ch)
        return logger
