import pytest
from calculator.parser import parse_operation
from calculator.tokenizer import Tokenizer

EPS = 1e-3

CASES = [("1", 1),
         ("1 + 2", 3),
         ("1 - 2", -1),
         ("2 * 3", 6),
         ("1 + 2 + 3 + 4 + 5", 15),
         ("2 * 3 * 4", 24),
         ("(1)", 1),
         ("(1 + 0)", 1),
         ("(1 + 1)", 2),
         ("(1 - 2)", -1),
         ("1 + 2 * 3", 7),
         ("(1 + 2) * 3", 9),
         ("-1", -1),
         ("-1 -2", -3),
         ("-(1 - 2)", 1),
         ("-(1 -(2 * 3))", 5),
         ("(((3)))", 3),
         ("(((-3)))", -3),
         ("2 / 3 + 1", 1.666)]


@pytest.mark.parametrize("input, expected_res", CASES)
def test_easy_caces(input, expected_res) -> None:
    iterator = Tokenizer(input).__iter__()
    op = parse_operation(iterator)
    assert op.execute() == pytest.approx(expected_res, EPS)
