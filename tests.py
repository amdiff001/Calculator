import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(3, 5), 8)


if __name__ == '__main__':
    unittest.main()
