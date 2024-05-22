
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
