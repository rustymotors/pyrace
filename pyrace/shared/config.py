import os

from .logging import getLogger

default_config = {
    "EXTERNAL_HOST": "localhost",
    "CERTIFICATE_FILE": "certificates/certificate.pem",
    "PRIVATE_KEY_FILE": "certificates/privatekey.pem",
    "PUBLIC_KEY_FILE": "certificates/publickey.pem",
}


class __Config:

    def __init__(self, logger):
        self.logger = logger

        self.EXTERNAL_HOST = os.getenv("EXTERNAL_HOST", default_config["EXTERNAL_HOST"])
        self.CERTIFICATE_FILE = os.getenv(
            "CERTIFICATE_FILE", default_config["CERTIFICATE_FILE"]
        )
        self.PRIVATE_KEY_FILE = os.getenv(
            "PRIVATE_KEY_FILE", default_config["PRIVATE_KEY_FILE"]
        )
        self.PUBLIC_KEY_FILE = os.getenv(
            "PUBLIC_KEY_FILE", default_config["PUBLIC_KEY_FILE"]
        )
        self.logger.info("Configuration loaded")

    def __str__(self):
        return str(
            {
                "EXTERNAL_HOST": self.EXTERNAL_HOST,
                "CERTIFICATE_FILE": self.CERTIFICATE_FILE,
                "PRIVATE_KEY_FILE": self.PRIVATE_KEY_FILE,
                "PUBLIC_KEY_FILE": self.PUBLIC_KEY_FILE,
            }
        )


__configInstance = None


def getConfig(logger=getLogger("shared.config")):
    """
    Retrieves the configuration instance.

    Args:
        logger (Logger, optional): The logger instance to use for logging. Defaults to getLogger("shared.config").

    Returns:
        __configInstance (__Config): The configuration instance.

    """
    global __configInstance
    if __configInstance is None:
        __configInstance = __Config(logger=logger)
    return __configInstance
