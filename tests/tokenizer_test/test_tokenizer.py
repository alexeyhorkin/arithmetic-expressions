import pytest
import calculator.tokens as tks
from calculator.tokenizer import Tokenizer
from ..tests_utities import CaseTokenizer


CASES = [CaseTokenizer("1", [tks.ConstantToken]),
         CaseTokenizer("1 + 2", [tks.ConstantToken,
                                 tks.SumToken,
                                 tks.ConstantToken]),
         CaseTokenizer("(2*3)", [tks.OpenBracketToken,
                                 tks.ConstantToken,
                                 tks.MulToken,
                                 tks.ConstantToken,
                                 tks.CloseBracketToken])]


@pytest.mark.parametrize("case", CASES)
def test_types_of_tokens(case: CaseTokenizer) -> None:
    for idx, tok in enumerate(Tokenizer(case.given)):
        assert isinstance(tok, case.expected[idx])
    assert idx + 1 == len(case.expected)
