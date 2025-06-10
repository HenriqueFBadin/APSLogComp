from code_class import Code


class Node:
    id = 0
    temporary_position = 0
    temp_counter = 0

    def create_temporary():
        Node.temporary_position += 1
        return "tmp" + str(Node.temporary_position)

    def new_tmp(prefix="tmp"):
        Node.temp_counter += 1
        return f"%{prefix}{Node.temp_counter}"

    def generate_id():
        Node.id += 1
        return Node.id

    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.generate_id()
        self.temporary_position = Node.create_temporary()

    def evaluate(self, st):
        pass

    def generate(self, st):
        pass


class BinOp(Node):
    def evaluate(self, st):
        child_0 = self.children[0].evaluate(st)
        child_1 = self.children[1].evaluate(st)
        if self.value == "+":
            if child_0[0] == "int" and child_1[0] == "int":
                return ("int", (child_0[1] + child_1[1]))

            else:
                if child_0[0] == "bool":
                    val0 = str(child_0[1]).lower()
                else:
                    val0 = str(child_0[1])

                if child_1[0] == "bool":
                    val1 = str(child_1[1]).lower()
                else:
                    val1 = str(child_1[1])

                return ("string", val0 + val1)

        elif self.value == "-" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] - child_1[1]))
        elif self.value == "*" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] * child_1[1]))
        elif self.value == "/" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] // child_1[1]))
        elif self.value == ">":
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            return ("bool", (child_0[1] > child_1[1]))

        elif self.value == "<":
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            return ("bool", (child_0[1] < child_1[1]))

        elif self.value == "==":
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            return ("bool", (child_0[1] == child_1[1]))
        elif self.value == "&&" and (child_0[0] == "bool" and child_1[0] == "bool"):
            return ("bool", (child_0[1] & child_1[1]))
        elif self.value == "||" and (child_0[0] == "bool" and child_1[0] == "bool"):
            return ("bool", (child_0[1] | child_1[1]))

    def generate(self, st):
        tipo_l, val_l = self.children[0].generate(st)
        tipo_r, val_r = self.children[1].generate(st)
        op = self.value
        tmp = f"%tmp_binop_{self.id}"

        # Operações aritméticas: aceita int e double misturados
        if op in {"+", "-", "*", "/"}:
            # Se qualquer for double, converte ambos pra double e usa f*
            if tipo_l == "double" or tipo_r == "double":
                if tipo_l != "double":
                    val_l_cast = f"%castl_{self.id}"
                    Code.append(f"{val_l_cast} = sitofp i32 {val_l} to double")
                else:
                    val_l_cast = val_l
                if tipo_r != "double":
                    val_r_cast = f"%castr_{self.id}"
                    Code.append(f"{val_r_cast} = sitofp i32 {val_r} to double")
                else:
                    val_r_cast = val_r

                opmap = {"+": "fadd", "-": "fsub", "*": "fmul", "/": "fdiv"}
                Code.append(f"{tmp} = {opmap[op]} double {val_l_cast}, {val_r_cast}")
                return ("double", tmp)
            # Ambos int
            elif tipo_l == "i32" and tipo_r == "i32":
                opmap = {"+": "add", "-": "sub", "*": "mul", "/": "sdiv"}
                Code.append(f"{tmp} = {opmap[op]} i32 {val_l}, {val_r}")
                return ("i32", tmp)
            else:
                raise TypeError("Operação aritmética só aceita int/double.")

        # Comparação ==
        elif op == "==":
            # Comparação de note: compara os dois campos
            if tipo_l == "note" and tipo_r == "note":
                midi_l, dur_l = val_l
                midi_r, dur_r = val_r
                midi_cmp = f"%cmp_midi_{self.id}"
                dur_cmp = f"%cmp_dur_{self.id}"
                both_cmp = f"%cmp_both_{self.id}"
                # Compara midi_value
                Code.append(f"{midi_cmp} = icmp eq i32 {midi_l}, {midi_r}")
                # Compara duration (double)
                Code.append(f"{dur_cmp} = fcmp oeq double {dur_l}, {dur_r}")
                # Faz AND dos resultados
                Code.append(f"{both_cmp} = and i1 {midi_cmp}, {dur_cmp}")
                return ("i1", both_cmp)
            # Comparação entre outros tipos idênticos (exceto sequence)
            elif tipo_l == tipo_r and tipo_l != "sequence":
                if tipo_l == "i32":
                    Code.append(f"{tmp} = icmp eq i32 {val_l}, {val_r}")
                    return ("i1", tmp)
                elif tipo_l == "double":
                    Code.append(f"{tmp} = fcmp oeq double {val_l}, {val_r}")
                    return ("i1", tmp)
                elif tipo_l == "i1":
                    Code.append(f"{tmp} = icmp eq i1 {val_l}, {val_r}")
                    return ("i1", tmp)
                elif tipo_l == "string":
                    raise NotImplementedError(
                        "Comparação de string ainda não suportada."
                    )
                else:
                    raise TypeError("Tipo não suportado para comparação.")
            else:
                raise TypeError(
                    "Comparação == só aceita tipos idênticos (exceto sequence) ou note == note."
                )

        # Comparação <, >
        elif op in {"<", ">"}:
            # Verificar se os tipos são compatíveis para comparação
            if tipo_l in {"i32", "double"} and tipo_r in {"i32", "double"}:
                # Se forem tipos mistos, converter int para double
                if tipo_l == "i32" and tipo_r == "double":
                    val_l_cast = f"%cast_l_{self.id}"
                    Code.append(f"{val_l_cast} = sitofp i32 {val_l} to double")
                    cmpop = "olt" if op == "<" else "ogt"
                    Code.append(f"{tmp} = fcmp {cmpop} double {val_l_cast}, {val_r}")
                    return ("i1", tmp)
                elif tipo_l == "double" and tipo_r == "i32":
                    val_r_cast = f"%cast_r_{self.id}"
                    Code.append(f"{val_r_cast} = sitofp i32 {val_r} to double")
                    cmpop = "olt" if op == "<" else "ogt"
                    Code.append(f"{tmp} = fcmp {cmpop} double {val_l}, {val_r_cast}")
                    return ("i1", tmp)
                elif tipo_l == "i32" and tipo_r == "i32":
                    cmpop = "slt" if op == "<" else "sgt"
                    Code.append(f"{tmp} = icmp {cmpop} i32 {val_l}, {val_r}")
                    return ("i1", tmp)
                elif tipo_l == "double" and tipo_r == "double":
                    cmpop = "olt" if op == "<" else "ogt"
                    Code.append(f"{tmp} = fcmp {cmpop} double {val_l}, {val_r}")
                    return ("i1", tmp)
            else:
                raise TypeError(
                    "Comparação < ou > só aceita tipos numéricos (int ou double)."
                )

        # Operações lógicas &&, ||
        elif op in {"&&", "||"}:
            if tipo_l == tipo_r == "i1":
                logicmap = {"&&": "and", "||": "or"}
                Code.append(f"{tmp} = {logicmap[op]} i1 {val_l}, {val_r}")
                return ("i1", tmp)
            else:
                raise TypeError("Operação lógica só aceita bool.")

        else:
            raise NotImplementedError(f"Operador '{op}' não implementado no BinOp.")


class UnOp(Node):
    def evaluate(self, st):
        child_0 = self.children[0].evaluate(st)
        if self.value == "+":
            return ("int", +child_0[1])
        elif self.value == "-":
            return ("int", -child_0[1])
        elif self.value == "!" and child_0[0] == "bool":
            return ("bool", not (child_0[1]))

    def generate(self, st):
        value = self.children[0].generate(st)
        op = self.value

        # value pode ser uma tupla: (tipo, valor_llvm)
        tipo, valor_llvm = value if isinstance(value, tuple) else (None, value)
        tmp = f"%tmp_unop_{self.id}"

        # Operador + (só retorna o valor)
        if op == "+":
            return (tipo, valor_llvm)

        # Operador - (negação aritmética)
        elif op == "-":
            if tipo == "i32":
                Code.append(f"{tmp} = sub i32 0, {valor_llvm}")
                return (tipo, tmp)
            elif tipo == "double":
                Code.append(f"{tmp} = fneg double {valor_llvm}")
                return (tipo, tmp)
            else:
                raise TypeError("O operador - só pode ser usado com int ou double.")

        # Operador ! (not)
        elif op == "!":
            if tipo == "i1":
                Code.append(f"{tmp} = xor i1 {valor_llvm}, true")
                return (tipo, tmp)
            else:
                raise TypeError("O operador ! só pode ser usado com bool.")

        else:
            raise ValueError(f"Operador unário não suportado: {op}")


class NoOp(Node):
    def evaluate(self, st):
        return super().evaluate(st)


class Identifier(Node):
    def evaluate(self, st):
        return st.get(self.value)

    def generate(self, st):
        var_info = st.symbolDict.get(self.value)
        if var_info is None:
            raise ValueError(f"Variável '{self.value}' não declarada.")

        var_type = var_info if isinstance(var_info, str) else var_info[0]

        # Para sequence, retorna o valor salvo na symbol table (AST do sequence)
        if var_type == "sequence":
            return var_info[1]  # AST/nó da sequence

        # Para note (struct): retorna pitch e duration carregados do struct
        if var_type == "note":
            # Gere nomes únicos para cada chamada!
            pitch_ptr = Node.new_tmp(f"{self.value}_pitch_ptr")
            duration_ptr = Node.new_tmp(f"{self.value}_duration_ptr")
            tmp_pitch = Node.new_tmp(f"{self.value}_tmp_pitch")
            tmp_duration = Node.new_tmp(f"{self.value}_tmp_duration")

            Code.append(
                f"{pitch_ptr} = getelementptr %note, %note* %{self.value}, i32 0, i32 0"
            )
            Code.append(f"{tmp_pitch} = load i32, i32* {pitch_ptr}")
            Code.append(
                f"{duration_ptr} = getelementptr %note, %note* %{self.value}, i32 0, i32 1"
            )
            Code.append(f"{tmp_duration} = load double, double* {duration_ptr}")

            return ("note", (tmp_pitch, tmp_duration))

        # Para tipos primitivos: carrega o valor
        llvm_types = {"int": "i32", "double": "double", "bool": "i1"}
        llvm_type = llvm_types.get(var_type)
        tmp = Node.new_tmp(f"{self.value}_val")
        Code.append(f"{tmp} = load {llvm_type}, {llvm_type}* %{self.value}")
        return (llvm_type, tmp)


class Assignment(Node):
    def evaluate(self, st):
        child_0 = self.children[0].value
        child_1 = self.children[1].evaluate(st)
        st.set(child_0, child_1)

    def generate(self, st):
        identifier = self.children[0].value
        var_info = st.symbolDict.get(identifier)

        if var_info is None:
            raise ValueError(f"Variável '{identifier}' não declarada.")

        var_type = (
            var_info if isinstance(var_info, str) else var_info[0]
        )  # obtém o tipo da variável, que pode ser string ou o primeiro elemento da tupla salva na symbol table

        # Assignment para sequence: só atualiza symbol table (não gera código LLVM)
        if var_type == "sequence":
            new_value = self.children[1]
            if not isinstance(new_value, SequenceDec):
                raise TypeError(
                    "Só é possível atribuir uma sequence a uma variável do tipo sequence."
                )
            new_sequence = new_value.generate(st)
            st.symbolDict[identifier] = ("sequence", new_sequence)
            return

        # Assignment para tipos primitivos e note
        value = self.children[1].generate(st)
        if var_type == "note":
            pitch, duration = value[1]
            pitch_ptr = Node.new_tmp(f"{identifier}_pitch_ptr")
            duration_ptr = Node.new_tmp(f"{identifier}_duration_ptr")
            Code.append(
                f"{pitch_ptr} = getelementptr %note, %note* %{identifier}, i32 0, i32 0"
            )
            Code.append(f"store i32 {pitch}, i32* {pitch_ptr}")
            Code.append(
                f"{duration_ptr} = getelementptr %note, %note* %{identifier}, i32 0, i32 1"
            )
            if isinstance(duration, int) or (
                isinstance(duration, str) and duration.isdigit()
            ):
                # Criar uma variável temporária para a conversão
                tmp_float = Node.new_tmp(f"{identifier}_duration_float")
                Code.append(f"{tmp_float} = sitofp i32 {duration} to double")
                # Armazenar a versão convertida
                Code.append(f"store double {tmp_float}, double* {duration_ptr}")
            else:
                # Se já for double, armazenar diretamente
                Code.append(f"store double {duration}, double* {duration_ptr}")
        else:
            llvm_types = {"int": "i32", "double": "double", "bool": "i1"}
            llvm_type = llvm_types.get(var_type)
            Code.append(f"store {llvm_type} {value[1]}, {llvm_type}* %{identifier}")


class Block(Node):
    def evaluate(self, st):
        for child in self.children:
            child.evaluate(st)

    def generate(self, st):
        for child in self.children:
            child.generate(st)


class If(Node):
    def evaluate(self, st):
        child_0 = self.children[0]
        child_1 = self.children[1]
        if child_0.evaluate(st)[0] != "bool":
            raise TypeError(
                f"A condição do 'if' deve ser do tipo bool, mas recebeu {child_0.evaluate(st)[0]}"
            )
        if child_0.evaluate(st)[1]:
            child_1.evaluate(st)
        else:
            if len(self.children) == 3:
                child_2 = self.children[2]
                child_2.evaluate(st)

    def generate(self, st):
        label_then = f"then_{self.id}"
        label_else = f"else_{self.id}"
        label_end = f"endif_{self.id}"

        # Gera o valor da condição (deve ser i1)
        cond = self.children[0].generate(st)
        cond_value = cond[1]

        # Branch condicional para then/else
        Code.append(f"br i1 {cond_value}, label %{label_then}, label %{label_else}")

        # Bloco then
        Code.append(f"{label_then}:")
        self.children[1].generate(st)
        Code.append(f"br label %{label_end}")

        # Bloco else (só se existir)
        Code.append(f"{label_else}:")
        if len(self.children) == 3:
            self.children[2].generate(st)
        Code.append(f"br label %{label_end}")

        # Fim do if
        Code.append(f"{label_end}:")


class IntVal(Node):
    def evaluate(self, st):
        return ("int", self.value)

    def generate(self, st):
        return ("i32", str(self.value))


class DoubleVal(Node):
    def evaluate(self, st):
        return ("double", self.value)

    def generate(self, st):
        return ("double", str(self.value))


class StrVal(Node):
    def evaluate(self, st):
        return ("string", self.value)

    def generate(self, st):
        raise NotImplementedError("Strings não são suportadas na geração de código.")


class BoolVal(Node):
    def evaluate(self, st):
        return ("bool", self.value)

    def generate(self, _st):
        return ("i1", "1" if self.value else "0")


class NoteVal(Node):
    def generate(self, st):
        note_map = {
            "C": 0,
            "C#": 1,
            "Db": 1,
            "D": 2,
            "D#": 3,
            "Eb": 3,
            "E": 4,
            "F": 5,
            "F#": 6,
            "Gb": 6,
            "G": 7,
            "G#": 8,
            "Ab": 8,
            "A": 9,
            "A#": 10,
            "Bb": 10,
            "B": 11,
            "Cb": 11,
            "B#": 0,
        }

        note_name = self.value[0]  # "C4"
        duration = self.value[1]  # 1.0

        pitch = "".join([c for c in note_name if not c.isdigit()])
        oitava = int("".join([c for c in note_name if c.isdigit()]))
        midi_value = note_map[pitch] + (oitava * 12)

        return ("note", (midi_value, duration))


class VarDec(Node):
    def evaluate(self, st):
        child_0 = self.children[0]  # Identificador da variável

        if child_0.value in st.symbolDict:
            raise ValueError(f"Variável '{child_0.value}' já criada")

        if len(self.children) > 1:
            child_1 = self.children[1]
            evaluated = child_1.evaluate(st)
            if self.value != evaluated[0]:
                raise ValueError(
                    f"Erro de atribuição. Tentando atribuir um {evaluated[0]} numa variável {self.value}"
                )
            st.create(child_0.value, (self.value, evaluated[1]))

        else:
            st.create(child_0.value, (self.value, None))

    def generate(self, st):
        identifier = self.children[0].value
        var_type = self.value

        # Mapeamento de tipos da sua linguagem para LLVM
        llvm_types = {
            "int": "i32",
            "double": "double",
            "bool": "i1",
            "note": "%note",
            # "string" e "sequence" vão ser tratados diferente, como conversamos
        }

        if identifier in st.symbolDict:
            raise ValueError(f"Variável '{identifier}' já criada")

        # Para sequence, só salva na symbolTable, não gera código LLVM
        if var_type == "sequence":
            if len(self.children) > 1:
                seq_value = self.children[1].generate(st)
                if not isinstance(self.children[1], SequenceDec):
                    raise TypeError(
                        "Só é possível atribuir uma sequence a uma variável do tipo sequence."
                    )
                st.create(identifier, ("sequence", seq_value))
            else:
                st.create(identifier, ("sequence", None))
            return

        st.create(identifier, var_type)
        # Para os tipos suportados, faz alocação no LLVM
        llvm_type = llvm_types.get(var_type)
        Code.append(f"%{identifier} = alloca {llvm_type}")

        # Se houver valor de inicialização
        if len(self.children) > 1:
            value = self.children[1].generate(st)
            # Para tipo note (struct), value é uma tupla com os dois valores
            if var_type == "note":
                pitch, duration = value[1]
                Code.append(
                    f"%{identifier}_pitch = getelementptr %note, %note* %{identifier}, i32 0, i32 0"
                )
                Code.append(f"store i32 {pitch}, i32* %{identifier}_pitch")
                Code.append(
                    f"%{identifier}_duration = getelementptr %note, %note* %{identifier}, i32 0, i32 1"
                )
                if isinstance(duration, int) or (
                    isinstance(duration, str) and duration.isdigit()
                ):
                    # Criar variável temporária para a conversão
                    tmp_float = Node.new_tmp(f"{identifier}_dur_float")
                    Code.append(f"{tmp_float} = sitofp i32 {duration} to double")
                    # Armazenar a versão convertida
                    Code.append(
                        f"store double {tmp_float}, double* %{identifier}_duration"
                    )
                else:
                    # Se já for double, armazenar diretamente
                    Code.append(
                        f"store double {duration}, double* %{identifier}_duration"
                    )
            else:
                Code.append(f"store {llvm_type} {value[1]}, {llvm_type}* %{identifier}")


class MusicBase(Node):
    def generate(self, st):
        instrumento = self.children[0].value
        instruments_codification = {"piano": 0, "guitar": 1, "violin": 2}
        Code.append(
            f"@instrument = global i32 {instruments_codification.get(instrumento, 0)}, align 4  ; instrument = {instrumento}"
        )
        Code.append("%instrument = load i32, i32* @instrument")

        tempo = self.children[1].generate(st)
        Code.append(
            f"@tempo_base = global i32 {tempo[1]}, align 4  ; tempo_base = {tempo[1]}"
        )
        Code.append("%tempo_base = load i32, i32* @tempo_base")


class Repeat(Node):
    def generate(self, st):
        repeat_count = self.children[0].generate(st)[1]
        if not isinstance(int(repeat_count), int) or int(repeat_count) <= 0:
            raise ValueError("O número de repetições deve ser um inteiro positivo.")

        counter_var = Node.new_tmp("repeat_counter")
        label_cond = f"repeat_cond_{self.id}"
        label_body = f"repeat_body_{self.id}"
        label_exit = f"repeat_exit_{self.id}"

        # Cria variável local para o contador
        Code.append(f"{counter_var} = alloca i32")
        Code.append(f"store i32 0, i32* {counter_var}")

        # Branch para checar condição
        Code.append(f"br label %{label_cond}")
        Code.append(f"{label_cond}:")

        # Carrega valor do contador atual
        current_val = Node.new_tmp("repeat_val")
        Code.append(f"{current_val} = load i32, i32* {counter_var}")

        # Compara contador < limite
        cmp_tmp = Node.new_tmp("repeat_cmp")
        Code.append(f"{cmp_tmp} = icmp slt i32 {current_val}, {repeat_count}")

        # Ramifica para body ou exit
        Code.append(f"br i1 {cmp_tmp}, label %{label_body}, label %{label_exit}")

        # Corpo do loop
        Code.append(f"{label_body}:")
        self.children[1].generate(st)

        # Incrementa o contador
        incr_tmp = Node.new_tmp("repeat_next")
        Code.append(f"{incr_tmp} = add i32 {current_val}, 1")
        Code.append(f"store i32 {incr_tmp}, i32* {counter_var}")

        # Volta para condição
        Code.append(f"br label %{label_cond}")

        # Fim
        Code.append(f"{label_exit}:")


class RepeatWhile(Node):
    def generate(self, st):
        label_cond = f"repeat_while_cond_{self.id}"
        label_body = f"repeat_while_body_{self.id}"
        label_exit = f"repeat_while_exit_{self.id}"

        # Salta para o bloco do loop
        Code.append(f"br label %{label_cond}")

        # Bloco da condição
        Code.append(f"{label_cond}:")
        cond_type, cond_val = self.children[0].generate(st)  # gera código para condição

        # cond_val já é um i1 (bool LLVM), pode usar direto
        Code.append(f"br i1 {cond_val}, label %{label_body}, label %{label_exit}")

        # Corpo do loop
        Code.append(f"{label_body}:")
        self.children[1].generate(st)  # executa o corpo

        # Retorna para verificar a condição novamente
        Code.append(f"br label %{label_cond}")

        # Saída do loop
        Code.append(f"{label_exit}:")


class PauseDuration(Node):
    def generate(self, st):
        duration_type, duration = self.children[0].generate(st)
        if duration_type == "double":

            # void pause_song(double duration, int tempo)
            Code.append(f"call void @pause_song(double {duration}, i32 %tempo_base)")
        elif duration_type == "i32":
            tmp_float = self.temporary_position
            Code.append(f"%{tmp_float} = sitofp i32 {duration} to double")

            # void pause_song(double duration, int tempo)
            Code.append(f"call void @pause_song(double %{tmp_float}, i32 %tempo_base)")
        else:
            raise TypeError("Pause espera um número (int ou double) como duration.")


class SequenceDec(Node):
    def generate(self, st):
        sequence = []
        for child in self.children:
            sequence.append(child)

        return sequence


class PlayNote(Node):
    def generate(self, st):
        note = self.children[0].generate(st)
        if note[0] != "note":
            raise TypeError("PlayNote espera um nó do tipo 'note'.")

        midi_value, duration = note[1]

        if isinstance(duration, int):
            tmp_float = self.temporary_position
            Code.append(f"%{tmp_float} = sitofp i32 {duration} to double")
            duration_param = f"%{tmp_float}"
        else:
            duration_param = str(duration)

        # void play_note(int midi_note, double duration, int instrument, int tempo)
        Code.append(
            f"call void @play_note(i32 {midi_value}, double {duration_param}, i32 %instrument, i32 %tempo_base)"
        )


class PlaySequence(Node):
    def generate(self, st):
        sequence = self.children[0].generate(st)
        if not isinstance(sequence, list):
            raise TypeError("PlaySequence espera uma lista de notas.")

        for child in sequence:
            if isinstance(child, NoteVal):
                PlayNote(value="play_note", children=[child]).generate(st)
            elif isinstance(child, PauseDuration):
                child.generate(st)
            elif isinstance(child, Identifier):
                note = child.generate(st)
                if note[0] == "note":
                    Code.append(
                        f"call void @play_note(i32 {note[1][0]}, double {note[1][1]}, i32 %instrument, i32 %tempo_base)"
                    )
                else:
                    raise TypeError(
                        f"PlaySequence só pode receber nós do tipo 'NoteVal', mas recebeu {note[0]}."
                    )
            else:
                raise TypeError(
                    f"PlaySequence espera um nó do tipo 'NoteVal' ou 'PauseDuration', mas recebeu {type(child).__name__}."
                )
