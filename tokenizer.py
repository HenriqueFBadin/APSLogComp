from token_class import Token

palavrasReservadas = [
    "if",
    "else",
    "while",
    "for",
    "var",
    "music_base",
    "tempo_base",
    "repeat",
    "pause_duration",
    "instrument",
    "play_note",
    "play_sequence",
    "times",
]
typeList = ["int", "string", "bool", "double", "note", "sequence"]


def isType(newToken):
    for _type in typeList:
        if newToken == _type:
            return "type"
    return "identifier"


def identificaBoolean(token):
    if token in {"true", "false"}:
        return "bool"

    return "identifier"


def verificaPalavraReservada(newToken):
    for palavra in palavrasReservadas:
        if newToken == palavra:
            if palavra == "for" or palavra == "while":
                return "while"
            return palavra
    return "identifier"


class Tokenizer:
    def __init__(self, source: str):
        self.source = source  # código-fonte que será tokenizado
        self.position = 0  # posição atual em que o Tokenizer está separando
        self.next = None  # último token separado
        self.selectNext()

    def selectNext(self):

        while self.position < len(self.source) and self.source[self.position] == " ":
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

            elif char == "\n":
                self.next = Token("lineBreaker", "\n")
                self.position += 1

            elif char == "\t":
                self.next = Token("tab", "\t")
                self.position += 1

            elif char == "=":
                if (
                    self.position + 1 < len(self.source)
                    and self.source[self.position + 1] == "="
                ):
                    self.next = Token("compare", "==")
                    self.position += 2
                else:
                    self.next = Token("assignment", "=")
                    self.position += 1

            elif char == ">":
                self.next = Token("greater than", ">")
                self.position += 1

            elif char == "<":
                self.next = Token("less than", "<")
                self.position += 1

            elif char == "!":
                self.next = Token("not", "!")
                self.position += 1

            elif char == "=":
                self.position += 1
                if self.position < len(self.source):
                    char = self.source[self.position]
                    if char == "=":
                        self.next = Token("compare", "==")
                        self.position += 1
                    else:
                        self.next = Token("assignment", "=")
                else:
                    self.next = Token("assignment", "=")

            elif char == "|":
                self.position += 1
                char = self.source[self.position]
                if char == "|":
                    self.next = Token("or", "||")
                    self.position += 1

            elif char == "&":
                self.position += 1
                char = self.source[self.position]
                if char == "&":
                    self.next = Token("and", "&&")
                    self.position += 1

            elif char == ",":
                self.next = Token("comma", ",")
                self.position += 1

            elif char.isdigit():
                isDouble = False
                while self.position < len(self.source) and (
                    self.source[self.position].isdigit()
                    or self.source[self.position] == "."
                ):
                    char = self.source[self.position]

                    # Verifica se é um ponto decimal e se ainda não encontrou um ponto antes
                    if char == "." and not isDouble:
                        isDouble = True
                    # Se encontrar um segundo ponto, é um erro
                    elif char == "." and isDouble:
                        raise ValueError(
                            "Número com formato inválido: múltiplos pontos decimais"
                        )

                    newToken += char
                    self.position += 1

                if isDouble:
                    self.next = Token("double", newToken)
                else:
                    self.next = Token("int", newToken)

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
                    self.next = Token("string", newToken)
                    self.position += 1
                else:
                    raise ValueError("String não fechada")

            elif char.isalpha() or char == "_":
                while self.position < len(self.source) and (
                    self.source[self.position].isalpha()
                    or self.source[self.position].isdigit()
                    or self.source[self.position] == "_"
                ):
                    char = self.source[self.position]
                    newToken += char
                    self.position += 1

                if newToken == "note":
                    # Pula espaços após "note"
                    a = self.source[self.position]
                    while (
                        self.position < len(self.source)
                        and self.source[self.position] == " "
                    ):
                        self.position += 1

                    # Lê a informação da nota (A-G, opcionalmente # ou b, seguido de dígito)
                    note_name = ""

                    # Verifica se tem uma letra de A a G
                    if (
                        self.position < len(self.source)
                        and self.source[self.position].upper() in "ABCDEFG"
                    ):
                        note_name += self.source[self.position].upper()
                        self.position += 1

                        # Verifica se tem # ou b (opcional)
                        if (
                            self.position < len(self.source)
                            and self.source[self.position] in "#b"
                        ):
                            note_name += self.source[self.position]
                            self.position += 1

                        # Verifica se tem um dígito
                        if (
                            self.position < len(self.source)
                            and self.source[self.position].isdigit()
                        ):
                            note_name += self.source[self.position]
                            self.position += 1

                            # Procura "duration"
                            # Pula espaços
                            while (
                                self.position < len(self.source)
                                and self.source[self.position] == " "
                            ):
                                self.position += 1

                            # Verifica se as próximas letras formam "duration"
                            duration_word = ""
                            temp_position = self.position

                            while (
                                temp_position < len(self.source)
                                and self.source[temp_position].isalpha()
                            ):
                                duration_word += self.source[temp_position]
                                temp_position += 1

                            if duration_word == "duration":
                                self.position = temp_position  # Avança a posição

                                # Pula espaços após "duration"
                                while (
                                    self.position < len(self.source)
                                    and self.source[self.position] == " "
                                ):
                                    self.position += 1

                                # Lê o valor numérico da duração
                                duration_value = ""
                                isDouble = False

                                while self.position < len(self.source) and (
                                    self.source[self.position].isdigit()
                                    or self.source[self.position] == "."
                                ):
                                    if self.source[self.position] == ".":
                                        if isDouble:
                                            raise ValueError(
                                                "Nota com duração inválida: múltiplos pontos decimais"
                                            )
                                        isDouble = True

                                    duration_value += self.source[self.position]
                                    self.position += 1

                                if duration_value:
                                    # Converte a duração para float ou int conforme necessário
                                    if isDouble:
                                        duration_number = float(duration_value)
                                    else:
                                        duration_number = int(duration_value)

                                    # Cria o token com uma tupla contendo nome da nota e duração
                                    self.next = Token(
                                        "note", (note_name, duration_number)
                                    )
                    else:
                        tipagem = isType(newToken)
                        self.next = Token(tipagem, newToken)

                else:
                    tipagem = isType(newToken)
                    if tipagem == "identifier":
                        tipagem = verificaPalavraReservada(newToken)
                        if tipagem == "identifier":
                            if newToken == "true":
                                tipagem = "bool"
                                newToken = "True"
                            elif newToken == "false":
                                tipagem = "bool"
                                newToken = "False"

                    self.next = Token(tipagem, newToken)
            else:
                raise ValueError(f"Caractere inesperado: {char}")

        else:
            self.next = Token("EOF", "")
