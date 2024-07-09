# test_fracao.py

import unittest
from Fracao import Fracao

class fracao_test(unittest.TestCase):

    # teste 1 de construtor
    def test_construtor_1(self):
        f = Fracao(2,3)
        self.assertEqual(2, f.numerador)
        self.assertEqual(3, f.denominador)

    # teste 2 denominador igual a zero
    def test_construtor_2(self):
        with self.assertRaises(ValueError):
            f = Fracao(2,0)
    
    # teste 3 simplificação de fracao
    def test_construtor_3(self):
        f = Fracao(2,4)
        self.assertEqual(1, f.numerador)
        self.assertEqual(2, f.denominador)

if __name__ == '__main__':
    unittest.main()