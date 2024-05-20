import unittest
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

class TestEncryption(unittest.TestCase):
    def test_verifyLegacyCipherSupport(self):
        key = os.urandom(16).hex()
        dataCipher = Cipher(algorithms.ARC4(bytes.fromhex(key)), mode=None)
        cmdCipher = Cipher(algorithms.TripleDES(bytes.fromhex(key)), modes.CBC(bytes.fromhex("0000000000000000")))

        # Assert that the ciphers are supported by the system
        self.assertIsNotNone(dataCipher)
        self.assertIsNotNone(cmdCipher)

if __name__ == '__main__':
    unittest.main()