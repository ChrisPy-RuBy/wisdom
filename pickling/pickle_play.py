import math
import pickle
import unittest


class Gerkin:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def radius(self):
        return self._width / 2

    @property
    def volume(self):
        return math.pi * self.radius * 2 * self._length

    def __repr__(self):
        return f"Gerkin(length={self._length}, width={self._width})"


def main():
    gerkin = Gerkin(4, 2)
    x = pickle.dumps(gerkin)
    import pdb; pdb.set_trace() 




if __name__ == "__main__":
    main()



class TestPickle(unittest.TestCase):

    """run tests with
    python -m  unittest pickle.py
    """

    def test_generate_gerkin_radius(self):
        gerkin = Gerkin(4, 2)
        r = gerkin.radius
        self.assertEqual(1, r)

    def test_generate_volume(self):
        gerkin  = Gerkin(4, 2)
        v = gerkin.volume
        self.assertEqual(25.13, round(v, 2))

