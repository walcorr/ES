import unittest
from unittest import TestCase
def calcular_frequencias(s):
    dic={}
    for a in s:
        if a in dic.keys():
            dic[a]+=1
        else:
            dic[a]=1
    return dic
    pass


def gerar_arvore_de_huffman(s):
    dicionario=calcular_frequencias(s)
    for a,b in dicionario.items():
        char=a
        menor=b
        break
    for a,b in dicionario.items():
        if b<=menor:
            menor=b
            char=a
    dicionario.__delitem__(char)
    arvore=Arvore(char,menor)
    while len(dicionario.keys())>0:
        for a,b in dicionario.items():
            char=a
            menor=b
            break
        for a,b in dicionario.items():
            if b<=menor:
                char=a
                menor=b
        arvore=arvore.fundir(Arvore(char,menor))
        dicionario.__delitem__(char)
    return arvore
    pass

def codificar(cod_dict, s):
    codificado=""
    for cont in s:
        codificado=codificado+cod_dict.get(cont)
    return codificado
    pass

class Noh:
    def __hash__(self):
        return hash(self.peso)

    def __eq__(self, other):
        if other is None or not isinstance(other, Noh):
            return False
        return self.peso == other.peso and self.esquerdo == other.esquerdo and self.direito == other.direito
    def __init__(self,peso):
        self.peso=peso
        self.esquerdo=None
        self.direito=None
        self.caminho=None
    def sou(self):
        return "noh"

class Folha():
    def __hash__(self):
        return hash(self.__dict__)

    def __eq__(self, other):
        if other is None or not isinstance(other, Folha):
            return False
        return self.__dict__ == other.__dict__
    def __init__(self,char,peso):
        self.char=char
        self.peso=peso
    def sou(self):
        return "folha"

class Arvore(object):
    
    def __hash__(self):
        return hash(self.raiz)

    def __eq__(self, other):
        if other is None:
            return False
        return self.raiz == other.raiz


    def __init__(self,char=None,peso=None):
        self.dic={}
        if char==None:
            self.raiz=None
        else:
            self.raiz=Folha(char,peso)

    def decodificar(self,s):
        self.cod_dict()
        total=""
        vez=""
        for i in s:
            vez=vez+i
            for a,b in self.dic.items():
                if b==vez:
                    total=total+a
                    vez=""
        return total

    def fundir(self,arvore):
        NovaArvore=Arvore()
        NovaArvore.raiz=Noh(self.raiz.peso+arvore.raiz.peso)
        if self.raiz.peso > arvore.raiz.peso:
            NovaArvore.raiz.esquerdo=self.raiz
            NovaArvore.raiz.direito=arvore.raiz
        else:
            NovaArvore.raiz.direito=self.raiz
            NovaArvore.raiz.esquerdo=arvore.raiz
        return NovaArvore
    def cod_dict(self):
        caminho=""

        cod_dict_rec("",self.dic,self.raiz)
        return self.dic

def cod_dict_rec(caminho,dic,vez):
    
    if vez.sou()=="folha":
        dic[vez.char]=caminho
    else:
        cod_dict_rec(caminho+"0",dic,vez.esquerdo)
        cod_dict_rec(caminho+"1",dic,vez.direito)

class CalcularFrequenciaCarecteresTestes(TestCase):
    def teste_string_vazia(self):
        self.assertDictEqual({}, calcular_frequencias(''))

    def teste_string_nao_vazia(self):
        self.assertDictEqual({'a': 3, 'b': 2, 'c': 1}, calcular_frequencias('aaabbc'))

class NohTestes(TestCase):
    def teste_folha_init(self):
        folha = Folha('a', 3)
        self.assertEqual('a', folha.char)
        self.assertEqual(3, folha.peso)

    def teste_folha_eq(self):
        self.assertEqual(Folha('a', 3), Folha('a', 3))
        self.assertNotEqual(Folha('a', 3), Folha('b', 3))
        self.assertNotEqual(Folha('a', 3), Folha('a', 2))
        self.assertNotEqual(Folha('a', 3), Folha('b', 2))

    def testes_eq_sem_filhos(self):
        self.assertEqual(Noh(2), Noh(2))
        self.assertNotEqual(Noh(2), Noh(3))

    def testes_eq_com_filhos(self):
        noh_com_filho = Noh(2)
        noh_com_filho.esquerdo = Noh(3)
        self.assertNotEqual(Noh(2), noh_com_filho)

    def teste_noh_init(self):
        noh = Noh(3)
        self.assertEqual(3, noh.peso)
        self.assertIsNone(noh.esquerdo)
        self.assertIsNone(noh.direito)

def _gerar_arvore_aaaa_bb_c():
    raiz = Noh(7)
    raiz.esquerdo = Folha('a', 4)
    noh = Noh(3)
    raiz.direito = noh
    noh.esquerdo = Folha('b', 2)
    noh.direito = Folha('c', 1)
    arvore_esperada = Arvore()
    arvore_esperada.raiz = raiz
    return arvore_esperada

class ArvoreTestes(TestCase):
    def teste_init_com_defaults(self):
        arvore = Arvore()
        self.assertIsNone(arvore.raiz)

    def teste_init_sem_defaults(self):
        arvore = Arvore('a', 3)
        self.assertEqual(Folha('a', 3), arvore.raiz)

    def teste_fundir_arvores_iniciais(self):
        raiz = Noh(3)
        raiz.esquerdo = Folha('b', 2)
        raiz.direito = Folha('c', 1)
        arvore_esperada = Arvore()
        arvore_esperada.raiz = raiz
        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore_fundida = arvore.fundir(arvore2)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_fundir_arvores_nao_iniciais(self):
        arvore_esperada = _gerar_arvore_aaaa_bb_c()
        arvore = Arvore('b', 2)
        arvore2 = Arvore('c', 1)
        arvore3 = Arvore('a', 4)
        arvore_fundida = arvore.fundir(arvore2)
        arvore_fundida = arvore3.fundir(arvore_fundida)
        self.assertEqual(arvore_esperada, arvore_fundida)

    def teste_gerar_dicionario_de_codificacao(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertDictEqual({'a': '0', 'b': '10', 'c': '11'}, arvore.cod_dict())

    def teste_decodificar(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))

class TestesDeIntegracao(TestCase):
    def teste_gerar_arvore_de_huffman(self):
        arvore = _gerar_arvore_aaaa_bb_c()
        self.assertEqual(arvore, gerar_arvore_de_huffman('aaaabbc'))

    def teste_codificar(self):
        arvore = gerar_arvore_de_huffman('aaaabbc')
        self.assertEqual('0000101011', codificar(arvore.cod_dict(), 'aaaabbc'))
        self.assertEqual('aaaabbc', arvore.decodificar('0000101011'))


if __name__ == '__main__':
    unittest.main()
