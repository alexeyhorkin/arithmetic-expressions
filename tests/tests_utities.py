import typing as tp
from dataclasses import dataclass

EPS = 1e-3


@dataclass
class CaseTokenizer:
    given: str
    expected: tp.Sequence[type]


@dataclass
class CaseCalc:
    given: str
    expected: tp.Union[int, float]
