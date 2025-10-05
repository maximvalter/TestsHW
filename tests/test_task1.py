import pytest
from task1 import solution

def test_infinite_solutions():
    assert solution(0, 0, 0) == ["Бесконечно много решений"]

@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (0, 0, 100, []), # нет решений
        (1, 2, 3, []), # d < 0
        (1, -13, 12, [12.0, 1.0]), # 2 корня
        (1, 2, 1, [-1.0]) # 1 корень
    ]
)
def test_solution(a, b, c, expected):
    d = solution(a, b, c)
    assert d == expected