# fracao.py

class Fracao:
    def __init__(self, numerador, denominador):
        if (denominador == 0):
            raise ValueError("Denominador não pode ser zero.")
        mdc = 1
        for i in range(min(numerador, denominador), 1, -1):
            if numerador % i == 0 and denominador % i == 0:
                mdc = i 
                break
        self._numerador = numerador // mdc
        self._denominador = denominador // mdc      
    
    @property
    def numerador(self):
        return self._numerador

    @property
    def denominador(self):
        return self._denominador