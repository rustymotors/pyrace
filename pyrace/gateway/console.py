from curtsies.input import Input
from threading import Thread
from pyrace.base import ServerBase
from pyrace.shared.logging import getLogger


class ConsoleThread(Thread, ServerBase):
    
    def __init__(
        self,
        parentThread: ServerBase,
        logger = getLogger("console")
    ) -> None:
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