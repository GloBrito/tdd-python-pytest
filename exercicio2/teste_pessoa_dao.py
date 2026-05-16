import pytest
from pessoa_dao import Person, Email, PersonDAO


@pytest.fixture
def dao() -> PersonDAO:
    return PersonDAO()


def criar_pessoa(**kwargs) -> Person:
    """Auxiliar: retorna um Person totalmente válido; sobrescreva campos via kwargs."""
    padrao = dict(
        id=1,
        name="João Silva",
        age=30,
        emails=[Email(name="joao@email.com")],
    )
    padrao.update(kwargs)
    return Person(**padrao)


class TestPessoaValida:
    def test_pessoa_valida_nao_retorna_erros(self, dao):
        pessoa = criar_pessoa()
        assert dao.isValidToInclude(pessoa) == []

    def test_pessoa_valida_com_multiplos_emails(self, dao):
        pessoa = criar_pessoa(emails=[Email("a@b.com"), Email("c@d.org")])
        assert dao.isValidToInclude(pessoa) == []


class TestValidacaoNome:
    def test_nome_com_apenas_uma_parte_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(name="João"))
        assert any("2 partes" in e for e in erros)

    def test_nome_com_numeros_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(name="João Silva2"))
        assert any("letras" in e for e in erros)

    def test_nome_com_caracteres_especiais_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(name="João @Silva"))
        assert any("letras" in e for e in erros)

    def test_nome_vazio_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(name=""))
        assert any("2 partes" in e for e in erros)

    def test_nome_com_duas_partes_e_valido(self, dao):
        assert dao.isValidToInclude(criar_pessoa(name="Ana Paula")) == []

    def test_nome_com_tres_partes_e_valido(self, dao):
        assert dao.isValidToInclude(criar_pessoa(name="Ana Paula Santos")) == []


class TestValidacaoIdade:
    def test_idade_zero_e_invalida(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(age=0))
        assert any("intervalo" in e for e in erros)

    def test_idade_negativa_e_invalida(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(age=-1))
        assert any("intervalo" in e for e in erros)

    def test_idade_201_e_invalida(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(age=201))
        assert any("intervalo" in e for e in erros)

    # testes de fronteira
    def test_idade_1_e_valida_fronteira_inferior(self, dao):
        assert dao.isValidToInclude(criar_pessoa(age=1)) == []

    def test_idade_200_e_valida_fronteira_superior(self, dao):
        assert dao.isValidToInclude(criar_pessoa(age=200)) == []

    def test_idade_100_e_valida(self, dao):
        assert dao.isValidToInclude(criar_pessoa(age=100)) == []


class TestPresencaEmail:
    def test_pessoa_sem_emails_e_invalida(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(emails=[]))
        assert any("Email" in e for e in erros)


class TestFormatoEmail:
    def test_email_sem_arroba_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(emails=[Email("emailinvalido.com")]))
        assert any("formato" in e for e in erros)

    def test_email_sem_ponto_no_dominio_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(emails=[Email("usuario@dominio")]))
        assert any("formato" in e for e in erros)

    def test_email_sem_parte_local_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(emails=[Email("@dominio.com")]))
        assert any("formato" in e for e in erros)

    def test_email_com_dominio_vazio_e_invalido(self, dao):
        erros = dao.isValidToInclude(criar_pessoa(emails=[Email("usuario@.com")]))
        assert any("formato" in e for e in erros)

    def test_email_com_extensao_vazia_e_invalido(self, dao):
        # nada após o ponto final
        erros = dao.isValidToInclude(criar_pessoa(emails=[Email("usuario@dominio.")]))
        assert any("formato" in e for e in erros)

    def test_formato_de_email_valido(self, dao):
        assert dao.isValidToInclude(criar_pessoa(emails=[Email("usuario@dominio.com")])) == []

    def test_email_com_subdominio_e_valido(self, dao):
        assert dao.isValidToInclude(criar_pessoa(emails=[Email("usuario@mail.dominio.org")])) == []


class TestMultiplosErros:
    def test_retorna_multiplos_erros_simultaneamente(self, dao):
        pessoa = Person(id=2, name="João", age=0, emails=[])
        erros = dao.isValidToInclude(pessoa)
        assert len(erros) >= 3  # erros de nome, idade e e-mail
