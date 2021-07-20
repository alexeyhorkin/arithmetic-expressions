import typing as tp
from abc import abstractmethod
from typing_extensions import Protocol

from . import tokens as tks


class SpecificIterator(Protocol, tp.Iterator[tks.Token]):

    current_token: tp.Optional[tks.Token] = None
    current_pos: int = 0
    input_str: str = ""
    is_modify: bool = True

    @abstractmethod
    def watch_next(self) -> tp.Optional[tks.Token]:
        raise NotImplementedError


class Tokenizer:

    def __init__(self, input_str: str) -> None:
        self.input = input_str.replace(" ", "")  # remove all whitespaces

    class TokenizerIterator(SpecificIterator):
        def __init__(self, input: str, is_modify: bool = True) -> None:
            self.current_token: tp.Optional[tks.Token] = None
            self.current_pos: int = 0
            self.input_str: str = input
            self.is_modify: bool = is_modify

        def get_cur_symbol(self) -> str:
            return self.input_str[self.current_pos]

        def watch_next(self) -> tp.Optional[tks.Token]:
            self.is_modify = False
            if not self._is_end():
                next_token = next(self)
                self.is_modify = True
                return next_token
            return None

        def __next__(self) -> tks.Token:
            token: tks.Token = tks.NoneToken()
            numerical_placeholder = ""
            if self._is_end():
                raise StopIteration
            current_symbol = self.get_cur_symbol()
            if current_symbol == "+":
                token = tks.SumToken()
            elif current_symbol == "-":
                token = tks.SubToken()
            elif current_symbol == "*":
                token = tks.MulToken()
            elif current_symbol == "/":
                token = tks.DivToken()
            elif current_symbol == "(":
                token = tks.OpenBracketToken()
            elif current_symbol == ")":
                token = tks.CloseBracketToken()
            elif current_symbol.isdigit():
                total_lehgth: int = 0
                is_point = False
                while current_symbol.isdigit() or current_symbol == ".":
                    if current_symbol == ".":
                        if is_point:
                            raise RuntimeError(
                                "Too many points for one float numder")
                        is_point = True

                    numerical_placeholder += current_symbol
                    self.current_pos += 1
                    total_lehgth += 1
                    if self._is_end():
                        break
                    current_symbol = self.get_cur_symbol()

                value = int(numerical_placeholder) if not is_point else \
                    float(numerical_placeholder)
                token = tks.ConstantToken(value)
                if self.is_modify:
                    self.current_pos -= 1
                else:
                    self.current_pos -= total_lehgth

            else:
                raise NotImplementedError(
                    f"This character: {current_symbol}" +
                    "not supported, see supported: {tks.SUPPORTED_TOKENS}")

            if self.is_modify:
                self.current_pos += 1
            self.current_token = token
            return token

        def _is_end(self) -> bool:
            return self.current_pos == len(self.input_str)

    def __iter__(self) -> SpecificIterator:
        return self.TokenizerIterator(input=self.input)
