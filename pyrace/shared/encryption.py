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
    try:
        key = os.urandom(16).hex()
        _ = Cipher(algorithms.ARC4(bytes.fromhex(key)), mode=None)
        _ = Cipher(
            algorithms.TripleDES(bytes.fromhex(key)),
            modes.CBC(bytes.fromhex("0000000000000000")),
        )
    except Exception as e:
        raise Exception("Legacy cipher support is not available") from e
