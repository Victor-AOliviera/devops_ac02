import pytest
from com.kuma.operacoes import Operacoes

def test_soma():
    operacoes = Operacoes()
    assert operacoes.soma([1,5])==6,'should be 6'