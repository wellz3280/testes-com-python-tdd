from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def setUp(self):

        self.val = Usuario('valderez')
        self.lance_val = Lance(self.val, 150.0)
        self.leilao = Leilao('celular')
        return self.leilao

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_adicionados_em_ordem_crescente(self):
        well = Usuario('weliton')
        lance_well = Lance(well, 100.0)

        self.leilao.lances.append(lance_well)
        self.leilao.lances.append(self.lance_val)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_adicionados_em_ordem_decrescente(self):
        well = Usuario('weliton')
        lance_well = Lance(well, 100.0)

        self.leilao.lances.append(lance_well)
        self.leilao.lances.append(self.lance_val)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tem_apenas_um_lance(self):
        self.leilao.lances.append(self.lance_val)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150.0,avaliador.menor_lance)
        self.assertEqual(150.0,avaliador.menor_lance)


    def test_deve_retornar_o_maior_e_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        well = Usuario('weliton')
        lance_well = Lance(well, 100.0)

        vini = Usuario('vinicius')
        lance_vini = Lance(vini, 200.0)

        self.leilao.lances.append(lance_well)
        self.leilao.lances.append(self.lance_val)
        self.leilao.lances.append(lance_vini)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)