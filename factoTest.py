import unittest

def facto(a):
    if a == 0 or a == 1:
        return 1
    elif a < 0:
        print("[ERROR] Out Of Range")
        return None
    else:
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result
    

class TestFacto(unittest.TestCase):

    def test_facto_0(self):
        self.assertEqual(facto(0), 1)

    def test_facto_1(self):
        self.assertEqual(facto(1), 1)

    def test_factorial_5(self):
        self.assertEqual(facto(5), 120)

    def test_factorial_negative(self):
        self.assertEqual(facto(-1), None)

if __name__ == "__main__" :
    unittest.main()