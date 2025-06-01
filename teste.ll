
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 160, align 4  ; tempo_base = 160
@tema_midi = global [3 x i32] zeroinitializer
@tema_dur = global [3 x double] zeroinitializer
@tema_pauses = global [3 x double] zeroinitializer

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
%nota2_midi = alloca i32
%nota2_dur = alloca double
store i32 53, i32* %nota2_midi
store double 0.500, double* %nota2_dur
%nota3_midi = alloca i32
%nota3_dur = alloca double
store i32 57, i32* %nota3_midi
store double 0.500, double* %nota3_dur
store i32 50, i32* %nota1_midi
store double 2.000, double* %nota1_dur
%tmp1 = load i32, i32* %nota1_midi
%tmp2 = load double, double* %nota1_dur
call void @play_note(i32 %tmp1, double %tmp2, i32 %instrument, i32 %tempo_base)
%tmp3 = sitofp i32 2 to double
call void @pause_song(double %tmp3, i32 %tempo_base)
%tmp4 = load i32, i32* %nota2_midi
%tmp5 = load i32, i32* %nota2_midi
%tmp6 = load double, double* %nota2_dur
%tmp7 = load i32, i32* %nota3_midi
%tmp8 = load i32, i32* %nota3_midi
%tmp9 = load double, double* %nota3_dur
%tmp10 = load i32, i32* %nota1_midi
%tmp11 = load i32, i32* %nota1_midi
%tmp12 = load double, double* %nota1_dur
%tmp13 = load i32, i32* %nota2_midi
%tmp14 = load i32, i32* %nota2_midi
%tmp15 = load double, double* %nota2_dur
%tmp16 = load i32, i32* %nota3_midi
%tmp17 = load i32, i32* %nota3_midi
%tmp18 = load double, double* %nota3_dur
%tmp19 = load i32, i32* %nota2_midi
%tmp20 = load i32, i32* %nota2_midi
%tmp21 = load double, double* %nota2_dur
%tmp22 = alloca [6 x i32]
%tmp23 = alloca [6 x double]
%tmp24 = alloca [6 x double]
%tmp25 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 0
store i32 %tmp5, i32* %tmp25
%tmp26 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 0
store double %tmp6, double* %tmp26
%tmp27 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 0
store double 1.000, double* %tmp27
%tmp28 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 1
store i32 %tmp8, i32* %tmp28
%tmp29 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 1
store double %tmp9, double* %tmp29
%tmp30 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 1
store double 0.500, double* %tmp30
%tmp31 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 2
store i32 %tmp11, i32* %tmp31
%tmp32 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 2
store double %tmp12, double* %tmp32
%tmp33 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 2
store double 0.730, double* %tmp33
%tmp34 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 3
store i32 %tmp14, i32* %tmp34
%tmp35 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 3
store double %tmp15, double* %tmp35
%tmp36 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 3
store double 2.000, double* %tmp36
%tmp37 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 4
store i32 %tmp17, i32* %tmp37
%tmp38 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 4
store double %tmp18, double* %tmp38
%tmp39 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 4
store double 1.000, double* %tmp39
%tmp40 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 5
store i32 %tmp20, i32* %tmp40
%tmp41 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 5
store double %tmp21, double* %tmp41
%tmp42 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 5
store double 2.000, double* %tmp42
%tmp43 = getelementptr [6 x i32], [6 x i32]* %tmp22, i32 0, i32 0
%tmp44 = getelementptr [6 x double], [6 x double]* %tmp23, i32 0, i32 0
%tmp45 = getelementptr [6 x double], [6 x double]* %tmp24, i32 0, i32 0
call void @play_sequence(i32* %tmp43, double* %tmp44, double* %tmp45, i32 6, i32 %instrument, i32 %tempo_base)
%tmp46 = load i32, i32* %nota1_midi
%tmp47 = load i32, i32* %nota1_midi
%tmp48 = load double, double* %nota1_dur
store i32 %tmp47, i32* getelementptr ([3 x i32], [3 x i32]* @tema_midi, i32 0, i32 0)
store double %tmp48, double* getelementptr ([3 x double], [3 x double]* @tema_dur, i32 0, i32 0)
store double 1.000, double* getelementptr ([3 x double], [3 x double]* @tema_pauses, i32 0, i32 0)
%tmp49 = load i32, i32* %nota2_midi
%tmp50 = load i32, i32* %nota2_midi
%tmp51 = load double, double* %nota2_dur
store i32 %tmp50, i32* getelementptr ([3 x i32], [3 x i32]* @tema_midi, i32 0, i32 1)
store double %tmp51, double* getelementptr ([3 x double], [3 x double]* @tema_dur, i32 0, i32 1)
store double 3.000, double* getelementptr ([3 x double], [3 x double]* @tema_pauses, i32 0, i32 1)
%tmp52 = load i32, i32* %nota3_midi
%tmp53 = load i32, i32* %nota3_midi
%tmp54 = load double, double* %nota3_dur
store i32 %tmp53, i32* getelementptr ([3 x i32], [3 x i32]* @tema_midi, i32 0, i32 2)
store double %tmp54, double* getelementptr ([3 x double], [3 x double]* @tema_dur, i32 0, i32 2)
store double 2.000, double* getelementptr ([3 x double], [3 x double]* @tema_pauses, i32 0, i32 2)
%tmp55 = getelementptr [3 x i32], [3 x i32]* @tema_midi, i32 0, i32 0
%tmp56 = getelementptr [3 x double], [3 x double]* @tema_dur, i32 0, i32 0
%tmp57 = getelementptr [3 x double], [3 x double]* @tema_pauses, i32 0, i32 0
call void @play_sequence(i32* %tmp55, double* %tmp56, double* %tmp57, i32 3, i32 %instrument, i32 %tempo_base)

  ret i32 0
}
