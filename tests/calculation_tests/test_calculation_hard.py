import pytest
from calculator.parser import parse_operation
from calculator.tokenizer import Tokenizer

EPS = 1e-3

HARD_CASES = [("7*(-1+2*(3*2*4+15*431)*1+((2*3)*11+314))", 93499),
              ("19 + 2 / 3 + (1 + 1 + 394) / 7 / 2", 47.94),
              ("1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10", 3628800)]


@pytest.mark.parametrize("input, expected_res", HARD_CASES)
def test_hard_caces(input, expected_res) -> None:
    iterator = Tokenizer(input).__iter__()
    op = parse_operation(iterator)
    assert op.execute() == pytest.approx(expected_res, EPS)
