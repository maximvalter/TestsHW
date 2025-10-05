import pytest

from task3 import solve

@pytest.mark.parametrize(
    "phrases, result",
    [
        (["ароза упала на лапу азора"], ["ароза упала на лапу азора"]),
        (["дом ком"], []),
        (["топот", "кот"], ["топот"]),
        (["нажал кабан на баклажан"], ["нажал кабан на баклажан"]),
        (["ТОПОТ", "ШаЛаШ", "дом", "кот"], ["топот", "шалаш"]),
        ([], []),
        (["a" * 1000], ["a" * 1000])
    ]
)
def test_solve(phrases, result):
    assert solve(phrases) == result


