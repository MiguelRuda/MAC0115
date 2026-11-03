def fatorial(n: int) -> int:
    """Calcula n! para um inteiro n >= 0."""
    if n < 0:
        raise ValueError("n deve ser não negativo")

    resultado = 1
    for fator in range(2, n + 1):
        resultado *= fator
    return resultado


if __name__ == "__main__":
    for n in range(6):
        print(f"{n}! = {fatorial(n)}")
