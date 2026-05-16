from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


@dataclass
class Funcionario:
    nome: str
    email: str
    salario_base: float
    cargo: Cargo


class CalculadoraSalario:
    """
    Calcula o salário líquido de um Funcionario com base no cargo e salário-base.

    Regras de desconto:
    - DESENVOLVEDOR: 20% se salário >= 3.000,00, senão 10%
    - DBA:           25% se salário >= 2.000,00, senão 15%
    - TESTADOR:      25% se salário >= 2.000,00, senão 15%
    - GERENTE:       30% se salário >= 5.000,00, senão 20%
    """

    _REGRAS: dict = {
        Cargo.DESENVOLVEDOR: (3_000.00, 0.20, 0.10),
        Cargo.DBA:           (2_000.00, 0.25, 0.15),
        Cargo.TESTADOR:      (2_000.00, 0.25, 0.15),
        Cargo.GERENTE:       (5_000.00, 0.30, 0.20),
    }

    def calcular_salario_liquido(self, funcionario: Funcionario) -> float:
        limite, desconto_alto, desconto_baixo = self._REGRAS[funcionario.cargo]
        desconto = desconto_alto if funcionario.salario_base >= limite else desconto_baixo
        return round(funcionario.salario_base * (1 - desconto), 2)
