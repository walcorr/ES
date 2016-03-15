import unittest

class Pilha():
    def __init__(self):
        self.pilha = []

    def vazia(self):
        return len(self.pilha)==0

    def topo(self):
        if len(self.pilha)!=0:
            return self.pilha[-1]
        else:
            raise IndexError        
    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        if len(self.pilha)!=0:
            return self.pilha.pop()            
        else:
            raise IndexError


def esta_balanceada(expressao):
    ca=Pilha()
    co=Pilha()
    pa=Pilha()

    for c in expressao:
        if c=='[':
            co.empilhar(0)
        elif c=='{':
            ca.empilhar(0)
        elif c=='(':
            pa.empilhar(0)
        if c==']':
            try:
                co.desempilhar()
            except IndexError:
                return False
        elif c=='}':
            try:
                ca.desempilhar()
            except IndexError:
                return False
        elif c==')':
            try:
                pa.desempilhar()
            except IndexError:
                return False
    if ca.vazia() and co.vazia() and pa.vazia():
        return True
    else:
        return False
    """
    Função que calcula se expressão possui parenteses, colchetes e chaves balanceados
    O Aluno deverá informar a complexidade de tempo e espaço da função
    Deverá ser usada como estrutura de dados apenas a pilha feita na aula anterior
    :param expressao: string com expressao a ser balanceada
    :return: boleano verdadeiro se expressao está balanceada e falso caso contrário
    """
    pass


class BalancearTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertTrue(esta_balanceada(''))

    def test_parenteses(self):
        self.assertTrue(esta_balanceada('()'))

    def test_chaves(self):
        self.assertTrue(esta_balanceada('{}'))

    def test_colchetes(self):
        self.assertTrue(esta_balanceada('[]'))

    def test_todos_caracteres(self):
        self.assertTrue(esta_balanceada('({[]})'))
        self.assertTrue(esta_balanceada('[({})]'))
        self.assertTrue(esta_balanceada('{[()]}'))

    def test_chave_nao_fechada(self):
        self.assertFalse(esta_balanceada('{'))

    def test_colchete_nao_fechado(self):
        self.assertFalse(esta_balanceada('['))

    def test_parentese_nao_fechado(self):
        self.assertFalse(esta_balanceada('('))

    def test_chave_nao_aberta(self):
        self.assertFalse(esta_balanceada('}{'))

    def test_colchete_nao_aberto(self):
        self.assertFalse(esta_balanceada(']['))

    def test_parentese_nao_aberto(self):
        self.assertFalse(esta_balanceada(')('))

    def test_falta_de_caracter_de_fechamento(self):
        self.assertFalse(esta_balanceada('({[]}'))

    def test_falta_de_caracter_de_abertura(self):
        self.assertFalse(esta_balanceada('({]})'))

    def test_expressao_matematica_valida(self):
        self.assertTrue(esta_balanceada('({[1+3]*5}/7)+9'))

    def test_char_errado_fechando(self):
        self.assertFalse(esta_balanceada('[)'))


if __name__ == '__main__':
    unittest.main()
