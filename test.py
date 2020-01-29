import unittest
import tictactoe import Board

class TestStringMethods(unittest.TestCase):

    def test_init(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_mark_square(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_has_winner(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()