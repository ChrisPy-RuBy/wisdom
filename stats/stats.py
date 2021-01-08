
import unittest
import operator

def absolute_trick(w_1, w_2, data, alpha):
    for x, y in data:
        p, q = x, y
        q_prime = w_1 * p + w_2
        w_1_op = operator.add if q_prime < q else operator.sub
        w_2_op = operator.sub if w_2 > y else operator.add
    return (w_1_op(w_1,p * alpha)), w_2_op(w_2, 1 * alpha)


def square_trick(w_1, w_2, data, alpha):
    for x, y in data:
        p, q = x, y
        q_prime = w_1 * p + w_2

    return (w_1 + p * (q - q_prime) * alpha), (w_2 + (q - q_prime) * alpha)


def mean_absolute_error(function, data):

    values = []
    for x, y in data:
        abs_error = abs(y - function(x))
        values.append(abs_error)
    return sum(values) / len(values)


def mean_square_error(function, data):

    values = []
    for x, y in data:
        square_error = (y - function(x))**2
        values.append(square_error)
    return sum(values) / (2 * len(values))


class TestAbsoluteError(unittest.TestCase):

    def test_mean_absolute_error(self):
        data = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
        def function(x): return 1.2 * x + 2
        result = mean_absolute_error(function, data)
        self.assertEqual(result, 3.88)

    def test_new_function(self):
        pass

    def test_mean_square_error(self):
        data = [(2, -2), (5, 6), (-4, -4), (-7, 1), (8, 14)]
        def function(x): return 1.2 * x + 2
        result = mean_square_error(function, data)
        self.assertEqual(round(result, 2), 10.69)

    def test_absolute_trick(self):
        point = [(-5, 3)]
        def function(x): return -0.6 * x + 4
        w_1, w_2 = absolute_trick(-0.6, 4, point, 0.1)
        self.assertEqual(round(w_1, 2), -0.1)
        self.assertEqual(round(w_2, 2), 3.9)

    def test_square_trick(self):
        point = [(-5, 3)]
        def function(x): return -0.6 * x + 4
        w_1, w_2 = square_trick(-0.6, 4, point, 0.01)
        self.assertEqual(round(w_1, 2), -0.4)
        self.assertEqual(round(w_2, 2), 3.96)
