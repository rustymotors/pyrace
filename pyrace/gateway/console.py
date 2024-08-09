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

from curtsies.input import Input
from threading import Thread
from pyrace.base import ServerBase
from pyrace.shared.logging import getLogger


class ConsoleThread(Thread, ServerBase):

    def __init__(self, parentThread: ServerBase, logger=getLogger("console")) -> None:
        Thread.__init__(self)
        self.parentThread = parentThread
        self.logger = logger
        self.shutdownRequested = False

        pass

    def run(self) -> None:

        if self.shutdownRequested:
            return

        reactor = Input()

        self.logger.info("Started console thread")

        with reactor:
            for e in reactor:
                if e == "p":
                    print(self.parentThread)
                    continue
                if e == "?":
                    print("Help:")
                    continue
                if e == "x":
                    self.parentThread.shutdownRequested = True
                    return
                print(repr(e))

    def stop(self) -> None:
        self.logger.info("Stopping console thread")
        self.shutdownRequested = True
        self.logger.info("Stopped console thread")
