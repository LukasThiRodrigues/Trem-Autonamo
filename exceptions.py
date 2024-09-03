class ComandoInvalidoError(Exception):
    """Exceção para comandos inválidos."""
    pass

class ListaComandosVaziaError(Exception):
    """Exceção para lista de comandos vazia."""
    pass

class MovimentoExcedeLimiteError(Exception):
    """Exceção para exceder o limite de movimentos totais."""
    pass

class MovimentosConsecutivosError(Exception):
    """Exceção para exceder o limite de movimentos consecutivos na mesma direção."""
    pass
