from enum import Enum


class TipoTriangulo(Enum):
    EQUILATERO = "equilátero"
    ISOSCELES = "isósceles"
    ESCALENO = "escaleno"


class TrianguloInvalidoErro(Exception):
    pass


def classificar_triangulo(a: int, b: int, c: int) -> TipoTriangulo:
    """
    Classifica um triângulo dados três lados inteiros.

    Levanta:
        TrianguloInvalidoErro: se algum lado for <= 0 ou se os lados não
        formarem um triângulo válido (desigualdade triangular).

    Retorna:
        TipoTriangulo: EQUILATERO, ISOSCELES ou ESCALENO.
    """
    if a <= 0 or b <= 0 or c <= 0:
        raise TrianguloInvalidoErro(
            "Todos os lados devem ser maiores que zero."
        )

    if a + b <= c or a + c <= b or b + c <= a:
        raise TrianguloInvalidoErro(
            "A soma de dois lados deve ser maior que o terceiro lado."
        )

    if a == b == c:
        return TipoTriangulo.EQUILATERO
    if a == b or b == c or a == c:
        return TipoTriangulo.ISOSCELES
    return TipoTriangulo.ESCALENO
