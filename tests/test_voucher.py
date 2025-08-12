import pytest
from src.voucher import validar_voucher

@pytest.mark.parametrize("valor, esperado", [
    (49.99, False),
    (50.00, True),
    (50.01, True),
    (275.00, True),
    (499.99, True),
    (500.00, True),
    (500.01, False)
])
def test_validade_voucher_com_valores_limites(valor, esperado):

    assert validar_voucher(valor) == esperado

@pytest.mark.parametrize("valor", [
    0.00,
    -10.00,
    1000.00
])
def test_validade_voucher_com_valores_fora_dos_limites(valor):

    assert validar_voucher(valor) is False