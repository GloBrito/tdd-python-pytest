from __future__ import annotations
import re
from dataclasses import dataclass, field
from typing import List


@dataclass
class Email:
    name: str  # endereço de e-mail


@dataclass
class Person:
    id: int
    name: str
    age: int
    emails: List[Email] = field(default_factory=list)


class PersonDAO:
    def save(self, p: Person) -> None:
        """Persiste um objeto Person (stub — fora do escopo do TDD aqui)."""
        raise NotImplementedError("save() não implementado")

    def isValidToInclude(self, p: Person) -> List[str]:
        """
        Valida um objeto Person antes da persistência.

        Regras de validação:
        1. O nome deve ser composto por ao menos 2 partes e apenas letras.
        2. A idade deve estar no intervalo [1, 200].
        3. O Person deve ter pelo menos um Email associado.
        4. O nome de cada Email deve estar no formato ____@____.____,
           sendo que cada parte deve ter ao menos um caractere.

        Retorna:
            Lista de mensagens de erro. Lista vazia indica objeto válido.
        """
        erros: List[str] = []

        # Regra 1 — validação do nome
        partes_nome = p.name.strip().split()
        if len(partes_nome) < 2:
            erros.append("O nome deve ser composto por ao menos 2 partes.")
        if not all(parte.isalpha() for parte in partes_nome):
            erros.append("O nome deve ser composto apenas por letras.")

        # Regra 2 — validação da idade
        if not (1 <= p.age <= 200):
            erros.append("A idade deve estar no intervalo [1, 200].")

        # Regra 3 — ao menos um e-mail
        if not p.emails:
            erros.append("O Person deve ter pelo menos um Email associado.")

        # Regra 4 — formato do e-mail
        padrao_email = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s.]+$')
        for email in p.emails:
            if not padrao_email.match(email.name):
                erros.append(
                    f"O e-mail '{email.name}' não está no formato válido (____@____.____)."
                )

        return erros
