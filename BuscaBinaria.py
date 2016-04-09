def busca_binaria(seq,procurado ):
    """
    O(log n) em tempo de execução já que o while vai percorrer a sequencia
    O(1) em memória pois possuirá apenas a sequencia e variaveis auxiliares
    """
    if len(seq)==0:
        return 0
    else:
        i=0
        f=len(seq)-1
        while(i<=f):
            m=(i+f)//2
            if procurado>seq[m]:
                i=m+1
            else:
                f=m-1
    if procurado>seq[m]:
        return m+1
    else:
        return m
        
import unittest


class BuscaBinariaTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertEqual(0, busca_binaria([], 1))
        self.assertEqual(0, busca_binaria([], 2))
        self.assertEqual(0, busca_binaria([], 3))

    def teste_lista_unitaria(self):
        self.assertEqual(0, busca_binaria([1], 0))
        self.assertEqual(0, busca_binaria([1], 1))
        self.assertEqual(1, busca_binaria([1], 2))
        self.assertEqual(1, busca_binaria([1], 3))
        self.assertEqual(1, busca_binaria([1], 4))

    def teste_lista_nao_unitaria(self):
        lista = list(range(10))
        self.assertEqual(0, busca_binaria(lista, -2))
        self.assertEqual(0, busca_binaria(lista, -1))
        for i in lista:
            self.assertEqual(i, busca_binaria(lista, i))
        self.assertEqual(10, busca_binaria(lista, 10))
        self.assertEqual(10, busca_binaria(lista, 11))
        self.assertEqual(10, busca_binaria(lista, 12))

    def teste_lista_elementos_repetidos(self):
        lista = [1, 1, 1, 2, 2, 2]
        self.assertEqual(0, busca_binaria(lista, 1))
        self.assertEqual(3, busca_binaria(lista, 2))

if __name__ == '__main__':
    unittest.main()
