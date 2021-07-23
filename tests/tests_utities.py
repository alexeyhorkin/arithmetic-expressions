import typing as tp
from dataclasses import dataclass

EPS = 1e-3

ERR_NO_CLOSE_BRACKET = "No close bracket found"
ERR_NO_OPEN_BRACKET = "No open bracket found"
ERR_INVALID_CHARACTER = "Invalid character"
ERR_NO_SUMMAND = "No addendum found"
ERR_NO_DIVIDER = "No divider found"
ERR_NO_MULTIPLIER = "No multiplier found"


@dataclass
class CaseTokenizer:
    given: str
    expected: tp.Sequence[type]


@dataclass
class CaseCalc:
    given: str
    expected: tp.Union[int, float]


@dataclass
class CaseInputValidation:
    given: str
    expected_error_message: tp.Optional[str]
