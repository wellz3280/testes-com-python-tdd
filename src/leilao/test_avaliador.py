from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_adicionados_em_ordem_crescente(self):
        well = Usuario('weliton')
        val = Usuario('valderez')

        lance_well = Lance(well, 100.0)
        lance_val = Lance(val, 150.0)

        leilao = Leilao('celular')

        leilao.lances.append(lance_well)
        leilao.lances.append(lance_val)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_adicionados_em_ordem_decrescente(self):
        well = Usuario('weliton')
        val = Usuario('valderez')

        lance_val = Lance(val, 150.0)
        lance_well = Lance(well, 100.0)

        leilao = Leilao('celular')

        leilao.lances.append(lance_well)
        leilao.lances.append(lance_val)

        avaliador = Avaliador()
        avaliador.avalia(leilao)
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado,avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado,avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tem_apenas_um_lance(self):
        gui = Usuario('gui')
        lance = Lance(gui,150.0)
        leilao = Leilao('celular')
        leilao.lances.append(lance)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150.0,avaliador.menor_lance)
        self.assertEqual(150.0,avaliador.maior_lance)
