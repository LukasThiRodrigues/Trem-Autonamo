from tremAutonomo import TremAutonomo
from exceptions import (
    ComandoInvalidoError,
    ListaComandosVaziaError,
    MovimentoExcedeLimiteError,
    MovimentosConsecutivosError
)

def main():
    comandos = []
    print("Digite os comandos para o trem (DIREITA ou ESQUERDA). Digite 'FIM' para encerrar.")
    while True:
        comando = input("Comando: ").strip().upper()
        if comando == 'FIM':
            break
        comandos.append(comando)

    trem = TremAutonomo()

    try:
        posicao_final = trem.mover(comandos)
        print(f"Posição Final do Trem: {posicao_final}")
    except ListaComandosVaziaError as e:
        print(e)
    except ComandoInvalidoError as e:
        print(e)
    except MovimentosConsecutivosError as e:
        print(e)
    except MovimentoExcedeLimiteError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
