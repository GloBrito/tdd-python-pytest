import pytest
from triangulo import classificar_triangulo, TipoTriangulo, TrianguloInvalidoErro


class TestTriangulosValidos:
    # CT-01: Triângulo escaleno válido
    def test_triangulo_escaleno_valido(self):
        resultado = classificar_triangulo(3, 4, 5)
        assert resultado == TipoTriangulo.ESCALENO

    # CT-02: Triângulo isósceles válido
    def test_triangulo_isosceles_valido(self):
        resultado = classificar_triangulo(5, 5, 3)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT-03: Triângulo equilátero válido
    def test_triangulo_equilatero_valido(self):
        resultado = classificar_triangulo(6, 6, 6)
        assert resultado == TipoTriangulo.EQUILATERO

    # CT-04: Permutação isósceles com lado_a == lado_b
    def test_isosceles_permutacao_a_igual_b(self):
        resultado = classificar_triangulo(5, 5, 3)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT-05: Permutação isósceles com lado_b == lado_c
    def test_isosceles_permutacao_b_igual_c(self):
        resultado = classificar_triangulo(3, 5, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT-06: Permutação isósceles com lado_a == lado_c
    def test_isosceles_permutacao_a_igual_c(self):
        resultado = classificar_triangulo(5, 3, 5)
        assert resultado == TipoTriangulo.ISOSCELES


class TestValoresInvalidosDosLados:
    # CT-07: Lado A igual a zero
    def test_lado_a_igual_a_zero(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(0, 4, 5)

    # CT-08: Lado B igual a zero
    def test_lado_b_igual_a_zero(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(3, 0, 5)

    # CT-09: Lado C igual a zero
    def test_lado_c_igual_a_zero(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(3, 4, 0)

    # CT-10: Lado A negativo
    def test_lado_a_negativo(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(-1, 4, 5)

    # CT-11: Lado B negativo
    def test_lado_b_negativo(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(3, -1, 5)

    # CT-12: Lado C negativo
    def test_lado_c_negativo(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(3, 4, -1)

    # CT-13: Todos os lados iguais a zero
    def test_todos_os_lados_iguais_a_zero(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(0, 0, 0)


class TestDesigualdadeTriangular:
    # CT-14: Soma de A+B igual ao lado C (triângulo degenerado)
    def test_soma_ab_igual_a_c(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(1, 2, 3)  # 1+2 == 3

    # CT-15: Permutação — soma A+C igual ao lado B
    def test_soma_ac_igual_a_b(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(1, 3, 2)  # 1+2 == 3

    # CT-16: Permutação — soma B+C igual ao lado A
    def test_soma_bc_igual_a_a(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(3, 1, 2)  # 1+2 == 3

    # CT-17: Soma de A+B menor que o lado C
    def test_soma_ab_menor_que_c(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(1, 2, 10)

    # CT-18: Permutação — soma A+C menor que o lado B
    def test_soma_ac_menor_que_b(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(1, 10, 2)

    # CT-19: Permutação — soma B+C menor que o lado A
    def test_soma_bc_menor_que_a(self):
        with pytest.raises(TrianguloInvalidoErro):
            classificar_triangulo(10, 1, 2)
