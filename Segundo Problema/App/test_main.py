from App.numeros import numeros
import unittest


class testNumeros(unittest.TestCase):
    def testNum(self):
        n = numeros(24)
        self.assertEqual(n.parImpar(),0, msg=None)



if __name__ == "__main__":
    unittest.main(exit=False)

