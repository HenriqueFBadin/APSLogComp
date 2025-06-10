from node import *
from tokenizer import Tokenizer
from prepro import PrePro


class Parser:
    tokenizador = None

    @staticmethod
    def parseProgram():
        program = Block("Program", [])

        token = Parser.tokenizador.next

        if token.type == "music_base":
            program.children.append(Parser.parseMusicBase())
            Parser.tokenizador.selectNext()

            while Parser.tokenizador.next.type != "EOF":
                token = Parser.tokenizador.next
                if token.type == "var":
                    program.children.append(Parser.parseVarDec())
                    Parser.tokenizador.selectNext()

                elif token.type == "lineBreaker":
                    Parser.tokenizador.selectNext()

                elif token.type == "openBlock":
                    program.children.append(Parser.parseBlock())
                    Parser.tokenizador.selectNext()

                else:
                    raise SyntaxError(
                        f"Token inesperado no início do programa: {token.type}. Deveria ser uma declaração de 'var' ou um bloco"
                    )

        else:
            raise SyntaxError(
                f"Token inesperado no início do programa: {token.type}. Deveria ser uma declaração de music_base"
            )

        return program

    @staticmethod
    def parseVarDec():
        Parser.tokenizador.selectNext()
        token = Parser.tokenizador.next

        if token.type != "identifier":
            raise SyntaxError("Esperado identificador após 'var'")

        ident = Identifier(value=token.value, children=[])
        Parser.tokenizador.selectNext()
        token = Parser.tokenizador.next

        if token.type != "type":
            raise SyntaxError("Esperado tipo após identificador")

        tipo = token.value
        Parser.tokenizador.selectNext()

        if Parser.tokenizador.next.type == "assignment":
            Parser.tokenizador.selectNext()
            expr = Parser.parseBExpression()
            return VarDec(tipo, [ident, expr])
        else:
            return VarDec(tipo, [ident])

    @staticmethod
    def parseMusicBase():
        Parser.tokenizador.selectNext()
        token = Parser.tokenizador.next

        if token.type != "openBlock":
            raise SyntaxError("Esperado abrir chaves após 'music_base'")

        Parser.tokenizador.selectNext()
        token = Parser.tokenizador.next

        if token.type == "lineBreaker":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next

        if token.type == "instrument":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "string":
                instrument = StrVal(value=(token.value), children=[])
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type != "lineBreaker":
                    raise ValueError(
                        "Token inesperado na leitura na declaração do music_base"
                    )
                else:
                    Parser.tokenizador.selectNext()
                    token = Parser.tokenizador.next
                    if token.type == "tempo_base":
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
                        if token.type == "int":
                            tempo = IntVal(value=(token.value), children=[])
                            Parser.tokenizador.selectNext()
                            token = Parser.tokenizador.next
                            while token.type == "lineBreaker":
                                Parser.tokenizador.selectNext()
                                token = Parser.tokenizador.next
                            if token.type != "closeBlock":
                                raise SyntaxError(
                                    "Esperado fechar chaves após 'music_base'"
                                )

                            return MusicBase(
                                value="music_base", children=[instrument, tempo]
                            )
        else:
            raise SyntaxError("Esperado 'instrument' após abrir chaves em 'music_base'")

    @staticmethod
    def parseBlock():
        block = Block(value="Block", children=[])
        token = Parser.tokenizador.next

        if token.type == "openBlock":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "lineBreaker":
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                while token.type != "closeBlock":
                    block.children.append(Parser.parseStatement())
                    Parser.tokenizador.selectNext()
                    token = Parser.tokenizador.next
                Parser.tokenizador.selectNext()

            else:
                raise SyntaxError("Falta um '\n' depois da abertura do bloco")

        else:
            raise SyntaxError("O bloco não foi iniciado")

        return block

    @staticmethod
    def parseStatement():
        statement = NoOp(value="", children=[])
        token = Parser.tokenizador.next

        if token.type == "identifier":
            statement = Identifier(value=(token.value), children=[])
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "assignment":
                Parser.tokenizador.selectNext()
                statement = Assignment(
                    value="=",
                    children=[statement, Parser.parseBExpression()],
                )
                token = Parser.tokenizador.next
            else:
                raise SyntaxError("Esperado um = após um identificador")
        elif token.type == "repeat":
            Parser.tokenizador.selectNext()
            expression = Parser.parseBExpression()
            token = Parser.tokenizador.next
            if token.type == "times":
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type == "while":
                    Parser.tokenizador.selectNext()
                    statement = RepeatWhile(
                        value="while",
                        children=[
                            Parser.parseBExpression(),
                            Repeat(
                                value="repeat",
                                children=[expression, Parser.parseBlock()],
                            ),
                        ],
                    )
                else:
                    statement = Repeat(
                        value="repeat", children=[expression, Parser.parseBlock()]
                    )
            else:
                raise SyntaxError("Esperado 'times' após a expressão de repetição")

        elif token.type == "if":
            Parser.tokenizador.selectNext()
            statement = If(
                value="if", children=[Parser.parseBExpression(), Parser.parseBlock()]
            )
            token = Parser.tokenizador.next
            if token.type == "else":
                Parser.tokenizador.selectNext()
                statement.children.append(Parser.parseBlock())

        elif token.type == "play_note":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "note":
                statement = PlayNote(
                    value="play_note",
                    children=[NoteVal(value=token.value, children=[])],
                )
                Parser.tokenizador.selectNext()
            elif token.type == "identifier":
                statement = PlayNote(
                    value="play_note",
                    children=[Identifier(value=token.value, children=[])],
                )
                Parser.tokenizador.selectNext()
            else:
                raise SyntaxError("Era esperado uma nota após 'play_note'")

        elif token.type == "play_sequence":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "identifier":
                Parser.tokenizador.selectNext()
                statement = PlaySequence(
                    value="play_sequence",
                    children=[Identifier(value=token.value, children=[])],
                )
            elif token.type == "openBrackets":
                Parser.tokenizador.selectNext()
                statement = PlaySequence(
                    value="play_sequence", children=[Parser.parseSequenceDec()]
                )
            else:
                raise SyntaxError("Era esperado uma nota após 'play_sequence'")

        elif token.type == "var":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "identifier":
                statement = Identifier(value=(token.value), children=[])
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type == "type":
                    token_value = token.value
                    Parser.tokenizador.selectNext()
                    token = Parser.tokenizador.next
                    if token.type == "assignment":
                        Parser.tokenizador.selectNext()
                        statement = VarDec(
                            value=token_value,
                            children=[statement, Parser.parseBExpression()],
                        )
                    else:
                        statement = VarDec(
                            value=token_value,
                            children=[statement],
                        )

                else:
                    raise SyntaxError(
                        "Era esperado um tipo depois da declaração de uma variável com var. Exemplo: var x int"
                    )
            else:
                raise SyntaxError(
                    "Era esperado um identificador depois da declaração de um 'var'"
                )

        elif token.type == "pause_duration":
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "int":
                statement = PauseDuration(
                    value="pause_duration",
                    children=[IntVal(value=int(token.value), children=[])],
                )
                Parser.tokenizador.selectNext()
            elif token.type == "double":
                statement = PauseDuration(
                    value="pause_duration",
                    children=[DoubleVal(value=float(token.value), children=[])],
                )
                Parser.tokenizador.selectNext()
            else:
                raise SyntaxError("Era esperado um inteiro após 'pause_duration'")

        token = Parser.tokenizador.next
        if token.type != "lineBreaker":
            raise SyntaxError("Era esperado um '\n' ou um 'identifier' ou um 'Println'")

        return statement

    @staticmethod
    def parseBExpression():
        resultado = Parser.parseBTerm()
        while Parser.tokenizador.next.type == "or":
            if Parser.tokenizador.next.type == "or":
                Parser.tokenizador.selectNext()
                resultado = BinOp("||", [resultado, Parser.parseBTerm()])
        return resultado

    @staticmethod
    def parseBTerm():
        resultado = Parser.parseReExpression()
        while Parser.tokenizador.next.type == "and":
            if Parser.tokenizador.next.type == "and":
                Parser.tokenizador.selectNext()
                resultado = BinOp("&&", [resultado, Parser.parseReExpression()])
        return resultado

    @staticmethod
    def parseReExpression():
        resultado = Parser.parseExpression()
        token = Parser.tokenizador.next
        while (
            Parser.tokenizador.next.type == "compare"
            or Parser.tokenizador.next.type == "greater than"
            or Parser.tokenizador.next.type == "less than"
        ):
            if Parser.tokenizador.next.value == "==":
                Parser.tokenizador.selectNext()
                resultado = BinOp("==", [resultado, Parser.parseExpression()])
            elif Parser.tokenizador.next.value == ">":
                Parser.tokenizador.selectNext()
                resultado = BinOp(">", [resultado, Parser.parseExpression()])
            elif Parser.tokenizador.next.value == "<":
                Parser.tokenizador.selectNext()
                resultado = BinOp("<", [resultado, Parser.parseExpression()])
        return resultado

    @staticmethod
    def parseExpression():
        resultado = Parser.parseTerm()
        while (
            Parser.tokenizador.next.type == "plus"
            or Parser.tokenizador.next.type == "minus"
        ):
            if Parser.tokenizador.next.type == "plus":
                Parser.tokenizador.selectNext()
                resultado = BinOp("+", [resultado, Parser.parseTerm()])
            elif Parser.tokenizador.next.type == "minus":
                Parser.tokenizador.selectNext()
                resultado = BinOp("-", [resultado, Parser.parseTerm()])
        return resultado

    @staticmethod
    def parseTerm():

        resultado = Parser.parseFactor()
        while (
            Parser.tokenizador.next.type == "multiplier"
            or Parser.tokenizador.next.type == "divider"
        ):
            if Parser.tokenizador.next.type == "multiplier":
                Parser.tokenizador.selectNext()
                resultado = BinOp("*", [resultado, Parser.parseFactor()])
            elif Parser.tokenizador.next.type == "divider":
                Parser.tokenizador.selectNext()
                resultado = BinOp("/", [resultado, Parser.parseFactor()])
        return resultado

    @staticmethod
    def parseFactor():
        factor = 0
        token = Parser.tokenizador.next

        if token.type == "int":
            factor = IntVal(value=int(token.value), children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "double":
            factor = DoubleVal(value=float(token.value), children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "string":
            factor = StrVal(value=(token.value), children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "bool":
            factor = BoolVal(value=bool(token.value), children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "note":
            factor = NoteVal(value=token.value, children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "openBrackets":
            Parser.tokenizador.selectNext()
            factor = Parser.parseSequenceDec()
        elif token.type == "identifier":
            factor = Identifier(value=token.value, children=[])
            Parser.tokenizador.selectNext()
        elif token.type == "plus":
            Parser.tokenizador.selectNext()
            factor = UnOp("+", [Parser.parseFactor()])
        elif token.type == "minus":
            Parser.tokenizador.selectNext()
            factor = UnOp("-", [Parser.parseFactor()])
        elif token.type == "not":
            Parser.tokenizador.selectNext()
            factor = UnOp("!", [Parser.parseFactor()])

        elif token.type == "openParentheses":
            Parser.tokenizador.selectNext()
            factor = Parser.parseBExpression()
            token = Parser.tokenizador.next
            if token.type == "closeParentheses":
                Parser.tokenizador.selectNext()
            else:
                raise TypeError("Parenteses de fechamento faltando")
        else:
            raise TypeError("Caractere não esperado")

        return factor

    @staticmethod
    def parseSequenceDec():
        sequence = SequenceDec(value="SequenceDec", children=[])

        token = Parser.tokenizador.next

        while token.type != "closeBrackets":
            while token.type == "lineBreaker":
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type == "closeBrackets":
                    break
            if token.type == "note":
                sequence.children.append(NoteVal(value=token.value, children=[]))
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type == "pause_duration":
                    Parser.tokenizador.selectNext()
                    token = Parser.tokenizador.next
                    if token.type == "int":
                        sequence.children.append(
                            PauseDuration(
                                value="pause_duration",
                                children=[IntVal(value=int(token.value), children=[])],
                            )
                        )
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
                    elif token.type == "double":
                        sequence.children.append(
                            PauseDuration(
                                value="pause_duration",
                                children=[
                                    DoubleVal(value=float(token.value), children=[])
                                ],
                            )
                        )
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
                    else:
                        raise SyntaxError(
                            "Era esperado um inteiro ou um double após 'pause_duration'"
                        )

                    if token.type == "comma":
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next

            elif token.type == "identifier":
                sequence.children.append(Identifier(value=token.value, children=[]))
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
                if token.type == "pause_duration":
                    Parser.tokenizador.selectNext()
                    token = Parser.tokenizador.next
                    if token.type == "int":
                        sequence.children.append(
                            PauseDuration(
                                value="pause_duration",
                                children=[IntVal(value=int(token.value), children=[])],
                            )
                        )
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
                    elif token.type == "double":
                        sequence.children.append(
                            PauseDuration(
                                value="pause_duration",
                                children=[
                                    DoubleVal(value=float(token.value), children=[])
                                ],
                            )
                        )
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
                    else:
                        raise SyntaxError(
                            "Era esperado um inteiro ou um double após 'pause_duration'"
                        )

                    if token.type == "comma":
                        Parser.tokenizador.selectNext()
                        token = Parser.tokenizador.next
            elif token.type == "closeBrackets":
                break
            else:
                raise SyntaxError(
                    f"Era esperado uma nota com 'pause_duration' para se iniciar uma sequencia. Token atual: {token.type}"
                )

        Parser.tokenizador.selectNext()

        return sequence

    @staticmethod
    def run(code):
        code = PrePro.filter(code)
        # print(code)
        Parser.tokenizador = Tokenizer(code)
        expression = Parser.parseProgram()
        token = Parser.tokenizador.next
        if token.type == "EOF":
            return expression
        else:
            token = Parser.tokenizador.next
            print(
                f"Token type = {token.type}, Token value = {token.value}, Expression = {expression}"
            )
            raise TypeError("O token final não é um EOF")
