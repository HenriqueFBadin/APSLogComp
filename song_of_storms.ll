
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 160, align 4  ; tempo_base = 160
@tema_midi = global [6 x i32] zeroinitializer
@tema_dur = global [6 x double] zeroinitializer
@tema_pauses = global [6 x double] zeroinitializer

; ====== Funções Musicais ======
declare void @play_note(i32, double, i32, i32)  ; (nota MIDI, duração em segundos)
declare void @pause_song(double, i32)           ; (duração em segundos)
declare void @play_sequence(i32*, double*, double*, i32, i32, i32)  ; (array MIDI, array durações, tamanho)

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:

%instrument = load i32, i32* @instrument
%tempo_base = load i32, i32* @tempo_base
%nota1_midi = alloca i32
%nota1_dur = alloca double
store i32 50, i32* %nota1_midi
store double 0.500, double* %nota1_dur
%nota2_midi = alloca i32
%nota2_dur = alloca double
store i32 53, i32* %nota2_midi
store double 0.500, double* %nota2_dur
%nota3_midi = alloca i32
%nota3_dur = alloca double
store i32 57, i32* %nota3_midi
store double 0.500, double* %nota3_dur
store i32 50, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 0)
store double 0.500, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 0)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 0)
%tmp1 = load i32, i32* %nota2_midi
%tmp2 = load i32, i32* %nota2_midi
%tmp3 = load double, double* %nota2_dur
store i32 %tmp2, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 1)
store double %tmp3, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 1)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 1)
%tmp4 = load i32, i32* %nota3_midi
%tmp5 = load i32, i32* %nota3_midi
%tmp6 = load double, double* %nota3_dur
store i32 %tmp5, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 2)
store double %tmp6, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 2)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 2)
%tmp7 = load i32, i32* %nota1_midi
%tmp8 = load i32, i32* %nota1_midi
%tmp9 = load double, double* %nota1_dur
store i32 %tmp8, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 3)
store double %tmp9, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 3)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 3)
%tmp10 = load i32, i32* %nota2_midi
%tmp11 = load i32, i32* %nota2_midi
%tmp12 = load double, double* %nota2_dur
store i32 %tmp11, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 4)
store double %tmp12, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 4)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 4)
%tmp13 = load i32, i32* %nota3_midi
%tmp14 = load i32, i32* %nota3_midi
%tmp15 = load double, double* %nota3_dur
store i32 %tmp14, i32* getelementptr ([6 x i32], [6 x i32]* @tema_midi, i32 0, i32 5)
store double %tmp15, double* getelementptr ([6 x double], [6 x double]* @tema_dur, i32 0, i32 5)
store double 0.250, double* getelementptr ([6 x double], [6 x double]* @tema_pauses, i32 0, i32 5)
%tmp16 = getelementptr [6 x i32], [6 x i32]* @tema_midi, i32 0, i32 0
%tmp17 = getelementptr [6 x double], [6 x double]* @tema_dur, i32 0, i32 0
%tmp18 = getelementptr [6 x double], [6 x double]* @tema_pauses, i32 0, i32 0
call void @play_sequence(i32* %tmp16, double* %tmp17, double* %tmp18, i32 6, i32 %instrument, i32 %tempo_base)
%tmp19 = alloca i32
store i32 0, i32* %tmp19
br label %repeat_cond_60
repeat_cond_60:
%tmp20 = load i32, i32* %tmp19
%tmp21 = icmp slt i32 %tmp20, 2
br i1 %tmp21, label %repeat_body_60, label %repeat_exit_60
repeat_body_60:
%tmp22 = load i32, i32* %nota3_midi
%tmp23 = load double, double* %nota3_dur
call void @play_note(i32 %tmp22, double %tmp23, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp24 = load i32, i32* %nota2_midi
%tmp25 = load double, double* %nota2_dur
call void @play_note(i32 %tmp24, double %tmp25, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp26 = load i32, i32* %nota1_midi
%tmp27 = load double, double* %nota1_dur
call void @play_note(i32 %tmp26, double %tmp27, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%tmp28 = add i32 %tmp20, 1
store i32 %tmp28, i32* %tmp19
br label %repeat_cond_60
repeat_exit_60:

  ret i32 0
}
