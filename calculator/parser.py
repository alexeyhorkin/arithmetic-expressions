import typing as tp

from . import tokens as tks
from . import operations as ops
from .tokenizer import SpecificIterator
from tests.tests_utities import (
    # ERR_NO_OPEN_BRACKET,
    ERR_NO_CLOSE_BRACKET,
    ERR_NO_MULTIPLIER,
    ERR_INVALID_CHARACTER,
    ERR_NO_DIVIDER,
    ERR_NO_SUMMAND_PLUS,
    ERR_NO_SUMMAND_MINUS
)


def parse_operation(tokenier_iterator: SpecificIterator) -> \
                    tp.Optional[ops.Operation]:
    left = parse_summand(tokenier_iterator)
    if left is None:
        return left
    while True:
        try:
            token = next(tokenier_iterator)
            if isinstance(token, tks.SumToken):
                right = parse_summand(tokenier_iterator)
                if right is None:
                    raise TypeError(ERR_NO_SUMMAND_PLUS)
                left = ops.BinaryAddOp(left, right)
            elif isinstance(token, tks.SubToken):
                right = parse_summand(tokenier_iterator)
                if right is None:
                    raise TypeError(ERR_NO_SUMMAND_MINUS)
                left = ops.BinarySubOp(left, right)
            else:
                break
        except StopIteration:
            break

    return left


def parse_summand(tokenier_iterator: SpecificIterator) -> \
                  tp.Optional[ops.Operation]:
    left = parse_factor(tokenier_iterator)
    if not left:
        return left
    while True:
        try:
            token = tokenier_iterator.watch_next()
            if isinstance(token, tks.MulToken):
                next(tokenier_iterator)
                right = parse_factor(tokenier_iterator)
                if right is None:
                    raise TypeError(ERR_NO_MULTIPLIER)
                left = ops.BinaryMulOp(left, right)
            elif isinstance(token, tks.DivToken):
                next(tokenier_iterator)
                right = parse_factor(tokenier_iterator)
                if right is None:
                    raise TypeError(ERR_NO_DIVIDER)
                left = ops.BinaryDivOp(left, right)
            else:
                break
        except StopIteration:
            break

    return left


def parse_factor(tokenier_iterator: SpecificIterator) -> \
                 tp.Optional[ops.Operation]:
    try:
        token = tokenier_iterator.watch_next()
        if isinstance(token, tks.SubToken):
            next(tokenier_iterator)
            right = parse_numerical(tokenier_iterator)
            if right is None:
                raise TypeError(ERR_INVALID_CHARACTER)
            return ops.UnarySub(right)
        elif isinstance(token, tks.ConstantToken) \
                or isinstance(token, tks.OpenBracketToken):
            return parse_numerical(tokenier_iterator)
        elif isinstance(token, tks.MulToken):
            raise TypeError(ERR_NO_MULTIPLIER)
        elif isinstance(token, tks.DivToken):
            raise TypeError(ERR_NO_DIVIDER)
        elif token is None:
            return token
        else:
            raise TypeError(ERR_INVALID_CHARACTER)
    except StopIteration:
        # pass  # [TODO]: add error raise
        raise RuntimeError


def parse_numerical(tokenier_iterator: SpecificIterator) -> \
                    tp.Optional[ops.Operation]:
    token = tokenier_iterator.watch_next()
    if isinstance(token, tks.OpenBracketToken):
        next(tokenier_iterator)
        token_res = parse_operation(tokenier_iterator)
        # check Closed Bracked
        if not isinstance(
                tokenier_iterator.current_token, tks.CloseBracketToken):
            raise TypeError(ERR_NO_CLOSE_BRACKET)
    elif isinstance(token, tks.ConstantToken):
        token_res = ops.ConstantOp(token.val)
        next(tokenier_iterator)
    else:
        raise StopIteration
    return token_res
