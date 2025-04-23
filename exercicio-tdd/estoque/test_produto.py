"""
Testes da classe Produto.
"""
import unittest
from datetime import datetime, timedelta
from produto import Produto


class TestProduto(unittest.TestCase):
    """Testa a classe Produto."""

    def setUp(self):
        """Configura o ambiente de teste."""
        self.produto = Produto(
            codigo="001",
            nome="Arroz",
            preco=5.0,
            quantidade=20,
            data_validade=datetime.now() + timedelta(days=10),
            estoque_minimo=10
        )

    def test_inicializacao(self):
        """Verifica se o produto é inicializado corretamente."""
        self.assertEqual(self.produto.codigo, "001")
        self.assertEqual(self.produto.nome, "Arroz")
        self.assertEqual(self.produto.preco, 5.0)
        self.assertEqual(self.produto.quantidade, 20)

    def test_adicionar_estoque(self):
        """Verifica se o estoque é adicionado corretamente."""
        self.produto.adicionar_estoque(5)
        self.assertEqual(self.produto.quantidade, 25)

        with self.assertRaises(ValueError):
            self.produto.adicionar_estoque(-10)

    def test_remover_estoque(self):
        """Verifica se o estoque é removido corretamente."""
        resultado = self.produto.remover_estoque(5)
        self.assertTrue(resultado)
        self.assertEqual(self.produto.quantidade, 15)

        resultado = self.produto.remover_estoque(100)
        self.assertFalse(resultado)

        with self.assertRaises(ValueError):
            self.produto.remover_estoque(-1)

    def test_verificar_estoque_baixo(self):
        """Verifica se a detecção de estoque baixo funciona corretamente."""
        self
