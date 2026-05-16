import pytest
from calculadora_salario import Funcionario, Cargo, CalculadoraSalario


@pytest.fixture
def calculadora() -> CalculadoraSalario:
    return CalculadoraSalario()


def criar_funcionario(cargo: Cargo, salario: float) -> Funcionario:
    return Funcionario(
        nome="Usuário Teste",
        email="teste@empresa.com",
        salario_base=salario,
        cargo=cargo,
    )


class TestDesenvolvedor:
    """DESENVOLVEDOR: desconto de 20% se salário >= 3.000, senão 10%"""

    def test_salario_abaixo_do_limite_aplica_desconto_de_10_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DESENVOLVEDOR, 2_000.00)
        assert calculadora.calcular_salario_liquido(func) == 1_800.00

    def test_salario_exatamente_no_limite_aplica_desconto_de_20_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DESENVOLVEDOR, 3_000.00)
        assert calculadora.calcular_salario_liquido(func) == 2_400.00

    def test_salario_acima_do_limite_aplica_desconto_de_20_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DESENVOLVEDOR, 5_000.00)
        assert calculadora.calcular_salario_liquido(func) == 4_000.00

    def test_salario_imediatamente_abaixo_do_limite(self, calculadora):
        func = criar_funcionario(Cargo.DESENVOLVEDOR, 2_999.99)
        assert calculadora.calcular_salario_liquido(func) == round(2_999.99 * 0.90, 2)


class TestDBA:
    """DBA: desconto de 25% se salário >= 2.000, senão 15%"""

    def test_salario_abaixo_do_limite_aplica_desconto_de_15_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DBA, 1_500.00)
        assert calculadora.calcular_salario_liquido(func) == 1_275.00

    def test_salario_exatamente_no_limite_aplica_desconto_de_25_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DBA, 2_000.00)
        assert calculadora.calcular_salario_liquido(func) == 1_500.00

    def test_salario_acima_do_limite_aplica_desconto_de_25_porcento(self, calculadora):
        func = criar_funcionario(Cargo.DBA, 4_000.00)
        assert calculadora.calcular_salario_liquido(func) == 3_000.00

    def test_salario_imediatamente_abaixo_do_limite(self, calculadora):
        func = criar_funcionario(Cargo.DBA, 1_999.99)
        assert calculadora.calcular_salario_liquido(func) == round(1_999.99 * 0.85, 2)


class TestTestador:
    """TESTADOR: desconto de 25% se salário >= 2.000, senão 15%"""

    def test_salario_abaixo_do_limite_aplica_desconto_de_15_porcento(self, calculadora):
        func = criar_funcionario(Cargo.TESTADOR, 1_000.00)
        assert calculadora.calcular_salario_liquido(func) == 850.00

    def test_salario_exatamente_no_limite_aplica_desconto_de_25_porcento(self, calculadora):
        func = criar_funcionario(Cargo.TESTADOR, 2_000.00)
        assert calculadora.calcular_salario_liquido(func) == 1_500.00

    def test_salario_acima_do_limite_aplica_desconto_de_25_porcento(self, calculadora):
        func = criar_funcionario(Cargo.TESTADOR, 3_000.00)
        assert calculadora.calcular_salario_liquido(func) == 2_250.00

    def test_salario_imediatamente_abaixo_do_limite(self, calculadora):
        func = criar_funcionario(Cargo.TESTADOR, 1_999.99)
        assert calculadora.calcular_salario_liquido(func) == round(1_999.99 * 0.85, 2)


class TestGerente:
    """GERENTE: desconto de 30% se salário >= 5.000, senão 20%"""

    def test_salario_abaixo_do_limite_aplica_desconto_de_20_porcento(self, calculadora):
        func = criar_funcionario(Cargo.GERENTE, 3_000.00)
        assert calculadora.calcular_salario_liquido(func) == 2_400.00

    def test_salario_exatamente_no_limite_aplica_desconto_de_30_porcento(self, calculadora):
        func = criar_funcionario(Cargo.GERENTE, 5_000.00)
        assert calculadora.calcular_salario_liquido(func) == 3_500.00

    def test_salario_acima_do_limite_aplica_desconto_de_30_porcento(self, calculadora):
        func = criar_funcionario(Cargo.GERENTE, 8_000.00)
        assert calculadora.calcular_salario_liquido(func) == 5_600.00

    def test_salario_imediatamente_abaixo_do_limite(self, calculadora):
        func = criar_funcionario(Cargo.GERENTE, 4_999.99)
        assert calculadora.calcular_salario_liquido(func) == round(4_999.99 * 0.80, 2)


class TestAtributosFuncionario:
    def test_funcionario_armazena_nome_e_email(self, calculadora):
        func = Funcionario(
            nome="Maria Oliveira",
            email="maria@empresa.com",
            salario_base=4_000.00,
            cargo=Cargo.GERENTE,
        )
        assert func.nome == "Maria Oliveira"
        assert func.email == "maria@empresa.com"

    def test_salario_liquido_e_do_tipo_float(self, calculadora):
        func = criar_funcionario(Cargo.DESENVOLVEDOR, 3_000.00)
        resultado = calculadora.calcular_salario_liquido(func)
        assert isinstance(resultado, float)
