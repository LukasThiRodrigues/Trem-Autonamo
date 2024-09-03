# tests/test_trem_autonomo.py

import unittest
from tremAutonomo import TremAutonomo
from exceptions import (
    ComandoInvalidoError,
    ListaComandosVaziaError,
    MovimentoExcedeLimiteError,
    MovimentosConsecutivosError
)

class TestTremAutonomo(unittest.TestCase):

    def test_movimentos_simples_direita(self):
        trem = TremAutonomo()
        comandos = ["DIREITA", "DIREITA"]
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, 2)

    def test_movimento_simples_esquerda(self):
        trem = TremAutonomo()
        comandos = ["ESQUERDA"]
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, -1)

    def test_movimentos_mistos(self):
        trem = TremAutonomo()
        comandos = ["ESQUERDA", "DIREITA", "DIREITA", "DIREITA", "DIREITA", "ESQUERDA"]
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, 2)

    def test_lista_comandos_vazia(self):
        trem = TremAutonomo()
        comandos = []
        with self.assertRaises(ListaComandosVaziaError):
            trem.mover(comandos)

    def test_comando_invalido(self):
        trem = TremAutonomo()
        comandos = ["DIREITA", "SUBIDA"]
        with self.assertRaises(ComandoInvalidoError):
            trem.mover(comandos)

    def test_comando_formato_incorreto(self):
        trem = TremAutonomo()
        comandos = ["direita", "ESQUERDA"]  # 'direita' em minúsculas
        with self.assertRaises(ComandoInvalidoError):
            trem.mover(comandos)

    def test_excede_movimentos_totais(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 55  # 55 movimentos
        posicao_final = trem.mover(comandos)
        self.assertEqual(trem.movimentos_totais, 50)
        self.assertEqual(posicao_final, 50)

    def test_excede_movimentos_consecutivos(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 21  # 21 movimentos consecutivos
        with self.assertRaises(MovimentosConsecutivosError):
            trem.mover(comandos)

    def test_condicao_borda_negativa(self):
        trem = TremAutonomo()
        comandos = ["ESQUERDA"]
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, -1)

    def test_condicao_borda_limite_movimentos(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 49 + ["ESQUERDA", "DIREITA"]  # 51 comandos
        posicao_final = trem.mover(comandos)
        self.assertEqual(trem.movimentos_totais, 50)
        self.assertEqual(posicao_final, 49)

    def test_mistura_de_comandos_complexos(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 10 + ["ESQUERDA"] * 10 + ["DIREITA"] * 10 + ["ESQUERDA"] * 10 + ["DIREITA"] * 10
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, 10)

    def test_mover_no_limite_exato(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 50
        posicao_final = trem.mover(comandos)
        self.assertEqual(trem.movimentos_totais, 50)
        self.assertEqual(posicao_final, 50)

if __name__ == '__main__':
    unittest.main()
