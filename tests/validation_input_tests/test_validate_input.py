import pytest
from calculator.parser import parse_operation
from calculator.tokenizer import Tokenizer
from ..tests_utities import (
    CaseInputValidation,
    ERR_NO_OPEN_BRACKET,
    ERR_NO_CLOSE_BRACKET,
    ERR_NO_MULTIPLIER,
    ERR_INVALID_CHARACTER,
    ERR_NO_DIVIDER,
    ERR_NO_SUMMAND
)

CASES = [CaseInputValidation("(1 + 2", ERR_NO_CLOSE_BRACKET),
         CaseInputValidation("(1 + 2)", None)]


@pytest.mark.parametrize("case", CASES)
def test_raises(case: CaseInputValidation) -> None:
    try:
        iterator = Tokenizer(case.given).__iter__()
        _ = parse_operation(iterator)
    except TypeError as err:
        if case.expected_error_message is None:
            assert False, f"Exception {err} raised but input is valid"
        else:
            assert str(err) == case.expected_error_message
    # assert True
