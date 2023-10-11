import unittest
from Seminar_13.Homework.z1 import Rectangle, NegativeValueError

class TestRec(unittest.TestCase):
    def setUp(self):
        self.rec = Rectangle(4, 3)
        self.rec2 = Rectangle(8, 2)

    def test1(self):
        self.assertEqual(self.rec.perimeter(), 14)

    def test2(self):
        self.rec.height = 4
        self.assertTrue(self.rec.area() == 16)

    def test4(self):
        self.assertNotEqual(self.rec.area(), self.rec2.area())

    def test5(self):
        self.assertRaises(NegativeValueError, Rectangle, (-5, 1))

    def test6(self):
        self.assertFalse(Rectangle(4, 3) is Rectangle(3, 4))


if __name__ == '__main__':
    unittest.main(verbosity=2)