# Exercícios Práticos de TDD — Python + pytest

Implementação dos três exercícios de TDD utilizando **Python 3.12** e **pytest**.

---

## Estrutura do Projeto

```
tdd_exercicios/
├── pyproject.toml
├── README.md
├── exercicio1/
│   ├── triangulo.py                   # Classificador de triângulo
│   └── teste_triangulo.py             # 19 casos de teste
├── exercicio2/
│   ├── pessoa_dao.py                  # Person, Email, PersonDAO.isValidToInclude()
│   └── teste_pessoa_dao.py            # 23 casos de teste
└── exercicio3/
    ├── calculadora_salario.py         # Funcionario, Cargo, CalculadoraSalario
    └── teste_calculadora_salario.py   # 18 casos de teste
```

---

## Pré-requisitos

- Python 3.10+
- pip

---

## Instalação

```bash
# Clone o repositório
git clone https://github.com/GloBrito/tdd-python-pytest
cd tdd_exercicios

# (Opcional) Crie um ambiente virtual
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows

# Instale as dependências de teste
pip install pytest pytest-cov
```

---

## Execução dos Testes

### Todos os exercícios de uma vez

```bash
pytest
```

### Por exercício individual

```bash
pytest exercicio1/ -v
pytest exercicio2/ -v
pytest exercicio3/ -v
```

---

## Cobertura de Código

### Relatório no terminal

```bash
pytest exercicio1/ --cov=exercicio1 --cov-report=term-missing
pytest exercicio2/ --cov=exercicio2 --cov-report=term-missing
pytest exercicio3/ --cov=exercicio3 --cov-report=term-missing
```

### Relatório HTML (abre no navegador)

```bash
pytest --cov=. --cov-report=html
open htmlcov/index.html       # macOS
xdg-open htmlcov/index.html   # Linux
```

---

## Evidências de Cobertura

### Exercício 1 — Triângulo (19 testes)

```
Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
exercicio1/triangulo.py      17      0   100%
------------------------------------------------------
TOTAL                       17      0   100%
19 passed in 0.10s
```
<img width="1844" height="611" alt="image" src="https://github.com/user-attachments/assets/6af0f0de-1806-4217-ae8e-102b8b09b5cd" />

---

### Exercício 2 — PersonDAO (23 testes)

```
Name                      Stmts   Miss  Cover   Missing
-------------------------------------------------------
exercicio2/pessoa_dao.py      32      1    97%   23
-------------------------------------------------------
TOTAL                        32      1    97%
23 passed in 0.15s
```
<img width="1844" height="706" alt="image" src="https://github.com/user-attachments/assets/697e04fb-8b90-43e4-9ade-90624b65c417" />


---

> A linha 23 corresponde ao stub `save()` que lança `NotImplementedError` —
> propositalmente fora do escopo dos testes, pois pertence à camada de persistência.

### Exercício 3 — Calculadora de Salário (18 testes)

```
Name                               Stmts   Miss  Cover   Missing
----------------------------------------------------------------
exercicio3/calculadora_salario.py      20      0   100%
----------------------------------------------------------------
TOTAL                                 20      0   100%
18 passed in 0.12s
```
<img width="1844" height="612" alt="image" src="https://github.com/user-attachments/assets/adfe5b42-7132-4468-b7b8-ce686ba9d551" />


---

## Técnica TDD Aplicada

Os exercícios foram desenvolvidos seguindo rigorosamente o ciclo **Red-Green-Refactor**:

1. **Red** — Escrever o teste antes da implementação; o teste falha pois o código ainda não existe
2. **Green** — Escrever a implementação mínima necessária para o teste passar
3. **Refactor** — Melhorar o código (legibilidade, estrutura) sem quebrar os testes
4. **Repetir** — Avançar para o próximo caso de teste

Cada classe de teste (`TestTriangulosValidos`, `TestValidacaoNome`, `TestDesenvolvedor`, etc.)
representa uma iteração desse ciclo, partindo dos casos mais simples (caminho feliz)
para os casos de fronteira e situações de exceção.

---

## Descrição dos Exercícios

### Exercício 1 — Classificador de Triângulo

Função `classificar_triangulo(a, b, c)` que retorna `TipoTriangulo.EQUILATERO`,
`ISOSCELES` ou `ESCALENO`. Lança `TrianguloInvalidoErro` para entradas inválidas.

| CT      | Descrição |
|---------|-----------|
| CT-01   | Triângulo escaleno válido |
| CT-02   | Triângulo isósceles válido |
| CT-03   | Triângulo equilátero válido |
| CT-04 a CT-06 | 3 permutações de isósceles (a=b, b=c, a=c) |
| CT-07 a CT-09 | Um lado igual a zero (3 variações) |
| CT-10 a CT-12 | Um lado negativo (3 variações) |
| CT-13   | Todos os lados iguais a zero |
| CT-14 a CT-16 | Soma de 2 lados = terceiro (3 permutações) |
| CT-17 a CT-19 | Soma de 2 lados < terceiro (3 permutações) |

### Exercício 2 — PersonDAO.isValidToInclude()

Valida um objeto `Person` e retorna lista de mensagens de erro,
seguindo exatamente o diagrama UML fornecido.

Regras validadas:
- Nome com ao menos 2 partes compostas apenas por letras
- Idade no intervalo `[1, 200]` (fronteiras inclusas)
- Ao menos um `Email` associado
- Formato de e-mail: `____@____.____` (regex: `^[^\s@]+@[^\s@]+\.[^\s@.]+$`)

### Exercício 3 — Calculadora de Salário

Calcula o salário líquido de um `Funcionario` com base no cargo e salário-base.

| Cargo        | Limite      | Desconto (>=) | Desconto (<) |
|--------------|-------------|---------------|--------------|
| DESENVOLVEDOR| R$ 3.000,00 | 20%           | 10%          |
| DBA          | R$ 2.000,00 | 25%           | 15%          |
| TESTADOR     | R$ 2.000,00 | 25%           | 15%          |
| GERENTE      | R$ 5.000,00 | 30%           | 20%          |

Cada cargo possui testes para: abaixo do limite, exatamente no limite (`>=`) e acima do limite.
# tdd-python-pytest
