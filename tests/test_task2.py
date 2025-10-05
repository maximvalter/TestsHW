import pytest
from task2 import vote

@pytest.mark.parametrize(
    'votes, result',
    [
        [[1, 2, 3, 1, 2, 3, 1, 2, 3, 1], 1],
        ((1, 3, 5, 6, 7, 7, 1, 3, 4, 7), 7),
        ("1273182374141414124057161", 1),
        (777, 7)
    ]
)
def test(votes, result):
    assert vote(votes) == result