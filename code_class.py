class Code:
    instructions = []
    global_decls = []  # Declarações globais (variáveis, constantes)

    @staticmethod
    def append(code: str) -> None:
        # Verifica se é uma declaração global (ex: "@var = global ...")
        if code.strip().startswith("@") and ("global" in code or "constant" in code):
            Code.global_decls.append(code)
        else:
            Code.instructions.append(code)

    @staticmethod
    def dump(filename: str) -> None:
        with open(filename, "w") as file:
            # Header LLVM IR — adiciona fmt_float só se precisar
            header = f"""
@.fmt_int = private constant [4 x i8] c"%d\\0A\\00"
@.fmt_float = private constant [4 x i8] c"%f\\0A\\00"
@.format_in = private constant [3 x i8] c"%d\\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
{"\n".join(Code.global_decls)}

; ====== Funções Musicais ======
declare void @play_note(i32, double, i32, i32)  ; (nota MIDI, duração em segundos)
declare void @pause_song(double, i32)           ; (duração em segundos)
declare void @play_sequence(i32*, double*, double*, i32, i32, i32)  ; (array MIDI, array durações, tamanho)

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {{
entry:
"""

            file.write(header + "\n")

            file.write("\n".join(Code.instructions))
            file.write("\n")

            # Footer LLVM IR
            footer = """
  ret i32 0
}
"""
            file.write(footer)
