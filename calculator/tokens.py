import typing as tp
from abc import ABC, abstractclassmethod


class Token(ABC):
    @abstractclassmethod
    def __str__(self) -> str:
        pass


class NoneToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "NoneToken"


class SumToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return " + "


class SubToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return " - "


class MulToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return " * "


class DivToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return " / "


class OpenBracketToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "("


class CloseBracketToken(Token):
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return ")"


class ConstantToken(Token):
    def __init__(self, value: tp.Union[int, float]) -> None:
        self.val = value

    def __str__(self) -> str:
        return str(self.val)


SUPPORTED_TOKENS = [SumToken, SubToken, MulToken,
                    DivToken, OpenBracketToken,
                    ConstantToken, CloseBracketToken]
