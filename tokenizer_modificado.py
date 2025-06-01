from token_class import Token

palavrasReservadas = [
    "music_base",
    "instrument",
    "tempo_base",
    "note",
    "duration",
    "pause",
    "repeat",
    "times",
    "while",
    "if",
    "else",
    "var",
    "play_note",
    "play_sequence",
]
logicalList = ["and", "or"]
tiposReservados = ["int", "float", "bool", "note", "sequence"]


def verificaPalavraReservada(newToken):
    if newToken in tiposReservados:
        return newToken
    if newToken in logicalList:
        return newToken
    if newToken in palavrasReservadas:
        return newToken
    return "identifier"


class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.position = 0
        self.next = None
        self.selectNext()

    def selectNext(self):
        while self.position < len(self.source) and self.source[self.position] in " \t":
            self.position += 1

        if self.position < len(self.source):
            char = self.source[self.position]
            newToken = ""

            if char == "+":
                self.next = Token("plus", "+")
                self.position += 1

            elif char == "-":
                self.next = Token("minus", "-")
                self.position += 1

            elif char == "*":
                self.next = Token("multiplier", "*")
                self.position += 1

            elif char == "/":
                self.next = Token("divider", "/")
                self.position += 1

            elif char == "(":
                self.next = Token("openParentheses", "(")
                self.position += 1

            elif char == ")":
                self.next = Token("closeParentheses", ")")
                self.position += 1

            elif char == "{":
                self.next = Token("openBlock", "{")
                self.position += 1

            elif char == "}":
                self.next = Token("closeBlock", "}")
                self.position += 1

            elif char == "[":
                self.next = Token("openBrackets", "[")
                self.position += 1

            elif char == "]":
                self.next = Token("closeBrackets", "]")
                self.position += 1

            elif char == ",":
                self.next = Token("comma", ",")
                self.position += 1

            elif char == "\n":
                self.next = Token("lineBreaker", "\n")
                self.position += 1

            elif char == "=":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "="
                ):
                    self.next = Token("eq", "==")
                    self.position += 2
                else:
                    self.next = Token("assign", "=")
                    self.position += 1

            elif char == "!":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "="
                ):
                    self.next = Token("neq", "!=")
                    self.position += 2
                else:
                    self.next = Token("not", "!")
                    self.position += 1

            elif char == ">":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "="
                ):
                    self.next = Token("gte", ">=")
                    self.position += 2
                else:
                    self.next = Token("gt", ">")
                    self.position += 1

            elif char == "<":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "="
                ):
                    self.next = Token("lte", "<=")
                    self.position += 2
                else:
                    self.next = Token("lt", "<")
                    self.position += 1

            elif char == "|":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "|"
                ):
                    self.next = Token("or", "||")
                    self.position += 2
                else:
                    raise ValueError(
                        f"ERRO LÉXICO: caractere inválido '{char}' na posição {self.position}"
                    )

            elif char == "&":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "&"
                ):
                    self.next = Token("and", "&&")
                    self.position += 2
                else:
                    raise ValueError(
                        f"ERRO LÉXICO: caractere inválido '{char}' na posição {self.position}"
                    )

            elif char.isdigit():
                has_dot = False
                while self.position < len(self.source) and (
                    self.source[self.position].isdigit()
                    or (self.source[self.position] == "." and not has_dot)
                ):
                    if self.source[self.position] == ".":
                        has_dot = True
                    newToken += self.source[self.position]
                    self.position += 1
                if has_dot:
                    self.next = Token("number_float", newToken)
                else:
                    self.next = Token("number_int", newToken)

            elif char == '"':
                self.position += 1
                while (
                    self.position < len(self.source)
                    and self.source[self.position] != '"'
                ):
                    newToken += self.source[self.position]
                    self.position += 1
                if (
                    self.position < len(self.source)
                    and self.source[self.position] == '"'
                ):
                    self.position += 1
                    self.next = Token("string", newToken)
                else:
                    raise ValueError("ERRO LÉXICO: String não fechada")

            elif (
                self.position + 1 < len(self.source)
                and self.source[self.position] in "ABCDEFG"
                and self.source[self.position + 1] in "#b"
            ):
                nota = self.source[self.position] + self.source[self.position + 1]
                self.position += 2
                if (
                    self.position < len(self.source)
                    and self.source[self.position].isdigit()
                ):
                    nota += self.source[self.position]
                    self.position += 1
                self.next = Token("note_name", nota)

            elif self.source[self.position] in "ABCDEFG":
                nota = self.source[self.position]
                self.position += 1
                if (
                    self.position < len(self.source)
                    and self.source[self.position].isdigit()
                ):
                    nota += self.source[self.position]
                    self.position += 1
                self.next = Token("note_name", nota)

            elif char.isalpha() or char == "_":
                while self.position < len(self.source) and (
                    self.source[self.position].isalnum()
                    or self.source[self.position] == "_"
                ):
                    newToken += self.source[self.position]
                    self.position += 1

                if newToken == "true" or newToken == "false":
                    self.next = Token("bool", newToken)
                elif newToken == "and":
                    self.next = Token("and", "&&")
                elif newToken == "or":
                    self.next = Token("or", "||")
                else:
                    tipagem = verificaPalavraReservada(newToken)
                    self.next = Token(tipagem, newToken)

            else:
                raise ValueError(
                    f"ERRO LÉXICO: caractere inválido '{char}' na posição {self.position}"
                )

        else:
            self.next = Token("EOF", "")
