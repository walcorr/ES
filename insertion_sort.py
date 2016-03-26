import unittest

def insertion_sort(seq):
    '''
    para memória O(1) pois possuirá apenas a lista e três variaveis auxiliares apenas
    Tempo de execução O(n²) pois possui um while dentro de outro while para percorrer a lista e realizar a ordenação
   '''
    if len(seq)<=1:
        return seq
    else:
        lio=0
        ind=0
        while ind<len(seq):
            ino=lio
            if seq[ind]>seq[lio]:
                ind+=1
                lio+=1
            else:
                ind+=1
                lio+=1
                while ino>0:
                    if seq[ino-1]>seq[ino]:
                        seq[ino-1],seq[ino]=seq[ino],seq[ino-1]
                    ino-=1
    
    return seq        

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], insertion_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], insertion_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], insertion_sort([2, 1]))

    def teste_lista_binaria(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertion_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))

if __name__ == '__main__':
    unittest.main()
