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


class ServerBase:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.shutdownRequested = False

    def start(self):
        raise NotImplementedError

    def stop(self):
        raise NotImplementedError

    def restart(self):
        raise NotImplementedError

    def status(self):
        raise NotImplementedError

    def log(self):
        raise NotImplementedError

    def config(self):
        raise NotImplementedError

    def version(self):
        raise NotImplementedError

    def help(self):
        raise NotImplementedError
