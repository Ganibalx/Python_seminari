import unittest
from Seminar_14.z1 import clear_text

class TestMy(unittest.TestCase):
    def setUp(self):
        self.correct = 'text'
        self.first = 'TeXt'
        self.second = 'Te....Xвыаываt'
        self.third = 'Te.sd...Xвыаываt'

    def test1(self):
        self.assertEqual(self.correct, clear_text(self.first))

    def test2(self):
        self.assertTrue(clear_text(self.first) == clear_text(self.second))

    def test4(self):
        self.assertFalse(self.correct is clear_text(self.third))

    def test5(self):
        self.assertRaises(ValueError, clear_text, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
