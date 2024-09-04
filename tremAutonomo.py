from exceptions import (
    ComandoInvalidoError,
    ListaComandosVaziaError,
    MovimentoExcedeLimiteError,
    MovimentosConsecutivosError
)

class TremAutonomo:
    DIREITA = "DIREITA"
    ESQUERDA = "ESQUERDA"
    DIRECOES_VALIDAS = {DIREITA, ESQUERDA}
    LIMITE_MOVIMENTOS_TOTAIS = 50
    LIMITE_MOVIMENTOS_CONSECUTIVOS = 20

    def __init__(self, posicao_inicial=0):
        self.posicao = posicao_inicial
        self.movimentos_totais = 0
        self.movimentos_consecutivos = 0
        self.ultima_direcao = None

    def mover(self, comandos):
        if not comandos:
            raise ListaComandosVaziaError("Erro: A lista de comandos está vazia.")

        for idx, comando in enumerate(comandos, start=1):
            if comando not in self.DIRECOES_VALIDAS:
                raise ComandoInvalidoError(f"Erro: Comando inválido '{comando}' na posição {idx}.")

            # Verificar movimentos consecutivos
            if comando == self.ultima_direcao:
                self.movimentos_consecutivos += 1
            else:
                self.movimentos_consecutivos = 1
                self.ultima_direcao = comando

            if self.movimentos_consecutivos > self.LIMITE_MOVIMENTOS_CONSECUTIVOS:
                raise MovimentosConsecutivosError(
                    f"Erro: Mais de {self.LIMITE_MOVIMENTOS_CONSECUTIVOS} movimentos consecutivos na direção '{comando}'."
                )

            # Atualizar posição
            if comando == self.DIREITA:
                self.posicao += 1
            elif comando == self.ESQUERDA:
                self.posicao -= 1

            self.movimentos_totais += 1

            if self.movimentos_totais >= self.LIMITE_MOVIMENTOS_TOTAIS:
                raise MovimentoExcedeLimiteError(
                    f"Atingido o limite de {self.LIMITE_MOVIMENTOS_TOTAIS} movimentos. Parando o trem."
                )

        return self.posicao
