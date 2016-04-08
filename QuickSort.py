import unittest
seq = [1, 1, 2]

def _quick_recursivo(seq, ini, fim):
    if ini>= fim:
        return seq
    else:
        indpivot = fim
        pivot = seq[indpivot]
        indme = ini
        indma = fim
        while(indme<indma):
            if(seq[indme]<=pivot):
                indme+=1
            elif(seq[indma]>=pivot):
                indma-=1
            else:
                seq[indme],seq[indma]=seq[indma],seq[indme]
         # posicionar pivot
        seq[indme],seq[indpivot]=seq[indpivot],seq[indme]
        indpivot=indme
        # Resolver para sublista da esquerda
        _quick_recursivo(seq,ini,indpivot-1)
        # Resolver para sublista da direita
        _quick_recursivo(seq,indpivot+1,fim)
        return seq

def quick_sort(seq):
    return _quick_recursivo(seq, 0, len(seq) - 1)

class OrdenacaoTestes(unittest.TestCase):
    def teste_lista_vazia(self):
        self.assertListEqual([], quick_sort([]))

    def teste_lista_unitaria(self):
        self.assertListEqual([1], quick_sort([1]))

    def teste_lista_binaria(self):
        self.assertListEqual([1, 2], quick_sort([2, 1]))

    def teste_lista_desordenada(self):
        self.assertListEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], quick_sort([9, 7, 1, 8, 5, 3, 6, 4, 2, 0]))


if __name__ == '__main__':
    unittest.main()
