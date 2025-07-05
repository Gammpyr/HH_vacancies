import pytest

from src.utils import is_string, is_empty

def test_is_string_err():
    with pytest.raises(TypeError):
        is_string(111, "Число не")

def test_is_empty_err():
    with pytest.raises(ValueError):
        is_empty('', "")