import typing as tp
from abc import ABC, abstractclassmethod


class Operation(ABC):
    @abstractclassmethod
    def execute(self) -> tp.Union[int, float]:
        pass


class ConstantOp(Operation):
    def __init__(self, value: tp.Union[int, float]) -> None:
        super().__init__()
        self.val = value

    def execute(self) -> tp.Union[int, float]:
        return self.val


class BinaryOperation(Operation):
    def __init__(self, left_op: 'Operation', right_op: 'Operation') -> None:
        super().__init__()
        self.left = left_op
        self.right = right_op


class BinaryAddOp(BinaryOperation):
    def execute(self) -> tp.Union[int, float]:
        return self.left.execute() + self.right.execute()


class BinarySubOp(BinaryOperation):
    def execute(self) -> tp.Union[int, float]:
        return self.left.execute() - self.right.execute()


class BinaryMulOp(BinaryOperation):
    def execute(self) -> tp.Union[int, float]:
        return self.left.execute() * self.right.execute()


class BinaryDivOp(BinaryOperation):
    def execute(self) -> tp.Union[int, float]:
        return self.left.execute() / self.right.execute()


class UnarySub(Operation):
    def __init__(self, operation: 'Operation') -> None:
        super().__init__()
        self.op = operation

    def execute(self) -> tp.Union[int, float]:
        return -self.op.execute()
