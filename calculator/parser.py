from . import tokens as tks
from . import operations as ops
from .tokenizer import SpecificIterator


def parse_operation(tokenier_iterator: SpecificIterator) -> \
                    ops.Operation:
    left = parse_summand(tokenier_iterator)
    while True:
        try:
            token = next(tokenier_iterator)
            if isinstance(token, tks.SumToken):
                right = parse_summand(tokenier_iterator)
                left = ops.BinaryAddOp(left, right)
            elif isinstance(token, tks.SubToken):
                right = parse_summand(tokenier_iterator)
                left = ops.BinarySubOp(left, right)
            else:
                break
        except StopIteration:
            break

    return left


def parse_summand(tokenier_iterator: SpecificIterator) -> \
                  ops.Operation:
    left = parse_factor(tokenier_iterator)
    while True:
        try:
            token = tokenier_iterator.watch_next()
            if isinstance(token, tks.MulToken):
                next(tokenier_iterator)
                right = parse_factor(tokenier_iterator)
                left = ops.BinaryMulOp(left, right)
            elif isinstance(token, tks.DivToken):
                next(tokenier_iterator)
                right = parse_factor(tokenier_iterator)
                left = ops.BinaryDivOp(left, right)
            else:
                break
        except StopIteration:
            break

    return left


def parse_factor(tokenier_iterator: SpecificIterator) -> \
                 ops.Operation:
    try:
        token = tokenier_iterator.watch_next()
        if isinstance(token, tks.SubToken):
            next(tokenier_iterator)
            right = parse_numerical(tokenier_iterator)
            return ops.UnarySub(right)
        else:
            return parse_numerical(tokenier_iterator)
    except StopIteration:
        # pass  # [TODO]: add error raise
        raise RuntimeError


def parse_numerical(tokenier_iterator: SpecificIterator) -> \
                    ops.Operation:
    token = tokenier_iterator.watch_next()
    if isinstance(token, tks.OpenBracketToken):
        next(tokenier_iterator)
        token_res = parse_operation(tokenier_iterator)
        # check Closed Bracked
        if not isinstance(
                tokenier_iterator.current_token, tks.CloseBracketToken):
            raise RuntimeError("Expression doesn't correct due to brackers")
    elif isinstance(token, tks.ConstantToken):
        token_res = ops.ConstantOp(token.val)
        next(tokenier_iterator)
    else:
        raise StopIteration
    return token_res
