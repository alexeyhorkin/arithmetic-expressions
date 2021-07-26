import typing as tp

from .operations import Operation
from .tokenizer import Tokenizer
from .parser import parse_operation


def calc(input_str: str) -> tp.Union[int, float, None]:
    """Wrapper to make calculations"""
    iterator = Tokenizer(input_str).__iter__()
    op = parse_operation(iterator)
    if isinstance(op, Operation):
        return op.execute()
    else:
        return None
