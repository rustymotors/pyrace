import logging
from tkinter import N


def getDefaultLevel():
    return logging.INFO


__logger = None


def getLogger(name: str | None, level: int = getDefaultLevel()) -> logging.Logger:
    global __logger
    if __logger is None:
        __logger = logging.getLogger('pyrace')
        __logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )

        __logger.addHandler(handler)
        
        if name != None:
            return __logger.getChild(name)

    return __logger
