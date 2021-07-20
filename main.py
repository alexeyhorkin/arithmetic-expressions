from calculator import tokenizer
from calculator.parser import parse_operation

if __name__ == "__main__":
    inp: str = "1 / 2"
    iterator = tokenizer.Tokenizer(inp).__iter__()
    op = parse_operation(iterator)
    print(op.execute())
