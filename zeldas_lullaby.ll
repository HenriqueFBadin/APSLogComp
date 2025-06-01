
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 60, align 4  ; tempo_base = 60

; ====== Funções Musicais ======
declare void @play_note(i32, float, i32, i32)  ; (nota MIDI, duração em segundos)
declare void @pause_song(float, i32)           ; (duração em segundos)
declare void @play_sequence(i32*, float*, i32, i32, i32)  ; (array MIDI, array durações, tamanho)

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:

%instrument = load i32, i32* @instrument
%tempo_base = load i32, i32* @tempo_base
%repetitions = alloca i32
store i32 0, i32* %repetitions
%tmp1 = alloca i32
store i32 0, i32* %tmp1
br label %repeat_cond_59
repeat_cond_59:
%tmp2 = load i32, i32* %tmp1
%tmp3 = icmp slt i32 %tmp2, 2
br i1 %tmp3, label %repeat_body_59, label %repeat_exit_59
repeat_body_59:
call void @play_note(i32 52, double 0.500, i32 %instrument, i32 %tempo_base)
call void @play_note(i32 55, double 0.500, i32 %instrument, i32 %tempo_base)
call void @play_note(i32 50, double 1.000, i32 %instrument, i32 %tempo_base)
%tmp4 = load i32, i32* %repetitions
%tmp5 = add i32 %tmp4, 1
store i32 %tmp5, i32* %repetitions
call void @pause_song(double 0.75, i32 %tempo_base)
%tmp6 = load i32, i32* %repetitions
%tmp7 = icmp eq i32 %tmp6, 2
br i1 %tmp7, label %then_58, label %else_58
then_58:
call void @play_note(i32 52, double 0.500, i32 %instrument, i32 %tempo_base)
call void @play_note(i32 55, double 0.500, i32 %instrument, i32 %tempo_base)
call void @play_note(i32 62, double 1.000, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.6, i32 %tempo_base)
call void @play_note(i32 60, double 1.000, i32 %instrument, i32 %tempo_base)
call void @play_note(i32 55, double 1.000, i32 %instrument, i32 %tempo_base)
%tmp8 = sitofp i32 1 to double
call void @pause_song(double %tmp8, i32 %tempo_base)
br label %endif_58
else_58:
br label %endif_58
endif_58:
%tmp9 = add i32 %tmp2, 1
store i32 %tmp9, i32* %tmp1
br label %repeat_cond_59
repeat_exit_59:

  ret i32 0
}
