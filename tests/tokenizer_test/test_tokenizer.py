import pytest
import calculator.tokens as tks
from calculator.tokenizer import Tokenizer

CASES = [("1", [tks.ConstantToken]),
         ("1 + 2", [tks.ConstantToken,
                    tks.SumToken,
                    tks.ConstantToken]),
         ("(2*3)", [tks.OpenBracketToken,
                    tks.ConstantToken,
                    tks.MulToken,
                    tks.ConstantToken,
                    tks.CloseBracketToken])]


@pytest.mark.parametrize("input, expected_tokens", CASES)
def test_types_of_tokens(input, expected_tokens) -> None:
    for idx, tok in enumerate(Tokenizer(input)):
        assert isinstance(tok, expected_tokens[idx])
    assert idx + 1 == len(expected_tokens)
