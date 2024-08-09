import unittest
from pyrace.shared import encryption


class TestEncryption(unittest.TestCase):
    def test_verifyLegacyCipherSupport(self):

        try:
            encryption.verifyLegacyCipherSupport()
        except Exception as e:
            self.fail("verifyLegacyCipherSupport() raised an exception: " + str(e))

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
