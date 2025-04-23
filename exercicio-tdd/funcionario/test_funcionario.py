"""
Testes da classe Funcionario.
"""
import unittest
from funcionario import Funcionario


class TestFuncionario(unittest.TestCase):
    """Testes da classe Funcionario."""

    def test_calcular_salario_bruto(self):
        """Testa o cálculo do salário bruto."""
        funcionario = Funcionario(
            nome="João",
            matricula=123,
            salario_hora=50.0,
            horas_trabalhadas=160
        )
        self.assertEqual(funcionario.calcular_salario_bruto(), 8000.0)

    def test_calcular_custo_total(self):
        """Testa o cálculo do custo total."""
        funcionario = Funcionario(
            nome="Maria",
            matricula=456,
            salario_hora=60.0,
            horas_trabalhadas=150,
            custo_empregador=1200.0
        )
        # salário: 60 * 150 = 9000 + 1200 = 10200
        self.assertEqual(funcionario.calcular_custo_total(), 10200.0)

    def test_calcular_comissao(self):
        """Testa o cálculo da comissão."""
        funcionario = Funcionario(
            nome="Carlos",
            matricula=789,
            tem_comissao=True,
            valor_comissao=200.0,
            contratos_fechados=3
        )
        self.assertEqual(funcionario.calcular_comissao(), 600.0)

        sem_comissao = Funcionario(
            nome="Ana",
            matricula=321,
            tem_comissao=False,
            valor_comissao=100.0,
            contratos_fechados=5
        )
        self.assertEqual(sem_comissao.calcular_comissao(), 0.0)


if __name__ == "__main__":
    unittest.main()
