from calculator.operations import Operation
import pytest
from calculator.parser import parse_operation
from calculator.tokenizer import Tokenizer
from ..tests_utities import CaseCalc, EPS

HARD_CASES = [CaseCalc("7*(-1+2*(3*2*4+15*431)*1+((2*3)*11+314))", 93499),
              CaseCalc("19 + 2 / 3 + (1 + 1 + 394) / 7 / 2", 47.94),
              CaseCalc("1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10", 3628800)]


@pytest.mark.parametrize("case", HARD_CASES)
def test_easy_caces_calc(case: CaseCalc) -> None:
    iterator = Tokenizer(case.given).__iter__()
    op = parse_operation(iterator)
    assert isinstance(op, Operation)
    assert op.execute() == pytest.approx(case.expected, EPS)
