
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 80, align 4  ; tempo_base = 80

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
%e_midi = alloca i32
%e_dur = alloca double
store i32 52, i32* %e_midi
store double 1.0, double* %e_dur
%g_midi = alloca i32
%g_dur = alloca double
store i32 55, i32* %g_midi
store double 1.0, double* %g_dur
%a_midi = alloca i32
%a_dur = alloca double
store i32 57, i32* %a_midi
store double 2.0, double* %a_dur
%tmp1 = alloca i32
store i32 0, i32* %tmp1
br label %repeat_cond_31
repeat_cond_31:
%tmp2 = load i32, i32* %tmp1
%tmp3 = icmp slt i32 %tmp2, 2
br i1 %tmp3, label %repeat_body_31, label %repeat_exit_31
repeat_body_31:
%tmp4 = load i32, i32* %e_midi
%tmp5 = load double, double* %e_dur
call void @play_note(i32 %tmp4, double %tmp5, i32 %instrument, i32 %tempo_base)
%tmp6 = load i32, i32* %g_midi
%tmp7 = load double, double* %g_dur
call void @play_note(i32 %tmp6, double %tmp7, i32 %instrument, i32 %tempo_base)
%tmp8 = load i32, i32* %a_midi
%tmp9 = load double, double* %a_dur
call void @play_note(i32 %tmp8, double %tmp9, i32 %instrument, i32 %tempo_base)
%tmp10 = sitofp i32 1 to double
call void @pause_song(double %tmp10, i32 %tempo_base)
%tmp11 = add i32 %tmp2, 1
store i32 %tmp11, i32* %tmp1
br label %repeat_cond_31
repeat_exit_31:

  ret i32 0
}
