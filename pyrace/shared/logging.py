# RustyMotors is a project to build an online server for a legacy racing game
# Copyright (C) 2024 Molly Draven
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
        self.logger.propagate = False
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
