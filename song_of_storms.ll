
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 160, align 4  ; tempo_base = 160
@tema_midi = global [6 x i32] zeroinitializer
@tema_dur = global [6 x double] zeroinitializer

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
%nota1_midi = alloca i32
%nota1_dur = alloca double
store i32 50, i32* %nota1_midi
store double 0.5, double* %nota1_dur
%nota2_midi = alloca i32
%nota2_dur = alloca double
store i32 53, i32* %nota2_midi
store double 0.5, double* %nota2_dur
%nota3_midi = alloca i32
%nota3_dur = alloca double
store i32 57, i32* %nota3_midi
store double 0.5, double* %nota3_dur
%tmp1 = load i32, i32* %nota1_midi
%tmp2 = load double, double* %nota1_dur
store i32 %tmp1, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 0)
store double %tmp2, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 0)
%tmp3 = load i32, i32* %nota2_midi
%tmp4 = load double, double* %nota2_dur
store i32 %tmp3, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 1)
store double %tmp4, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 1)
%tmp5 = load i32, i32* %nota3_midi
%tmp6 = load double, double* %nota3_dur
store i32 %tmp5, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 2)
store double %tmp6, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 2)
%tmp7 = load i32, i32* %nota1_midi
%tmp8 = load double, double* %nota1_dur
store i32 %tmp7, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 3)
store double %tmp8, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 3)
%tmp9 = load i32, i32* %nota2_midi
%tmp10 = load double, double* %nota2_dur
store i32 %tmp9, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 4)
store double %tmp10, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 4)
%tmp11 = load i32, i32* %nota3_midi
%tmp12 = load double, double* %nota3_dur
store i32 %tmp11, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 5)
store double %tmp12, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 5)
%tmp13 = getelementptr [6 x i32], [6 x i32]* @tema_midi, i32 0, i32 0
%tmp14 = getelementptr [6 x float], [6 x float]* @tema_dur, i32 0, i32 0
call void @play_sequence(i32* %tmp13, float* %tmp14, i32 6, i32 %instrument, i32 %tempo_base)
%tmp15 = alloca i32
store i32 0, i32* %tmp15
br label %repeat_cond_42
repeat_cond_42:
%tmp16 = load i32, i32* %tmp15
%tmp17 = icmp slt i32 %tmp16, 2
br i1 %tmp17, label %repeat_body_42, label %repeat_exit_42
repeat_body_42:
%tmp18 = load i32, i32* %nota3_midi
%tmp19 = load double, double* %nota3_dur
call void @play_note(i32 %tmp18, double %tmp19, i32 %instrument, i32 %tempo_base)
%tmp20 = load i32, i32* %nota2_midi
%tmp21 = load double, double* %nota2_dur
call void @play_note(i32 %tmp20, double %tmp21, i32 %instrument, i32 %tempo_base)
%tmp22 = load i32, i32* %nota1_midi
%tmp23 = load double, double* %nota1_dur
call void @play_note(i32 %tmp22, double %tmp23, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%tmp24 = add i32 %tmp16, 1
store i32 %tmp24, i32* %tmp15
br label %repeat_cond_42
repeat_exit_42:

  ret i32 0
}
