from calculator.operations import Operation
import pytest
from calculator.parser import parse_operation
from calculator.tokenizer import Tokenizer
from ..tests_utities import CaseCalc, EPS


CASES = [CaseCalc("1", 1),
         CaseCalc("1 + 2", 3),
         CaseCalc("1 - 2", -1),
         CaseCalc("2 * 3", 6),
         CaseCalc("1 + 2 + 3 + 4 + 5", 15),
         CaseCalc("2 * 3 * 4", 24),
         CaseCalc("(1)", 1),
         CaseCalc("(1 + 0)", 1),
         CaseCalc("(1 + 1)", 2),
         CaseCalc("(1 - 2)", -1),
         CaseCalc("1 + 2 * 3", 7),
         CaseCalc("(1 + 2) * 3", 9),
         CaseCalc("-1", -1),
         CaseCalc("-1 -2", -3),
         CaseCalc("-(1 - 2)", 1),
         CaseCalc("-(1 -(2 * 3))", 5),
         CaseCalc("(((3)))", 3),
         CaseCalc("(((-3)))", -3),
         CaseCalc("2 / 3 + 1", 1.666)]


@pytest.mark.parametrize("case", CASES)
def test_easy_caces_calc(case: CaseCalc) -> None:
    iterator = Tokenizer(case.given).__iter__()
    op = parse_operation(iterator)
    assert isinstance(op, Operation)
    assert op.execute() == pytest.approx(case.expected, EPS)
