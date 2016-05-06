import unittest
from itertools import product

regra = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wzyz'}

def gerar_alfa(s):
    """
    O(3^n)para espaço, pois cada elemento de entrada gera 3 ou 4 elementos de saida
    O(n^2)para tempo pois para cada elemento realiza um while dentro de um for
    """
    resposta=[tuple()]
    for i in s:
        posicao=len(resposta)-1
        while(posicao>=0):
            posicaoAtual=resposta.pop(posicao)
            l=regra.__getitem__(i)
            for t in l:
                resposta.append(posicaoAtual+tuple(t,))
            posicao-=1
    return resposta

class Testes(unittest.TestCase):
    def testes_string_vazia(self):
        self.assertListEqual([tuple()], list(gerar_alfa('')))

    def testes_string_2(self):
        self.assertListEqual([('a',), ('b',), ('c',)], list(gerar_alfa('2')))

    def testes_string_3(self):
        self.assertListEqual([('d',), ('e',), ('f',)], list(gerar_alfa('3')))

    def testes_string_com_2_numeros(self):
        self.assertSetEqual(set((('a', 'd'), ('a', 'e'), ('a', 'f'), ('b', 'd'), ('b', 'e'), ('b', 'f'), ('c', 'd'),
                                 ('c', 'e'), ('c', 'f'))), set(gerar_alfa('23')))

    def testes_com_5_numeros(self):
        resultado = set(gerar_alfa('73696'))
        self.assertIn(tuple('renzo'), resultado)
        self.assertSetEqual(set(product('pqrs', 'def', 'mno', 'wzyz', 'mno')), resultado)

if __name__ == '__main__':
    unittest.main()
