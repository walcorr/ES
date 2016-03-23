import unittest
def ordenar(seq):

    '''
    para memória O(1) pois possuirá apenas a lista e uma variavel apenas
    Tempo de execução O(n²) pois tem um for dentro de outro for percorrendo a lista
    o melhor caso seria se já estivesse ordenado pois iria percorrer apenas uma vez a lista
    se fosse verificasse que não ouve troca
    '''
    flag=True
    for i in range(len(seq)-1):
        for a in range(len(seq)-1):
            if seq[a]>seq[a+1]:
                flag=False
                seq[a],seq[a+1]=seq[a+1],seq[a]
        if(flag):
            print("lista ordenada")
            break
    return seq
    pass


class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], ordenar([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], ordenar([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], ordenar([2, 1]))


    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], ordenar([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
