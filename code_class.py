class Code:
    instructions = []
    global_instructions = []

    @staticmethod
    def append(code: str) -> None:
        if code.strip().startswith("@") and "= global" in code:
            Code.global_instructions.append(code)
        else:
            Code.instructions.append(code)

    @staticmethod
    def dump(filename: str) -> None:
        with open(filename, "w") as file:
            # Escrever cabeçalho
            header = f"""
@.fmt_int = private constant [4 x i8] c"%d\\0A\\00"
@.fmt_float = private constant [4 x i8] c"%f\\0A\\00"
@.format_in = private constant [3 x i8] c"%d\\00"

@scan_int = common global i32 0, align 4

; ====== Funções Musicais ======
declare void @play_note(i32, double, i32, i32)  ; (nota MIDI, duração em segundos)
declare void @pause_song(double, i32)           ; (duração em segundos)

; ====== Structs ======
%note = type {{ i32, double }}
"""
            file.write(header + "\n")

            # Escrever instruções globais
            if Code.global_instructions:
                file.write("; ====== Variáveis Globais ======\n")
                file.write("\n".join(Code.global_instructions))
                file.write("\n\n")

            # Declarações de funções externas
            file.write("declare i32 @printf(i8*, ...)\n")
            file.write("declare i32 @scanf(i8*, ...)\n\n")

            # Início da função main
            file.write("define i32 @main() {\n")
            file.write("entry:\n\n")

            # Escrever corpo da função main
            file.write("\n".join(Code.instructions) + "\n")

            # Escrever Footer
            footer = """
  ret i32 0
}
"""

            file.write("\n" + footer)
