from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def verifyLegacyCipherSupport():
    """
    Verifies the support for legacy ciphers.

    This function generates a random key and creates two ciphers using different algorithms.
    It checks if the ciphers are supported by the system.

    Returns:
        None
    """
    key = os.urandom(16).hex()
    dataCypher = Cipher(algorithms.ARC4(bytes.fromhex(key)), mode=None)
    cmdCypher = Cipher(algorithms.TripleDES(bytes.fromhex(key)), modes.CBC(bytes.fromhex("0000000000000000")))
    
    

