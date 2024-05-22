import logging
from tkinter import N


def getDefaultLevel():
    return logging.INFO

class __Logger:
    def __init__(self, name: str | None, level: int) -> None:
        self.name = name
        self.level = level
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        )

        self.logger.addHandler(handler)
        
    def getLogger(self, name: str):
        level = self.level
        name = f"{self.name}.{name}"
        return self.__class__(name, level)

    def debug(self, message: str, *args):
        self.logger.debug(message, *args)
        
    def info(self, message: str, *args):
        self.logger.info(message, *args)
        
    def warning(self, message: str, *args):
        self.logger.warning(message, *args)
        
    def error(self, message: str, *args):
        self.logger.error(message, *args)
        
    def critical(self, message: str, *args):
        self.logger.critical(message, *args)
        
    def exception(self, message: str, *args):
        self.logger.exception(message, *args)
        
    def log(self, level: int, message: str, *args):
        self.logger.log(level, message, *args)

__logger = None


def getLogger(name: str | None, level: int = getDefaultLevel()) -> __Logger:
    global __logger
    if __logger is None:
        __logger = __Logger('pyrace', level)
        
        if name != None:
            return __logger.getLogger(name)

    return __logger
