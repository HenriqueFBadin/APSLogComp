from node_adaptado import *
from tokenizer_modificado import Tokenizer
from prepro import PrePro


class Parser:
    tokenizador = None

    @staticmethod
    def parseProgram():
        setup = Parser.parseSetup()
        if Parser.tokenizador.next.type != "lineBreaker":
            raise SyntaxError("Esperado nova linha após setup")
        Parser.tokenizador.selectNext()
        block = Block("Block", [])
        while Parser.tokenizador.next.type != "EOF":
            if Parser.tokenizador.next.type == "lineBreaker":
                Parser.tokenizador.selectNext()
                continue
            block.children.append(Parser.parseStatement())
            Parser.tokenizador.selectNext()
        program = Block("Program", [setup, block])
        return program

    @staticmethod
    def parseSetup():
        setup_children = []
        if Parser.tokenizador.next.value != "music_base":
            raise SyntaxError("Esperado 'music_base' no início do programa")
        Parser.tokenizador.selectNext()
        if Parser.tokenizador.next.type != "openBlock":
            raise SyntaxError("Esperado '{' após music_base")
        Parser.tokenizador.selectNext()
        while Parser.tokenizador.next.type != "closeBlock":
            if Parser.tokenizador.next.type == "lineBreaker":
                Parser.tokenizador.selectNext()
                continue
            token = Parser.tokenizador.next
            if token.type == "instrument":
                Parser.tokenizador.selectNext()
                if Parser.tokenizador.next.type != "string":
                    raise SyntaxError("Esperado string após 'instrument'")
                token = Parser.tokenizador.next
                setup_children.append(Instrument(token.value, []))
                Parser.tokenizador.selectNext()
                token = Parser.tokenizador.next
            elif token.type == "tempo_base":
                Parser.tokenizador.selectNext()
                if (
                    Parser.tokenizador.next.type != "number_int"
                    and Parser.tokenizador.next.type != "number_float"
                ):
                    raise SyntaxError("Esperado número após 'tempo_base'")
                token = Parser.tokenizador.next
                setup_children.append(Tempo("tempo_base", [IntVal(token.value, [])]))
                Parser.tokenizador.selectNext()
            else:
                raise SyntaxError("Esperado 'instrument' ou 'tempo_base'")
        Parser.tokenizador.selectNext()
        return MusicBase("music_base", setup_children)

    @staticmethod
    def parseStatement():
        token = Parser.tokenizador.next
        if token.type == "play_note":
            Parser.tokenizador.selectNext()
            if Parser.tokenizador.next.type == "identifier":
                note = Identifier(Parser.tokenizador.next.value, [])
                Parser.tokenizador.selectNext()
            else:
                note = Parser.parseNoteItem()
            return PlayNote("play_note", [note])

        elif token.type == "play_sequence":
            Parser.tokenizador.selectNext()
            if Parser.tokenizador.next.type == "identifier":
                seq = Identifier(Parser.tokenizador.next.value, [])
                Parser.tokenizador.selectNext()
            else:
                seq = Parser.parseSequence()
            return PlaySequence("play_sequence", [seq])

        elif token.type == "pause":
            Parser.tokenizador.selectNext()
            if Parser.tokenizador.next.type != "duration":
                raise SyntaxError("Esperado 'duration' após 'pause'")
            Parser.tokenizador.selectNext()
            dur = Parser.parseFactor()
            return Pause("pause", [dur])

        elif token.type == "if":
            Parser.tokenizador.selectNext()
            cond = Parser.parseBExpression()
            if Parser.tokenizador.next.type != "lineBreaker":
                raise SyntaxError("Esperado NEWLINE após expressão if")
            Parser.tokenizador.selectNext()
            block_true = Parser.parseBlock()
            if Parser.tokenizador.next.type == "else":
                Parser.tokenizador.selectNext()
                block_false = Parser.parseBlock()
                return If("if", [cond, block_true, block_false])
            return If("if", [cond, block_true])

        elif token.type == "repeat":
            Parser.tokenizador.selectNext()
            repetitions = Parser.parseFactor()

            if Parser.tokenizador.next.type != "times":
                raise SyntaxError("Esperado 'times' após 'repeat'")
            Parser.tokenizador.selectNext()

            if Parser.tokenizador.next.type == "while":
                Parser.tokenizador.selectNext()
                condition = Parser.parseBExpression()
                if Parser.tokenizador.next.type != "lineBreaker":
                    raise SyntaxError("Esperado NEWLINE após expressão do repeat while")
                Parser.tokenizador.selectNext()
                block = Parser.parseBlock()
                return RepeatWhile("repeat_while", [repetitions, condition, block])

            elif Parser.tokenizador.next.type == "lineBreaker":
                Parser.tokenizador.selectNext()
                block = Parser.parseBlock()
                return Repeat("repeat", [repetitions, block])

            else:
                raise SyntaxError("Forma inválida após 'times'")

        elif token.type == "var":
            Parser.tokenizador.selectNext()  # Come, var

            # Nome do identificador
            if Parser.tokenizador.next.type != "identifier":
                raise SyntaxError("Esperado nome do identificador após 'var'")
            name = Parser.tokenizador.next.value
            Parser.tokenizador.selectNext()

            # Tipo obrigatório
            if Parser.tokenizador.next.type not in [
                "int",
                "float",
                "bool",
                "note",
                "sequence",
            ]:
                raise SyntaxError(
                    f"Esperado tipo após identificador. Token atual {Parser.tokenizador.next.type}"
                )
            var_type = Parser.tokenizador.next.type  # Ex: "int", "note" etc.
            Parser.tokenizador.selectNext()

            # Inicialização (opcional)
            if Parser.tokenizador.next.type == "assign":
                Parser.tokenizador.selectNext()
                value = Parser.parseFactor()
                return VarDec(var_type, [Identifier(name, []), value])
            else:
                return VarDec(var_type, [Identifier(name, [])])

        elif token.type == "identifier":
            statement = Identifier(value=(token.value), children=[])
            Parser.tokenizador.selectNext()
            token = Parser.tokenizador.next
            if token.type == "assign":
                Parser.tokenizador.selectNext()
                statement = Assignment(
                    value="=",
                    children=[statement, Parser.parseBExpression()],
                )
                return statement
            else:
                raise SyntaxError("Esperado um = após um identificador")

        elif token.type == "lineBreaker":
            return NoOp("", [])

        else:
            raise SyntaxError(f"Comando inesperado: {token.type}")

    @staticmethod
    def parseNoteItem():
        if Parser.tokenizador.next.type != "note":
            raise SyntaxError("Esperado 'note'")
        Parser.tokenizador.selectNext()
        note = Parser.parseFactor()
        if Parser.tokenizador.next.type != "duration":
            raise SyntaxError("Esperado 'duration'")
        Parser.tokenizador.selectNext()
        duration = Parser.parseFactor()
        return Note("note", [note, duration])

    @staticmethod
    def parseSequence():
        if Parser.tokenizador.next.type != "openBrackets":
            raise SyntaxError("Esperado '['")
        Parser.tokenizador.selectNext()

        items = []
        while Parser.tokenizador.next.type != "closeBrackets":
            if Parser.tokenizador.next.type == "note":
                # Adiciona a nota
                items.append(Parser.parseNoteItem())

                # Verifica se tem pausa após a nota
                if Parser.tokenizador.next.type == "pause":
                    Parser.tokenizador.selectNext()
                    if Parser.tokenizador.next.type != "duration":
                        raise SyntaxError("Esperado 'duration' após 'pause'")
                    Parser.tokenizador.selectNext()
                    dur = Parser.parseFactor()
                    # Armazena a pausa como parte da sequência
                    items.append(Pause("pause", [dur]))

            elif Parser.tokenizador.next.type == "identifier":
                items.append(Identifier(Parser.tokenizador.next.value, []))
                Parser.tokenizador.selectNext()

                # Verifica pausa após identificador
                if Parser.tokenizador.next.type == "pause":
                    Parser.tokenizador.selectNext()
                    if Parser.tokenizador.next.type != "duration":
                        raise SyntaxError("Esperado 'duration' após 'pause'")
                    Parser.tokenizador.selectNext()
                    dur = Parser.parseFactor()
                    items.append(Pause("pause", [dur]))

            if Parser.tokenizador.next.type == "comma":
                Parser.tokenizador.selectNext()

        Parser.tokenizador.selectNext()
        return Sequence("sequence", items)

    @staticmethod
    def parseBlock():
        if Parser.tokenizador.next.type != "openBlock":
            raise SyntaxError(
                f"Esperado '{{' para abrir bloco, mas o token foi {Parser.tokenizador.next.type}"
            )
        Parser.tokenizador.selectNext()
        if Parser.tokenizador.next.type != "lineBreaker":
            raise SyntaxError("Esperado NEWLINE após abertura de bloco")
        Parser.tokenizador.selectNext()
        block = Block("Block", [])
        while Parser.tokenizador.next.type != "closeBlock":
            block.children.append(Parser.parseStatement())
            Parser.tokenizador.selectNext()
        Parser.tokenizador.selectNext()
        return block

    @staticmethod
    def parseBExpression():
        result = Parser.parseBTerm()
        while Parser.tokenizador.next.type == "or":
            Parser.tokenizador.selectNext()
            result = BinOp("||", [result, Parser.parseBTerm()])
        return result

    @staticmethod
    def parseBTerm():
        result = Parser.parseReExpression()
        while Parser.tokenizador.next.type == "and":
            Parser.tokenizador.selectNext()
            result = BinOp("&&", [result, Parser.parseReExpression()])
        return result

    @staticmethod
    def parseReExpression():
        result = Parser.parseExpression()
        if Parser.tokenizador.next.value in ["==", "!=", ">", "<", ">=", "<="]:
            op = Parser.tokenizador.next.value
            Parser.tokenizador.selectNext()
            right = Parser.parseExpression()
            result = BinOp(op, [result, right])
        return result

    @staticmethod
    def parseExpression():
        result = Parser.parseTerm()
        while Parser.tokenizador.next.type in ["plus", "minus"]:
            op = Parser.tokenizador.next.value
            Parser.tokenizador.selectNext()
            result = BinOp(op, [result, Parser.parseTerm()])
        return result

    @staticmethod
    def parseTerm():
        result = Parser.parseFactor()
        while Parser.tokenizador.next.type in ["multiplier", "divider"]:
            op = Parser.tokenizador.next.value
            Parser.tokenizador.selectNext()
            result = BinOp(op, [result, Parser.parseFactor()])
        return result

    @staticmethod
    def parseFactor():
        token = Parser.tokenizador.next
        if token.type == "number_int":
            Parser.tokenizador.selectNext()
            return IntVal(int(token.value), [])
        elif token.type == "number_float":
            Parser.tokenizador.selectNext()
            return FloatVal(float(token.value), [])
        elif token.type == "string":
            Parser.tokenizador.selectNext()
            return StrVal(token.value, [])
        elif token.type == "identifier":
            Parser.tokenizador.selectNext()
            return Identifier(token.value, [])
        elif token.type == "note":
            return Parser.parseNoteItem()
        elif token.type == "note_name":
            Parser.tokenizador.selectNext()
            return Identifier(token.value, [])
        elif token.type == "openBrackets":
            return Parser.parseSequence()
        elif token.type == "not":
            Parser.tokenizador.selectNext()
            return UnOp("!", [Parser.parseFactor()])
        elif token.type == "openParentheses":
            Parser.tokenizador.selectNext()
            expr = Parser.parseBExpression()
            if Parser.tokenizador.next.type != "closeParentheses":
                raise SyntaxError("Parêntese de fechamento faltando")
            Parser.tokenizador.selectNext()
            return expr
        else:
            raise SyntaxError(f"Token inesperado no fator: {token.type}")

    @staticmethod
    def run(code):
        code = PrePro.filter(code)
        Parser.tokenizador = Tokenizer(code)
        result = Parser.parseProgram()
        if Parser.tokenizador.next.type != "EOF":
            raise TypeError("Token extra após o fim do programa")
        return result
