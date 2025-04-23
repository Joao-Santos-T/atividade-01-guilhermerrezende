"""
Sistema de gerenciamento de funcionários.
"""
from dataclasses import dataclass


@dataclass
class Funcionario:
    """Representação de um funcionário com foco em custos trabalhistas e comissões."""

    nome: str
    matricula: int
    salario_hora: float = 100.0
    horas_trabalhadas: float = 0.0
    custo_empregador: float = 1000.0
    tem_comissao: bool = True
    valor_comissao: float = 100.0
    contratos_fechados: int = 0

    def calcular_salario_bruto(self) -> float:
        return self.salario_hora * self.horas_trabalhadas

    def calcular_custo_total(self) -> float:
        return self.calcular_salario_bruto() + self.custo_empregador

    def calcular_comissao(self) -> float:
        if not self.tem_comissao:
            return 0.0
        return self.valor_comissao * self.contratos_fechados
