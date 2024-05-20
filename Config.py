import os

default_config = {
    "EXTERNAL_HOST": "localhost",
    "CERTIFICATE_FILE": "certificates/certificate.pem",
    "PRIVATE_KEY_FILE": "certificates/privatekey.pem",
    "PUBLIC_KEY_FILE": "certificates/publickey.pem",
}


class Config:
    EXTERNAL_HOST = None
    CERTIFICATE_FILE = None
    PRIVATE_KEY_FILE = None
    PUBLIC_KEY_FILE = None

    def __init__(self):
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

    def __str__(self):
        return str(
            {
                "EXTERNAL_HOST": self.EXTERNAL_HOST,
                "CERTIFICATE_FILE": self.CERTIFICATE_FILE,
                "PRIVATE_KEY_FILE": self.PRIVATE_KEY_FILE,
                "PUBLIC_KEY_FILE": self.PUBLIC_KEY_FILE,
            }
        )
