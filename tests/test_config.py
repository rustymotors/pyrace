import unittest
from pyrace.shared.config import getConfig


class TestConfig(unittest.TestCase):
    def test_getConfig(self):
        config = getConfig()

        # Check if the configuration instance is not None
        self.assertIsNotNone(config)

        # Check if the configuration instance has the expected attributes
        self.assertTrue(hasattr(config, "EXTERNAL_HOST"))
        self.assertTrue(hasattr(config, "CERTIFICATE_FILE"))
        self.assertTrue(hasattr(config, "PRIVATE_KEY_FILE"))
        self.assertTrue(hasattr(config, "PUBLIC_KEY_FILE"))

        # Add more assertions as needed


if __name__ == "__main__":
    unittest.main()
