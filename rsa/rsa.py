"""Super simple implementation of the process involved in
RSA encryption.
"""
import unittest


def egcd(a, b):
    """Extended general common denominator algo.
    """
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def modinv(a, m):
    """Modulo inverse
    """
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def generate_public_key(p, q):
    return p * q


def generate_private_key(p, q, e):
    m = (p - 1) * (q - 1)
    return modinv(e, m)


def encode_message(message, public_key, e):
    # transform message into an integer
    numbers = [int(bin(c), 2) for c in message.encode("ascii")]
    print(numbers)

    def encrypt(num, N, e):
        return num**e % N
    return [encrypt(n, public_key, e) for n in numbers]


def decode_message(message, public_key, private_key):

    def decrypt(num, N, d):
        return num**d % N
    decrypt = [decrypt(num, public_key, private_key) for num in message]
    # Remember that a bytes object is just a list of numbers.
    # So create a bytes object from the numbers and decode
    # to create the string
    return bytes(decrypt).decode('ascii')


class TestRSA(unittest.TestCase):

    def test_generate_public_key(self):
        public_key = generate_public_key(17, 11)
        self.assertEqual(187, public_key)

    def test_generate_private_key(self):
        private_key = generate_private_key(17, 11, 7)
        self.assertEqual(23, private_key)

    def test_encode_message(self):
        encoded_message = encode_message("X", 187, 7)
        expected_message = [11]
        self.assertEqual(expected_message, encoded_message)

    def test_decode_message(self):
        decoded_message = decode_message([11], 187, 23)
        expected_message = "X"
        self.assertEqual(expected_message, decoded_message)
