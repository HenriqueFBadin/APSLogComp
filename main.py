import sys
from symbolTable import SymbolTable
from parser import *
from code_class import Code
from node import Node


def main():
    st = SymbolTable()
    source = sys.argv[1]
    base = source.rsplit(".", 1)[0]
    with open(source, "r", encoding="utf-8") as file:
        source = file.read()

    ast = Parser.run(source)
    ast.generate(st)
    Code.dump(f"{base}.ll")


if __name__ == "__main__":
    main()
