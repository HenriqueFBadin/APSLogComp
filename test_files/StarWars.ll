
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Funções Musicais ======
declare void @play_note(i32, double, i32, i32)  ; (nota MIDI, duração em segundos)
declare void @pause_song(double, i32)           ; (duração em segundos)

; ====== Structs ======
%note = type { i32, double }

; ====== Variáveis Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 120, align 4  ; tempo_base = 120

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:

%instrument = load i32, i32* @instrument
%tempo_base = load i32, i32* @tempo_base
%repeat_counter1 = alloca i32
store i32 0, i32* %repeat_counter1
br label %repeat_cond_57
repeat_cond_57:
%repeat_val2 = load i32, i32* %repeat_counter1
%repeat_cmp3 = icmp slt i32 %repeat_val2, 3
br i1 %repeat_cmp3, label %repeat_body_57, label %repeat_exit_57
repeat_body_57:
call void @play_note(i32 40, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%repeat_next4 = add i32 %repeat_val2, 1
store i32 %repeat_next4, i32* %repeat_counter1
br label %repeat_cond_57
repeat_exit_57:
call void @play_note(i32 45, double 0.75, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
call void @play_note(i32 52, double 0.75, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%repeat_counter5 = alloca i32
store i32 0, i32* %repeat_counter5
br label %repeat_cond_67
repeat_cond_67:
%repeat_val6 = load i32, i32* %repeat_counter5
%repeat_cmp7 = icmp slt i32 %repeat_val6, 2
br i1 %repeat_cmp7, label %repeat_body_67, label %repeat_exit_67
repeat_body_67:
call void @play_note(i32 50, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 49, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 47, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 57, double 1.0, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.75, i32 %tempo_base)
call void @play_note(i32 52, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%repeat_next8 = add i32 %repeat_val6, 1
store i32 %repeat_next8, i32* %repeat_counter5
br label %repeat_cond_67
repeat_exit_67:
call void @play_note(i32 50, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 49, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 50, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
call void @play_note(i32 47, double 0.75, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)


  ret i32 0
}
