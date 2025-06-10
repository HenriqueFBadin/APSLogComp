class SymbolTable:
    def __init__(self):
        self.symbolDict = {}
        self.offset = 0  # [ebp-offset]

    def create(self, key, data):
        """
        Cria uma variável na tabela de símbolos. Recebe o nome da variável e uma tupla com o tipo e o valor atual dela.
        Se a variável já existir, lança um KeyError.
        """
        if key in self.symbolDict:
            raise KeyError(f"A variável '{key}' já foi declarada.")
        self.symbolDict[key] = data

    # def set(self, key, value):
    #     if key not in self.symbolDict:
    #         raise KeyError(f"A variável '{key}' não foi declarada.")
    #     _type, _ = self.symbolDict[key]
    #     if _type != value[0]:
    #         raise SyntaxError(
    #             f"Erro de atribuição. Tentando atribuir um {value[0]} numa variável {_type}"
    #         )
    #     self.symbolDict[key] = (_type, value[1])

    # def get(self, key):
    #     if key not in self.symbolDict:
    #         raise KeyError(f"A variável '{key}' não foi declarada.")
    #     return self.symbolDict[key]

    def get(self, key):
        return self.symbolDict[key]
