class Pilha():
    def __init__(self):
        self.pilha = []

    def vazia(self):
        return len(self.pilha)==0

    def topo(self):
        if len(self.pilha)!=0:
            return self.pilha[-1]
        else:
            erro=PilhaVaziaErro(IndexError)
            raise erro
    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if len(self.pilha)!=0:
            return self.pilha.pop()            
        else:
            erro=PilhaVaziaErro(IndexError)
            raise erro

class PilhaVaziaErro(Exception):
    pass


import unittest

class PilhaTestes(unittest.TestCase):
    def test_topo_lista_vazia(self):
        pilha = Pilha()
        self.assertTrue(pilha.vazia())
        self.assertRaises(PilhaVaziaErro, pilha.topo)

    def test_empilhar_um_elemento(self):
        pilha = Pilha()
        pilha.empilhar('A')
        self.assertFalse(pilha.vazia())
        self.assertEqual('A', pilha.topo())

    def test_empilhar_dois_elementos(self):
        pilha = Pilha()
        pilha.empilhar('A')
        pilha.empilhar('B')
        self.assertFalse(pilha.vazia())
        self.assertEqual('B', pilha.topo())

    def test_desempilhar_pilha_vazia(self):
        pilha = Pilha()
        self.assertRaises(PilhaVaziaErro, pilha.desempilhar)

    def test_desempilhar(self):
        pilha = Pilha()
        letras = 'ABCDE'
        for letra in letras:
            pilha.empilhar(letra)

        for letra_em_ordem_reversa in reversed(letras):
            letra_desempilhada = pilha.desempilhar()
            self.assertEqual(letra_em_ordem_reversa, letra_desempilhada)

if __name__ == '__main__':
    unittest.main()
