from code_class import Code

temporary_position = 0


def create_temporary():
    global temporary_position
    temporary_position += 1
    return "tmp" + str(temporary_position)


class Node:
    id = 0

    def generate_id():
        Node.id += 1
        return Node.id

    def __init__(self, value, children):
        self.value = value
        self.children = children
        self.id = Node.generate_id()

    def evaluate(self, st):
        pass

    def generate(self, st):
        pass


class BinOp(Node):
    def evaluate(self, st):
        child_0 = self.children[0].evaluate(st)
        child_1 = self.children[1].evaluate(st)
        if self.value == "+":

            # ============= Operação INT + INT =============#
            if child_0[0] == "int" and child_1[0] == "int":
                return ("int", (child_0[1] + child_1[1]))
            # ==============================================#

            # ============= Operação FLOAT + FLOAT =============#
            elif child_0[0] == "float" and child_1[0] == "float":
                return ("float", child_0[1] + child_1[1])
            # ==================================================#

            # ============= Operação FLOAT + INT =============#
            elif child_0[0] == "float" and child_1[0] == "int":
                return ("float", child_0[1] + float(child_1[1]))

            elif child_0[0] == "int" and child_1[0] == "float":
                return ("float", float(child_0[1]) + child_1[1])
            # ================================================#

            # ============= Operação X + X =============#
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
            # ==========================================#

        # ============= Operação INT - INT =============#
        elif self.value == "-" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] - child_1[1]))
        # ==============================================#

        # ============= Operação FLOAT - FLOAT =============#
        elif self.value == "-" and (child_0[0] == "float" and child_1[0] == "float"):
            return ("float", (child_0[1] - child_1[1]))
        # ==================================================#

        # ============= Operação FLOAT - INT =============#
        elif self.value == "-" and child_0[0] == "float" and child_1[0] == "int":
            return ("float", child_0[1] - float(child_1[1]))
        elif self.value == "-" and child_0[0] == "int" and child_1[0] == "float":
            return ("float", float(child_0[1]) - child_1[1])
        # ================================================#

        # ============= Operação INT * INT =============#
        elif self.value == "*" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] * child_1[1]))
        # ==============================================#

        # ============= Operação FLOAT * FLOAT =============#
        elif self.value == "*" and (child_0[0] == "float" and child_1[0] == "float"):
            return ("float", (child_0[1] * child_1[1]))
        # ==================================================#

        # ============= Operação FLOAT * INT =============#
        elif self.value == "*" and child_0[0] == "float" and child_1[0] == "int":
            return ("float", child_0[1] * float(child_1[1]))
        elif self.value == "*" and child_0[0] == "int" and child_1[0] == "float":
            return ("float", float(child_0[1]) * child_1[1])
        # ================================================#

        # ============= Verificação divisão por zero =============#
        elif self.value == "/":
            if child_1[1] == 0:
                raise ZeroDivisionError("Divisão por zero!")
        # ========================================================#

        # ============= Operação INT / INT =============#
        elif self.value == "/" and (child_0[0] == "int" and child_1[0] == "int"):
            return ("int", (child_0[1] // child_1[1]))
        # ==============================================#

        # ============= Operação FLOAT / FLOAT =============#
        elif self.value == "/" and (child_0[0] == "float" and child_1[0] == "float"):
            return ("float", (child_0[1] / child_1[1]))
        # ==================================================#

        # ============= Operação FLOAT / INT =============#
        elif self.value == "/" and child_0[0] == "float" and child_1[0] == "int":
            return ("float", child_0[1] / float(child_1[1]))
        elif self.value == "/" and child_0[0] == "int" and child_1[0] == "float":
            return ("float", float(child_0[1]) / child_1[1])
        # ================================================#

        elif self.value == ">":
            if (child_0[0] == "float" and child_1[0] == "int") or (
                child_0[0] == "int" and child_1[0] == "float"
            ):
                return ("bool", float(child_0[1]) > float(child_1[1]))
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            return ("bool", (child_0[1] > child_1[1]))

        elif self.value == "<":
            if (child_0[0] == "float" and child_1[0] == "int") or (
                child_0[0] == "int" and child_1[0] == "float"
            ):
                return ("bool", float(child_0[1]) < float(child_1[1]))
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            return ("bool", (child_0[1] < child_1[1]))

        elif self.value == "==":
            if (child_0[0] == "float" and child_1[0] == "int") or (
                child_0[0] == "int" and child_1[0] == "float"
            ):
                resultado = abs(float(child_0[1]) - float(child_1[1])) < 1e-9
                return ("bool", resultado)
            if child_0[0] != child_1[0]:
                raise TypeError(
                    f"Erro de tipo: Não é possível comparar '{child_0[0]}' com '{child_1[0]}'"
                )
            if child_0[0] == "float" and child_1[0] == "float":
                resultado = abs(child_0[1] - child_1[1]) < 1e-9
                return ("bool", resultado)
            else:
                return ("bool", (child_0[1] == child_1[1]))

        elif self.value == "&&" and (child_0[0] == "bool" and child_1[0] == "bool"):
            return ("bool", (child_0[1] & child_1[1]))

        elif self.value == "||" and (child_0[0] == "bool" and child_1[0] == "bool"):
            return ("bool", (child_0[1] | child_1[1]))

    def generate(self, st):
        left, left_type = self.children[0].generate(st)
        right, right_type = self.children[1].generate(st)

        # ============= OPERAÇÕES ARITMÉTICAS =============#
        if self.value in ["+", "-", "*", "/"]:
            # Verificar se ambos os tipos são numéricos (i32 ou float)
            if (left_type not in ["i32", "float"]) or (
                right_type not in ["i32", "float"]
            ):
                raise TypeError(f"Operador '{self.value}' requer operandos numéricos")

            # Conversão implícita: se qualquer lado for float, converte ambos para float
            if left_type == "float" and right_type != "float":
                tmp_conv = create_temporary()
                Code.append(f"%{tmp_conv} = sitofp i32 {right} to float")
                right = f"%{tmp_conv}"
                right_type = "float"
            elif right_type == "float" and left_type != "float":
                tmp_conv = create_temporary()
                Code.append(f"%{tmp_conv} = sitofp i32 {left} to float")
                left = f"%{tmp_conv}"
                left_type = "float"

            result_type = (
                "float" if (left_type == "float" or right_type == "float") else "i32"
            )

            # Operações específicas
            tmp = create_temporary()

            if self.value == "+":
                op = "fadd" if result_type == "float" else "add"
                Code.append(f"%{tmp} = {op} {result_type} {left}, {right}")
            elif self.value == "-":
                op = "fsub" if result_type == "float" else "sub"
                Code.append(f"%{tmp} = {op} {result_type} {left}, {right}")
            elif self.value == "*":
                op = "fmul" if result_type == "float" else "mul"
                Code.append(f"%{tmp} = {op} {result_type} {left}, {right}")
            elif self.value == "/":
                # Não há verificação de divisão por zero em tempo de compilação em LLVM
                op = "fdiv" if result_type == "float" else "sdiv"
                Code.append(f"%{tmp} = {op} {result_type} {left}, {right}")

            return f"%{tmp}", result_type

        # ============= OPERAÇÕES DE COMPARAÇÃO =============#
        elif self.value in [">", "<", "=="]:
            if left_type == "i1" or right_type == "i1":
                if left_type != right_type:
                    raise TypeError(
                        f"Não é possível comparar '{left_type}' com '{right_type}'"
                    )

                # Comparação de booleanos
                tmp = create_temporary()
                if self.value == "==":
                    Code.append(f"%{tmp} = icmp eq i1 {left}, {right}")
                else:
                    raise TypeError(
                        f"Operação '{self.value}' não suportada entre booleanos"
                    )

            # Comparação de tipos numéricos
            elif left_type in ["i32", "float"] and right_type in ["i32", "float"]:
                # Converter para float se um dos operandos for float
                if left_type == "float" and right_type != "float":
                    tmp_conv = create_temporary()
                    Code.append(f"%{tmp_conv} = sitofp i32 {right} to float")
                    right = f"%{tmp_conv}"
                    right_type = "float"
                elif right_type == "float" and left_type != "float":
                    tmp_conv = create_temporary()
                    Code.append(f"%{tmp_conv} = sitofp i32 {left} to float")
                    left = f"%{tmp_conv}"
                    left_type = "float"

                result_type = (
                    "float"
                    if (left_type == "float" or right_type == "float")
                    else "i32"
                )

                tmp = create_temporary()
                if result_type == "float":
                    if self.value == "==":
                        Code.append(f"%{tmp} = fcmp oeq float {left}, {right}")
                    elif self.value == ">":
                        Code.append(f"%{tmp} = fcmp ogt float {left}, {right}")
                    elif self.value == "<":
                        Code.append(f"%{tmp} = fcmp olt float {left}, {right}")
                else:
                    if self.value == "==":
                        Code.append(f"%{tmp} = icmp eq i32 {left}, {right}")
                    elif self.value == ">":
                        Code.append(f"%{tmp} = icmp sgt i32 {left}, {right}")
                    elif self.value == "<":
                        Code.append(f"%{tmp} = icmp slt i32 {left}, {right}")

            elif (left_type == "note" and right_type == "note") and self.value == "==":
                if isinstance(self.children[0], Identifier):
                    left_data = st.get(self.children[0].value)
                    left_midi = create_temporary()
                    left_dur = create_temporary()
                    Code.append(f"%{left_midi} = load i32, i32* {left_data['llvm']}")
                    Code.append(
                        f"%{left_dur} = load double, double* {left_data['llvm_dur']}"
                    )
                else:
                    note_str, _ = self.children[0].generate(st)
                    midi_str, dur_str = note_str.split("_")[1:]
                    left_midi = midi_str
                    left_dur = f"{float(dur_str):.3f}"

                if isinstance(self.children[1], Identifier):
                    right_data = st.get(self.children[1].value)
                    right_midi = create_temporary()
                    right_dur = create_temporary()
                    Code.append(f"%{right_midi} = load i32, i32* {right_data['llvm']}")
                    Code.append(
                        f"%{right_dur} = load double, double* {right_data['llvm_dur']}"
                    )
                else:
                    note_str, _ = self.children[1].generate(st)
                    midi_str, dur_str = note_str.split("_")[1:]
                    right_midi = midi_str
                    right_dur = f"{float(dur_str):.3f}"

                cmp_midi = create_temporary()
                if left_midi.isdigit():
                    left_midi_str = left_midi
                else:
                    left_midi_str = f"%{left_midi}"

                if right_midi.isdigit():
                    right_midi_str = right_midi
                else:
                    right_midi_str = f"%{right_midi}"
                Code.append(
                    f"%{cmp_midi} = icmp eq i32 {left_midi_str}, {right_midi_str}"
                )

                if left_midi.isdigit():
                    left_dur_str = left_midi
                else:
                    left_dur_str = f"%{left_midi}"

                if right_midi.isdigit():
                    right_dur_str = right_midi
                else:
                    right_dur_str = f"%{right_midi}"

                if left_dur_str.startswith("%"):
                    tmp = create_temporary()
                    Code.append(f"%{tmp} = sitofp i32 {left_dur_str} to double")
                    left_dur_str = f"%{tmp}"
                else:
                    left_dur_str = f"{float(left_dur_str):.3f}"

                if right_dur_str.startswith("%"):
                    tmp = create_temporary()
                    Code.append(f"%{tmp} = sitofp i32 {right_dur_str} to double")
                    right_dur_str = f"%{tmp}"
                else:
                    right_dur_str = f"{float(right_dur_str):.3f}"

                cmp_dur = create_temporary()
                Code.append(
                    f"%{cmp_dur} = fcmp oeq double {left_dur_str}, {right_dur_str}"
                )
                tmp = create_temporary()
                Code.append(f"%{tmp} = and i1 %{cmp_midi}, %{cmp_dur}")

            else:
                raise TypeError(
                    f"Não é possível comparar '{left_type}' com '{right_type}'"
                )

            return f"%{tmp}", "i1"

        # ============= OPERAÇÕES LÓGICAS =============#
        elif self.value in ["&&", "||"]:
            if left_type != "i1" or right_type != "i1":
                raise TypeError(f"Operador '{self.value}' requer operandos booleanos")

            tmp = create_temporary()
            if self.value == "&&":
                Code.append(f"%{tmp} = and i1 {left}, {right}")
            elif self.value == "||":
                Code.append(f"%{tmp} = or i1 {left}, {right}")

            return f"%{tmp}", "i1"

        else:
            raise NotImplementedError(f"Operador '{self.value}' não suportado.")


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
        value_tmp, value_type = self.children[0].generate(st)

        if self.value == "+":
            return value_tmp, value_type

        elif self.value == "-":
            tmp = create_temporary()
            if value_type == "i32":
                Code.append(f"%{tmp} = sub i32 0, {value_tmp}")
            elif value_type == "float":
                Code.append(f"%{tmp} = fsub float 0.0, {value_tmp}")
            else:
                raise TypeError(f"Operador '-' não suportado para tipo {value_type}")
            return f"%{tmp}", value_type

        elif self.value == "!":
            if value_type != "i1":
                raise TypeError(
                    f"Operador '!' só é válido para booleanos, recebeu {value_type}"
                )
            tmp = create_temporary()
            Code.append(f"%{tmp} = xor i1 {value_tmp}, true")  # inverte o bit
            return f"%{tmp}", "i1"

        else:
            raise NotImplementedError(f"Operador unário '{self.value}' não suportado.")


class NoOp(Node):
    def evaluate(self, st):
        return super().evaluate(st)


class Identifier(Node):
    def evaluate(self, st):
        return st.get(self.value)

    def generate(self, st):
        data = st.get(self.value)
        tmp = create_temporary()
        if data["type"] == "float":
            data_type = "double"
            Code.append(f"%{tmp} = load {data_type}, {data_type}* {data["llvm"]}")
        if data["type"] == "note":
            data_type = "i32"
            Code.append(f"%{tmp} = load {data_type}, {data_type}* {data["llvm"]}")
        else:
            Code.append(f"%{tmp} = load {data["type"]}, {data["type"]}* {data["llvm"]}")
        return f"%{tmp}", data["type"]


class Assignment(Node):
    def evaluate(self, st):
        child_0 = self.children[0].value
        child_1 = self.children[1].evaluate(st)
        st.set(child_0, child_1)

    def generate(self, st):
        identifier = self.children[0].value
        data = st.get(identifier)
        reg_valor, value_type = self.children[1].generate(st)  # Mantido!

        if data["type"] == "sequence" and not (value_type.startswith("seq_")):
            raise TypeError(
                f"Tipo incompatível: esperado sequence, recebeu {value_type}"
            )
        elif data["type"] != "sequence" and data["type"] != value_type:
            raise TypeError(f"Tipo incompatível: {data['type']} vs {value_type}")

        # Se for uma nota, reg_valor será "note_60_1.0"
        if value_type == "note":
            midi, duration = reg_valor.split("_")[1:]
            Code.append(f"store i32 {midi}, i32* {data['llvm']}")
            Code.append(f"store double {float(duration)}, double* {data['llvm_dur']}")
        elif data["type"] == "sequence":
            midi_str = reg_valor if reg_valor.startswith("seq_midi:") else None
            dur_str = value_type if value_type.startswith("seq_dur:") else None

            if not midi_str or not dur_str:
                raise ValueError("Erro ao atribuir sequência: dados malformados.")

            midi_vals = midi_str.split("[")[1].split("]")[0].split(",")
            dur_vals = dur_str.split("[")[1].split("]")[0].split(",")

            size = len(midi_vals)
            if size != len(dur_vals):
                raise ValueError(
                    "Sequência com tamanhos diferentes de notas e durações."
                )

            for i in range(size):
                Code.append(
                    f"store i32 {midi_vals[i]}, "
                    f"i32* getelementptr ([{size} x i32], [{size} x i32]* {data['llvm']}, i32 0, i32 {i})"
                )
                if dur_vals[i].startswith("%"):
                    dur_val_str = dur_vals[i]
                else:
                    dur_val_str = f"{float(dur_vals[i]):.3f}"

                Code.append(
                    f"store double {dur_val_str}, "
                    f"double* getelementptr ([{size} x double], [{size} x double]* {data['llvm_dur_arr']}, i32 0, i32 {i})"
                )
        else:
            # Comportamento original para outros tipos
            Code.append(
                f"store {data['type']} {reg_valor}, {data['type']}* {data['llvm']}"
            )


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
        cond_val, cond_type = self.children[0].generate(st)

        if cond_type != "i1":
            raise TypeError(
                f"A condição do 'if' deve ser booleana (i1), mas recebeu '{cond_type}'"
            )

        label_then = f"then_{self.id}"
        label_else = f"else_{self.id}"
        label_exit = f"endif_{self.id}"

        # Verificação condicional
        Code.append(f"br i1 {cond_val}, label %{label_then}, label %{label_else}")

        # Corpo
        Code.append(f"{label_then}:")
        self.children[1].generate(st)
        Code.append(f"br label %{label_exit}")

        # Else
        Code.append(f"{label_else}:")
        if len(self.children) == 3:
            self.children[2].generate(st)
        Code.append(f"br label %{label_exit}")

        Code.append(f"{label_exit}:")


class IntVal(Node):
    def evaluate(self, st):
        return ("int", self.value)

    def generate(self, st):
        return str(self.value), "i32"


class FloatVal(Node):
    def evaluate(self, st):
        return ("float", self.value)

    def generate(self, st):
        return str(self.value), "float"


class StrVal(Node):
    def evaluate(self, st):
        return ("string", self.value)

    def generate(self, st):
        raise NotImplementedError("Strings não são suportadas na geração de código.")


class BoolVal(Node):
    def evaluate(self, st):
        return ("bool", self.value)

    def generate(self, _st):
        return "1" if self.value else "0", "i1"


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

        if identifier in st.symbolDict:
            raise ValueError(f"Variável '{identifier}' já existe")

        # --- Tipos Primitivos (int, float, bool) ---
        if var_type in ["int", "float", "bool"]:
            llvm_type = {"int": "i32", "float": "double", "bool": "i1"}[var_type]

            var_alloca = f"%{identifier}"
            Code.append(f"{var_alloca} = alloca {llvm_type}")
            st.create(identifier, {"llvm": var_alloca, "type": llvm_type})

            # Inicialização (se houver)
            if len(self.children) > 1:
                value_tmp, value_type = self.children[1].generate(st)

                if llvm_type != value_type:
                    raise TypeError(
                        f"Tipo da variável '{identifier}' é {llvm_type}, mas valor inicial é {value_type}"
                    )

                if llvm_type in ["i32", "double", "i1"]:
                    Code.append(
                        f"store {llvm_type} {value_tmp}, {llvm_type}* {var_alloca}"
                    )

        # --- Tipo Note ---
        elif var_type == "note":
            # Aloca espaço para MIDI e duração
            Code.append(f"%{identifier}_midi = alloca i32")
            Code.append(f"%{identifier}_dur = alloca double")

            if len(self.children) > 1 and not isinstance(self.children[1], Note):
                raise TypeError(
                    f"Esperado tipo 'note', obtido {type(self.children[1]).__name__}"
                )

            # Se houver inicialização
            if len(self.children) > 1:
                note_str, _ = self.children[1].generate(st)  # Ex: "note_60_1.0"
                midi, duration = note_str.split("_")[1:]  # Extrai 60 e 1.0
                Code.append(f"store i32 {midi}, i32* %{identifier}_midi")
                Code.append(
                    f"store double {float(duration)}, double* %{identifier}_dur"
                )

            st.create(
                identifier,
                {
                    "llvm": f"%{identifier}_midi",
                    "llvm_dur": f"%{identifier}_dur",
                    "type": "note",
                },
            )

        # --- Tipo Sequence ---
        elif var_type == "sequence":
            # Aloca arrays globais para MIDI e durações
            seq_size = len(self.children[1].children) if len(self.children) > 1 else 0
            Code.append(
                f"@{identifier}_midi = global [{seq_size} x i32] zeroinitializer"
            )
            Code.append(
                f"@{identifier}_dur = global [{seq_size} x double] zeroinitializer"
            )

            # Se houver inicialização
            if len(self.children) > 1:
                for i, note_node in enumerate(self.children[1].children):
                    if isinstance(note_node, Identifier):
                        # Carrega de variável existente
                        var_data = st.get(note_node.value)
                        tmp_midi = create_temporary()
                        tmp_dur = create_temporary()
                        Code.append(f"%{tmp_midi} = load i32, i32* {var_data['llvm']}")
                        Code.append(
                            f"%{tmp_dur} = load double, double* {var_data['llvm_dur']}"
                        )
                        Code.append(
                            f"store i32 %{tmp_midi}, i32* getelementptr ([{seq_size} x i32], [{seq_size} x i32]* @{identifier}_midi, i32 0, i32 {i})"
                        )
                        Code.append(
                            f"store double %{tmp_dur}, double* getelementptr ([{seq_size} x double], [{seq_size} x double]* @{identifier}_dur, i32 0, i32 {i})"
                        )
                    else:
                        # Nota direta
                        note_str, _ = note_node.generate(st)  # ex.: "note_52_1"
                        midi_str, dur_str = note_str.split("_")[1:]  # ["52", "1"]

                        Code.append(
                            f"store i32 {midi_str}, "
                            f"i32* getelementptr ([{seq_size} x i32], "
                            f"[{seq_size} x i32]* @{identifier}_midi, i32 0, i32 {i})"
                        )
                        Code.append(
                            f"store double {float(dur_str)}, "
                            f"double* getelementptr ([{seq_size} x double], "
                            f"[{seq_size} x double]* @{identifier}_dur, i32 0, i32 {i})"
                        )

            st.create(
                identifier,
                {
                    "llvm": f"@{identifier}_midi",
                    "llvm_dur_arr": f"@{identifier}_dur",
                    "size": seq_size,
                    "type": "sequence",
                },
            )

        else:
            raise TypeError(f"Tipo '{var_type}' não suportado")


class PlayNote(Node):
    def generate(self, st):
        # Se for uma nota direta (ex: play_note note C4 duration 1.5)
        if isinstance(self.children[0], Note):
            midi_value, _ = self.children[0].generate(st)
            duration = self.children[0].children[1].value
            midi_value = midi_value.split("_")
            duration = float(duration)
            formatted_val = f"{duration:.3f}"
            Code.append(
                f"call void @play_note(i32 {midi_value[1]}, double {formatted_val}, i32 %instrument, i32 %tempo_base)"
            )

        # Se for uma variável (ex: play_note nota_fav)
        else:
            var_name = self.children[0].value
            var_data = st.get(var_name)

            # Carrega MIDI e duração
            tmp_midi = create_temporary()
            tmp_dur = create_temporary()
            Code.append(f"%{tmp_midi} = load i32, i32* {var_data['llvm']}")
            Code.append(f"%{tmp_dur} = load double, double* {var_data['llvm_dur']}")

            Code.append(
                f"call void @play_note(i32 %{tmp_midi}, double %{tmp_dur}, i32 %instrument, i32 %tempo_base)"
            )


class PlaySequence(Node):
    def generate(self, st):
        # Pode receber Sequence diretamente ou Identifier
        if isinstance(self.children[0], Sequence):
            # Sequência direta (não armazenada em variável)
            midi_str, dur_str = self.children[0].generate(st)
            # Extrai valores das strings
            midi_values = midi_str.split("[")[1].split("]")[0].split(",")
            dur_values = dur_str.split("[")[1].split("]")[0].split(",")

            # Aloca arrays temporários
            tmp_midi_arr = create_temporary()
            tmp_dur_arr = create_temporary()
            size = len(midi_values)

            Code.append(f"%{tmp_midi_arr} = alloca [{size} x i32]")
            Code.append(f"%{tmp_dur_arr} = alloca [{size} x double]")

            # Preenche arrays
            for i in range(size):
                # ponteiro para a posição i do array MIDI
                gep_m = create_temporary()
                Code.append(
                    f"%{gep_m} = getelementptr [{size} x i32], "
                    f"[{size} x i32]* %{tmp_midi_arr}, i32 0, i32 {i}"
                )
                if midi_values[i].startswith("%"):  # veio de variável
                    Code.append(f"store i32 {midi_values[i]}, i32* %{gep_m}")
                else:  # é número literal
                    Code.append(f"store i32 {midi_values[i]}, i32* %{gep_m}")

                # ponteiro para a posição i do array de durações
                gep_d = create_temporary()
                Code.append(
                    f"%{gep_d} = getelementptr [{size} x double], "
                    f"[{size} x double]* %{tmp_dur_arr}, i32 0, i32 {i}"
                )
                if not (dur_values[i].startswith("%")):
                    formatted_val = f"{float(dur_values[i]):.3f}"
                    Code.append(f"store double {formatted_val}, double* %{gep_d}")
                else:

                    Code.append(f"store double {dur_values[i]}, double* %{gep_d}")

            # Chama play_sequence
            arr_ptr = create_temporary()
            Code.append(
                f"%{arr_ptr} = getelementptr [{size} x i32], [{size} x i32]* %{tmp_midi_arr}, i32 0, i32 0"
            )
            dur_ptr = create_temporary()
            Code.append(
                f"%{dur_ptr} = getelementptr [{size} x double], [{size} x double]* %{tmp_dur_arr}, i32 0, i32 0"
            )

            Code.append(
                f"call void @play_sequence(i32* %{arr_ptr}, double* %{dur_ptr}, i32 {size}, i32 %instrument, i32 %tempo_base)"
            )

        else:
            # Variável contendo sequência
            var_name = self.children[0].value
            var_data = st.get(var_name)

            midi_ptr = create_temporary()
            Code.append(
                f"%{midi_ptr} = getelementptr [{var_data['size']} x i32], [{var_data['size']} x i32]* {var_data['llvm']}, i32 0, i32 0"
            )

            dur_ptr = create_temporary()
            Code.append(
                f"%{dur_ptr} = getelementptr [{var_data['size']} x float], [{var_data['size']} x float]* {var_data['llvm_dur_arr']}, i32 0, i32 0"
            )

            Code.append(
                f"call void @play_sequence(i32* %{midi_ptr}, float* %{dur_ptr}, i32 {var_data['size']}, i32 %instrument, i32 %tempo_base)"
            )


class Pause(Node):
    def generate(self, st):
        value_tmp, value_type = self.children[0].generate(st)
        if value_type == "float":
            Code.append(f"call void @pause_song(double {value_tmp}, i32 %tempo_base)")
        elif value_type == "i32":
            tmp_float = create_temporary()
            Code.append(f"%{tmp_float} = sitofp i32 {value_tmp} to double")
            Code.append(f"call void @pause_song(double %{tmp_float}, i32 %tempo_base)")
        else:
            raise TypeError("Pause espera um número (int ou float)")


class Note(Node):
    def generate(self, st):
        note_map = {
            "C": 0,
            "C#": 1,
            "D": 2,
            "D#": 3,
            "E": 4,
            "F": 5,
            "F#": 6,
            "G": 7,
            "G#": 8,
            "A": 9,
            "A#": 10,
            "B": 11,
        }

        note_name = self.children[0].value  # "C4"
        duration = self.children[1].value  # 1.0

        pitch = "".join([c for c in note_name if not c.isdigit()])
        oitava = int("".join([c for c in note_name if c.isdigit()]))
        midi_value = note_map[pitch] + (oitava * 12)

        # Retorna um valor "fake" que carrega MIDI e duração
        return f"note_{midi_value}_{duration}", "note"  # Ex: ("note_60_1.0", "note")


class Sequence(Node):
    def generate(self, st):
        # Gera arrays para MIDI e durações
        midi_values = []
        dur_values = []

        for note_node in self.children:
            if isinstance(note_node, Identifier):
                # Se for variável, carrega seus valores
                var_data = st.get(note_node.value)
                tmp_midi = create_temporary()
                tmp_dur = create_temporary()
                Code.append(f"%{tmp_midi} = load i32, i32* {var_data['llvm']}")
                Code.append(f"%{tmp_dur} = load double, double* {var_data['llvm_dur']}")
                midi_values.append(f"%{tmp_midi}")
                dur_values.append(f"%{tmp_dur}")
            else:  # nota direta
                note_str, _ = note_node.generate(st)  # "note_48_0.5"
                midi_val, dur_val = note_str.split("_")[1:]  # ["48", "0.5"]

                midi_values.append(midi_val)  # agora é "48"
                dur_values.append(dur_val)

        # Retorna os arrays como strings especiais
        return (
            f"seq_midi:[{','.join(midi_values)}]",
            f"seq_dur:[{','.join(dur_values)}]",
        )


class Repeat(Node):
    def generate(self, st):
        # Gera valor do contador (quantas vezes repetir)
        count_tmp, count_type = self.children[0].generate(st)
        if count_type != "i32":
            raise TypeError("Repeat espera inteiro como contador")

        counter_var = create_temporary()
        label_cond = f"repeat_cond_{self.id}"
        label_body = f"repeat_body_{self.id}"
        label_exit = f"repeat_exit_{self.id}"

        # Cria variável local para o contador
        Code.append(f"%{counter_var} = alloca i32")
        Code.append(f"store i32 0, i32* %{counter_var}")

        # Branch para checar condição
        Code.append(f"br label %{label_cond}")
        Code.append(f"{label_cond}:")

        # Carrega valor do contador atual
        current_val = create_temporary()
        Code.append(f"%{current_val} = load i32, i32* %{counter_var}")

        # Compara contador < limite
        cmp_tmp = create_temporary()
        Code.append(f"%{cmp_tmp} = icmp slt i32 %{current_val}, {count_tmp}")

        # Ramifica para body ou exit
        Code.append(f"br i1 %{cmp_tmp}, label %{label_body}, label %{label_exit}")

        # Corpo do loop
        Code.append(f"{label_body}:")
        self.children[1].generate(st)

        # Incrementa o contador
        incr_tmp = create_temporary()
        Code.append(f"%{incr_tmp} = add i32 %{current_val}, 1")
        Code.append(f"store i32 %{incr_tmp}, i32* %{counter_var}")

        # Volta para condição
        Code.append(f"br label %{label_cond}")

        # Fim
        Code.append(f"{label_exit}:")


class RepeatWhile(Node):
    def generate(self, st):
        max_tmp, max_type = self.children[0].generate(st)
        if max_type != "i32":
            raise TypeError("RepeatWhile espera inteiro como máximo")

        counter_var = create_temporary()
        label_cond = f"repeatwhile_cond_{self.id}"
        label_body = f"repeatwhile_body_{self.id}"
        label_exit = f"repeatwhile_exit_{self.id}"

        # Cria variável local para o contador
        Code.append(f"%{counter_var} = alloca i32")
        Code.append(f"store i32 0, i32* %{counter_var}")

        # Branch para checar condição
        Code.append(f"br label %{label_cond}")
        Code.append(f"{label_cond}:")

        # Carrega valor do contador atual
        current_val = create_temporary()
        Code.append(f"%{current_val} = load i32, i32* %{counter_var}")

        # Compara contador < máximo
        cmp_cnt = create_temporary()
        Code.append(f"%{cmp_cnt} = icmp slt i32 %{current_val}, {max_tmp}")

        # Avalia condição booleana do usuário
        cond_tmp, cond_type = self.children[1].generate(st)
        if cond_type != "i1":
            raise TypeError(
                "RepeatWhile espera condicional booleana no segundo argumento"
            )

        # AND lógico das duas condições (contador < máximo && condição)
        and_tmp = create_temporary()
        Code.append(f"%{and_tmp} = and i1 %{cmp_cnt}, {cond_tmp}")

        # Ramifica para body ou exit
        Code.append(f"br i1 %{and_tmp}, label %{label_body}, label %{label_exit}")

        # Corpo do loop
        Code.append(f"{label_body}:")
        self.children[2].generate(st)

        # Incrementa contador
        incr_tmp = create_temporary()
        Code.append(f"%{incr_tmp} = add i32 %{current_val}, 1")
        Code.append(f"store i32 %{incr_tmp}, i32* %{counter_var}")

        # Volta para condição
        Code.append(f"br label %{label_cond}")

        # Fim
        Code.append(f"{label_exit}:")


class Instrument(Node):
    def generate(self, st):
        instruments_codification = {"piano": 0, "guitar": 1, "violin": 2}
        Code.append(
            f"@instrument = global i32 {instruments_codification.get(self.value, 0)}, align 4  ; instrument = {self.value}"
        )
        Code.append("%instrument = load i32, i32* @instrument")
        return ""


class Tempo(Node):
    def generate(self, st):
        tempo = self.children[0].generate(st)
        Code.append(
            f"@tempo_base = global i32 {tempo[0]}, align 4  ; tempo_base = {tempo[0]}"
        )
        Code.append("%tempo_base = load i32, i32* @tempo_base")
        return ""


class MusicBase(Node):
    def generate(self, st):
        for child in self.children:
            child.generate(st)
