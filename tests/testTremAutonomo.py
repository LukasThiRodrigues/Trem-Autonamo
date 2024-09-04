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
        comandos = ["DIREITA", "CIMA"]
        with self.assertRaises(ComandoInvalidoError):
            trem.mover(comandos)

    def test_comando_formato_incorreto(self):
        trem = TremAutonomo()
        comandos = ["direita", "ESQUERDA"]  # 'direita' em minúsculas
        with self.assertRaises(ComandoInvalidoError):
            trem.mover(comandos)

    def test_excede_movimentos_totais(self):
        trem = TremAutonomo()
        comandos = ["DIREITA", "ESQUERDA"] * 51 # 51 movimentos
        with self.assertRaises(MovimentoExcedeLimiteError):
            trem.mover(comandos)

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
        comandos = ["DIREITA"] * 20 + ["ESQUERDA"] * 20 + ["DIREITA"] * 10  # Total: 50 comandos
        posicao_final = trem.mover(comandos)
        self.assertEqual(trem.movimentos_totais, 50)
        self.assertEqual(posicao_final, 10)

    def test_mistura_de_comandos_complexos(self):
        trem = TremAutonomo()
        comandos = ["DIREITA"] * 10 + ["ESQUERDA"] * 10 + ["DIREITA"] * 10 + ["ESQUERDA"] * 10 + ["DIREITA"] * 10
        posicao_final = trem.mover(comandos)
        self.assertEqual(posicao_final, 10)

if __name__ == '__main__':
    unittest.main()
