import logging
from threading import Thread
from webbrowser import get

from pyrace.shared.config import getConfig

def __onSocketConnection(socket, logger=logging.getLogger(__name__)) -> None:
    pass

class __Gateway(Thread):
    
    def __init__(self, config, logger, portList, onSocketConnection) -> None:
        self.config = config
        self.logger = logger
        self.portList = portList
        self.onSocketConnection = onSocketConnection
        
        self.logger.info("Starting gateway with the following configuration: %s", self.config)
        pass
    
    def start(self) -> None:
        self.logger.info("Starting gateway")
        pass

gatewayInstance = None

def getGateway(config=getConfig(), logger=logging.getLogger(__name__), portList= [], onSocketConnection=__onSocketConnection) -> __Gateway:
    global gatewayInstance
    if gatewayInstance is None:
        gatewayInstance = __Gateway(
            config=config,
            logger=logger,
            portList=portList,
            onSocketConnection=onSocketConnection
        )
    return gatewayInstance
