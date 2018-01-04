import unittest
from fib_standard import fib_standard
from fib_recursive import fib_rec_memo

class MyTest(unittest.TestCase):
    pass

def test_gen(expected, actual):
    def test_method(self):
        return self.assertEqual(expected, actual)
    return test_method


if __name__ == '__main__':
    cases = ((fib_standard(38), 39088169), (fib_rec_memo(38), 39088169))
    for index, case in enumerate(cases):
        test_name = 'test_{0}'.format(index)
        test = test_gen(case[1], case[0])
        setattr(MyTest, test_name, test)
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
