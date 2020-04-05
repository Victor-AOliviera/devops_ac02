from unittest import TestCase
from com.kuma.operacoes import operacoes

class TestOperacoes(TestCase):

    def setup(self):
        self.operacoes = operacoes()

        def test_soma(self):
            self.assetEqual(self.operacoes.soma(1,5), 6 , "should be 6")