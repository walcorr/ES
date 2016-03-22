# Exercício de avaliação de expressão aritmética.
# Só podem ser usadas as estruturas Pilha e Fila implementadas em aulas anteriores.
# Deve ter análise de tempo e espaço para função avaliação
from collections import deque
from aula5.fila import Fila
from aula4.pilha import Pilha


'''
O(n) para tempo, pois percorrerá toda a expressão
O(n) para memoria pois a pilha irá crescer de acordo com a expressão, mesmo que possua variaveis
que permanecem constantes
'''


class ErroLexico(Exception):
    pass


class ErroSintatico(Exception):
    pass


def analise_lexica(expressao):
    fila=Fila()
    num=""
    if len(expressao):
        for t in expressao:
            if t in set("0123456789"):
                num=num+t
            else:
                if len(num)>0:
                    fila.enfileirar(num)
                    num=""
                if t in set("{}[]()/+-*."):
                    fila.enfileirar(t)
                else:
                    raise ErroLexico("Erro Léxico")
                
        if not len(num)==0:
            fila.enfileirar(num)
    return fila

        
            
        
    """
    Executa análise lexica transformando a expressao em fila de objetos:
    Transforma inteiros em ints
    Flutuantes em floats
    e verificar se demais caracteres são validos: +-*/(){}[]
    :param expressao: string com expressao a ser analisada
    :return: fila com tokens
    """
    pass


def analise_sintatica(fila):
    """
    Função que realiza analise sintática de tokens produzidos por analise léxica.
    Executa validações sintáticas e se não houver erro retorn fila_sintatica para avaliacao

    :param fila: fila proveniente de análise lexica
    :return: fila_sintatica com elementos tokens de numeros
    """
    
    num=0
    ponto=False
    tokens=Fila()
    if len(fila)>0:
        for t in fila:
            if t in set("{}[]()/+-*"):
                if not num==0:
                    tokens.enfileirar(num)
                num=0
                tokens.enfileirar(t)
                ponto=False
                
                    
            else:
                if t in ("."):
                    ponto=True
                else:
                    val=int(t)
                    if ponto:
                        num=num+(val/10**len(t))
                    else:
                        num=num+val
                    
        if not num==0:
                    tokens.enfileirar(num)
        return tokens
    else:
        raise ErroSintatico("erro")
    


def avaliar(expressao):
    fila=analise_sintatica(analise_lexica(expressao))
    res=Pilha()
    var3,var2,var1 = None,None,None
    aux=0
    for t in fila:
        res.empilhar(t)
        
        if len(res)>=3:
            var3=res.desempilhar()
            var2=res.desempilhar()
            var1=res.desempilhar()
            if str(var2) in "+-*/" and not str(var1) in "([{" and not str(var3) in "([{" :
                if var2 == "+":
                    aux=var1+var3
                elif var2 == "/":
                    aux=var1/var3
                elif var2 == "-":
                    aux=var1-var3
                elif var2 == "*":
                    aux=var1*var3
                res.empilhar(aux)
            else:
                res.empilhar(var1)
                res.empilhar(var2)
                res.empilhar(var3)
        if str(t) in ")}]":
            res.desempilhar()
            aux=res.desempilhar()
            res.desempilhar()
            res.empilhar(aux)
            if len(res)>=3:
                var3=res.desempilhar()
                var2=res.desempilhar()
                var1=res.desempilhar()
                if str(var2) in "+-*/" and not str(var1) in "([{" and not str(var3) in "([{" :
                    if var2 == "+":
                        aux=var1+var3
                    elif var2 == "/":
                        aux=var1/var3
                    elif var2 == "-":
                        aux=var1-var3
                    elif var2 == "*":
                        aux=var1*var3
                    res.empilhar(aux)
                else:
                    res.empilhar(var1)
                    res.empilhar(var2)
                    res.empilhar(var3)
            
        
    return res.desempilhar()
    """
    Função que avalia expressão aritmetica retornando se valor se não houver nenhum erro
    :param expressao: string com expressão aritmética
    :return: valor númerico com resultado
    """
    pass


import unittest


class AnaliseLexicaTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        fila = analise_lexica('')
        self.assertTrue(fila.vazia())

    def test_caracter_estranho(self):
        self.assertRaises(ErroLexico, analise_lexica, 'a')
        self.assertRaises(ErroLexico, analise_lexica, 'ab')

    def test_inteiro_com_um_algarismo(self):
        fila = analise_lexica('1')
        self.assertEqual('1', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_inteiro_com_vários_algarismos(self):
        fila = analise_lexica('1234567890')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_float(self):
        fila = analise_lexica('1234567890.34')
        self.assertEqual('1234567890', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('34', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_parenteses(self):
        fila = analise_lexica('(1)')
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_chaves(self):
        fila = analise_lexica('{(1)}')
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_colchetes(self):
        fila = analise_lexica('[{(1.0)}]')
        self.assertEqual('[', fila.desenfileirar())
        self.assertEqual('{', fila.desenfileirar())
        self.assertEqual('(', fila.desenfileirar())
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertEqual(')', fila.desenfileirar())
        self.assertEqual('}', fila.desenfileirar())
        self.assertEqual(']', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_adicao(self):
        fila = analise_lexica('1+2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('+', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_subtracao(self):
        fila = analise_lexica('1-2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('-', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_multiplicacao(self):
        fila = analise_lexica('1*2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('*', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_divisao(self):
        fila = analise_lexica('1/2.0')
        self.assertEqual('1', fila.desenfileirar())
        self.assertEqual('/', fila.desenfileirar())
        self.assertEqual('2', fila.desenfileirar())
        self.assertEqual('.', fila.desenfileirar())
        self.assertEqual('0', fila.desenfileirar())
        self.assertTrue(fila.vazia())

    def test_expresao_com_todos_simbolos(self):
        expressao = '1/{2.0+3*[7-(5-3)]}'
        fila = analise_lexica(expressao)
        self.assertListEqual(list(expressao), [e for e in fila])
        self.assertTrue(fila.vazia())


class AnaliseSintaticaTestes(unittest.TestCase):
    def test_fila_vazia(self):
        fila = Fila()
        self.assertRaises(ErroSintatico, analise_sintatica, fila)

    def test_int(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_float(self):
        fila = Fila()
        fila.enfileirar('1234567890')
        fila.enfileirar('.')
        fila.enfileirar('4')
        fila_sintatica = analise_sintatica(fila)
        self.assertEqual(1234567890.4, fila_sintatica.desenfileirar())
        self.assertTrue(fila_sintatica.vazia())

    def test_expressao_com_todos_elementos(self):
        fila = analise_lexica('1000/{222.125+3*[7-(5-3)]}')
        fila_sintatica = analise_sintatica(fila)
        self.assertListEqual([1000, '/', '{', 222.125, '+', 3, '*', '[', 7, '-', '(', 5, '-', 3, ')', ']', '}'],
                             [e for e in fila_sintatica])


class AvaliacaoTestes(unittest.TestCase):
    def test_expressao_vazia(self):
        self.assertRaises(ErroSintatico, avaliar, '')

    def test_inteiro(self):
        self.assert_avaliacao('1')

    def test_float(self):
        self.assert_avaliacao('2.1')

    def test_soma(self):
        self.assert_avaliacao('2+1')

    def test_subtracao_e_parenteses(self):
        self.assert_avaliacao('(2-1)')

    def test_expressao_com_todos_elementos(self):
        self.assertEqual(1.0, avaliar('2.0/[4*3+1-{15-(1+3)}]'))

    def assert_avaliacao(self, expressao):
        self.assertEqual(eval(expressao), avaliar(expressao))


if __name__ == '__main__':
    unittest.main()
