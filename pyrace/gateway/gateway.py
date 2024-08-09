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

import asyncio
from http.server import BaseHTTPRequestHandler, HTTPServer, ThreadingHTTPServer
from re import T
from threading import Thread
from webbrowser import get

from pyrace.base import ServerBase
from pyrace.gateway.console import ConsoleThread
from pyrace.gateway.parseQuery import parseQuery
from pyrace.gateway.web import WebServer
from pyrace.shared.config import getConfig
from pyrace.shared.logging import getLogger
from sentry_sdk import capture_exception


def __onSocketConnection(socket, logger) -> None:
    pass


class webRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, logger, *args):
        self.logger = logger
        super().__init__(*args)

    def do_GET(self):
        try:
            self.logger.info(
                "== %s request for path: %s", str(self.command), str(self.path)
            )
            self.logger.info("== Query: %s", str(parseQuery(self.path)))
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"Hello, world")
        except Exception as e:
            capture_exception(e)

    def log_message(self, format: str, *args: str) -> None:
        self.logger.info(format, *args)


class GatewayServer(ServerBase):

    def __init__(self, config, logger, portList, onSocketConnection) -> None:
        try:
            super().__init__("localhost", 3000)
            self.shutdownRequested = False
            self.config = config
            self.logger = logger
            self.portList = portList
            self.onSocketConnection = onSocketConnection
            self.webLogger = self.logger.getLogger("web")
            self.loop = asyncio.get_event_loop()

            self.logger.info(
                "Starting gateway with the following configuration: %s", self.config
            )
        except Exception as e:
            capture_exception(e)

    def start(self) -> None:
        """
        Starts the gateway.

        This method initializes and starts the console thread and the HTTP server thread.

        Returns:
            None
        """
        try:
            self.logger.info("Starting gateway")

            self.consoleThread = ConsoleThread(
                parentThread=self,
                logger=self.logger.getLogger("console"),
            )
            self.consoleThread.start()

            self.logger.info("Started console thread")

            self.webLogger.info("Starting web server")
            self.httpServer = HTTPServer(
                ("localhost", 3000),
                lambda *args: webRequestHandler(self.webLogger, *args),
            )

            # Wrap the serve_forever method in a lambda to allow it to be called by the asyncio event loop

            self.httpServerThread = Thread(target=self.httpServer.serve_forever)
            self.httpServerThread.start()

            self.webLogger.info("Started web server")

            self.run()
        except Exception as e:
            capture_exception(e)

    def __stopWebServer(self):
        try:
            self.webLogger.info("Stopping web server")
            self.httpServer.shutdown()
            self.httpServerThread.join()
            self.webLogger.info("Stopped web server")
        except Exception as e:
            capture_exception(e)

    def stop(self) -> None:
        """
        Stops the gateway.

        This method shuts down the HTTP server thread and waits for the console thread to join.
        """
        self.logger.info("Stopping gateway")

        self.consoleThread.stop()

        self.__stopWebServer()

        self.logger.info("Stopped gateway")

    def restart(self) -> None:
        """
        Restarts the gateway.

        This method stops the gateway and then starts it again.
        """
        self.logger.info("Restarting gateway")

        self.stop()
        self.start()

        self.logger.info("Restarted gateway")

    def run(self) -> None:
        """
        Runs the gateway.

        This method starts the gateway and then waits for the console thread to join.
        """
        while not self.shutdownRequested:
            pass

        self.stop()


gatewayInstance = None


def getGateway(
    config=getConfig(),
    logger=getLogger(__name__),
    portList=[],
    onSocketConnection=__onSocketConnection,
) -> GatewayServer:
    global gatewayInstance
    if gatewayInstance is None:
        gatewayInstance = GatewayServer(
            config=config,
            logger=logger,
            portList=portList,
            onSocketConnection=onSocketConnection,
        )
    return gatewayInstance
