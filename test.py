import unittest
import example


class TestCase(unittest.TestCase):

    def test_add_1(self):
        self.assertEqual(example.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(example.sub(5, 3), 2)


if __name__ == '__main__':
    unittest.main()
