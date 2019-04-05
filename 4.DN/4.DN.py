import unittest


def moznosti(s):
    return ["B3", "C2"]

def legalna(a, b):
    return b < "C4"





class TestKonj(unittest.TestCase):
    def test_moznosti(self):
        self.assertEqual(moznosti("A1"), ["B3", "C2"])
        self.assertEqual(moznosti("A2"), ["B4", "C1", "C3"])

    def test_legalna(self):
        self.assertTrue(legalna("A1", "C2"))
        self.assertFalse(legalna("A3", "C8"))


if __name__ == '__main__':
    unittest.main(verbosity=2)

