
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 120, align 4  ; tempo_base = 120
@melodia1_midi = global [3 x i32] zeroinitializer
@melodia1_dur = global [3 x double] zeroinitializer
@melodia2_midi = global [3 x i32] zeroinitializer
@melodia2_dur = global [3 x double] zeroinitializer

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
%e3_midi = alloca i32
%e3_dur = alloca double
store i32 40, i32* %e3_midi
store double 0.25, double* %e3_dur
%g3_midi = alloca i32
%g3_dur = alloca double
store i32 43, i32* %g3_midi
store double 0.25, double* %g3_dur
%a3_midi = alloca i32
%a3_dur = alloca double
store i32 45, i32* %a3_midi
store double 0.25, double* %a3_dur
%a3s_midi = alloca i32
%a3s_dur = alloca double
store i32 46, i32* %a3s_midi
store double 0.25, double* %a3s_dur
%b3_midi = alloca i32
%b3_dur = alloca double
store i32 47, i32* %b3_midi
store double 0.25, double* %b3_dur
%c4_midi = alloca i32
%c4_dur = alloca double
store i32 48, i32* %c4_midi
store double 0.25, double* %c4_dur
%d4_midi = alloca i32
%d4_dur = alloca double
store i32 50, i32* %d4_midi
store double 0.25, double* %d4_dur
%e4_midi = alloca i32
%e4_dur = alloca double
store i32 52, i32* %e4_midi
store double 0.25, double* %e4_dur
%f4_midi = alloca i32
%f4_dur = alloca double
store i32 53, i32* %f4_midi
store double 0.25, double* %f4_dur
%g4_midi = alloca i32
%g4_dur = alloca double
store i32 55, i32* %g4_midi
store double 0.25, double* %g4_dur
%a4_midi = alloca i32
%a4_dur = alloca double
store i32 57, i32* %a4_midi
store double 0.25, double* %a4_dur
%tmp1 = load i32, i32* %e4_midi
%tmp2 = load double, double* %e4_dur
store i32 %tmp1, i32* getelementptr ([3 x i32], [3 x i32]* @melodia1_midi, i32 0, i32 0)
store double %tmp2, double* getelementptr ([3 x double], [3 x double]* @melodia1_dur, i32 0, i32 0)
%tmp3 = load i32, i32* %e4_midi
%tmp4 = load double, double* %e4_dur
store i32 %tmp3, i32* getelementptr ([3 x i32], [3 x i32]* @melodia1_midi, i32 0, i32 1)
store double %tmp4, double* getelementptr ([3 x double], [3 x double]* @melodia1_dur, i32 0, i32 1)
%tmp5 = load i32, i32* %e4_midi
%tmp6 = load double, double* %e4_dur
store i32 %tmp5, i32* getelementptr ([3 x i32], [3 x i32]* @melodia1_midi, i32 0, i32 2)
store double %tmp6, double* getelementptr ([3 x double], [3 x double]* @melodia1_dur, i32 0, i32 2)
%tmp7 = getelementptr [3 x i32], [3 x i32]* @melodia1_midi, i32 0, i32 0
%tmp8 = getelementptr [3 x float], [3 x float]* @melodia1_dur, i32 0, i32 0
call void @play_sequence(i32* %tmp7, float* %tmp8, i32 3, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%tmp9 = load i32, i32* %c4_midi
%tmp10 = load double, double* %c4_dur
call void @play_note(i32 %tmp9, double %tmp10, i32 %instrument, i32 %tempo_base)
%tmp11 = load i32, i32* %e4_midi
%tmp12 = load double, double* %e4_dur
call void @play_note(i32 %tmp11, double %tmp12, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%tmp13 = load i32, i32* %g4_midi
%tmp14 = load double, double* %g4_dur
call void @play_note(i32 %tmp13, double %tmp14, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp15 = load i32, i32* %g3_midi
%tmp16 = load double, double* %g3_dur
call void @play_note(i32 %tmp15, double %tmp16, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp17 = load i32, i32* %c4_midi
%tmp18 = load double, double* %c4_dur
store i32 %tmp17, i32* getelementptr ([3 x i32], [3 x i32]* @melodia2_midi, i32 0, i32 0)
store double %tmp18, double* getelementptr ([3 x double], [3 x double]* @melodia2_dur, i32 0, i32 0)
%tmp19 = load i32, i32* %g3_midi
%tmp20 = load double, double* %g3_dur
store i32 %tmp19, i32* getelementptr ([3 x i32], [3 x i32]* @melodia2_midi, i32 0, i32 1)
store double %tmp20, double* getelementptr ([3 x double], [3 x double]* @melodia2_dur, i32 0, i32 1)
%tmp21 = load i32, i32* %e3_midi
%tmp22 = load double, double* %e3_dur
store i32 %tmp21, i32* getelementptr ([3 x i32], [3 x i32]* @melodia2_midi, i32 0, i32 2)
store double %tmp22, double* getelementptr ([3 x double], [3 x double]* @melodia2_dur, i32 0, i32 2)
%tmp23 = getelementptr [3 x i32], [3 x i32]* @melodia2_midi, i32 0, i32 0
%tmp24 = getelementptr [3 x float], [3 x float]* @melodia2_dur, i32 0, i32 0
call void @play_sequence(i32* %tmp23, float* %tmp24, i32 3, i32 %instrument, i32 %tempo_base)
%tmp25 = load i32, i32* %a3_midi
%tmp26 = load double, double* %a3_dur
call void @play_note(i32 %tmp25, double %tmp26, i32 %instrument, i32 %tempo_base)
%tmp27 = load i32, i32* %b3_midi
%tmp28 = load double, double* %b3_dur
call void @play_note(i32 %tmp27, double %tmp28, i32 %instrument, i32 %tempo_base)
%tmp29 = load i32, i32* %a3s_midi
%tmp30 = load double, double* %a3s_dur
call void @play_note(i32 %tmp29, double %tmp30, i32 %instrument, i32 %tempo_base)
%tmp31 = load i32, i32* %a3_midi
%tmp32 = load double, double* %a3_dur
call void @play_note(i32 %tmp31, double %tmp32, i32 %instrument, i32 %tempo_base)
%tmp33 = load i32, i32* %g3_midi
%tmp34 = load double, double* %g3_dur
call void @play_note(i32 %tmp33, double %tmp34, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.25, i32 %tempo_base)
%tmp35 = load i32, i32* %e4_midi
%tmp36 = load double, double* %e4_dur
call void @play_note(i32 %tmp35, double %tmp36, i32 %instrument, i32 %tempo_base)
%tmp37 = load i32, i32* %g4_midi
%tmp38 = load double, double* %g4_dur
call void @play_note(i32 %tmp37, double %tmp38, i32 %instrument, i32 %tempo_base)
%tmp39 = load i32, i32* %a4_midi
%tmp40 = load double, double* %a4_dur
call void @play_note(i32 %tmp39, double %tmp40, i32 %instrument, i32 %tempo_base)
%tmp41 = load i32, i32* %f4_midi
%tmp42 = load double, double* %f4_dur
call void @play_note(i32 %tmp41, double %tmp42, i32 %instrument, i32 %tempo_base)
%tmp43 = load i32, i32* %g4_midi
%tmp44 = load double, double* %g4_dur
call void @play_note(i32 %tmp43, double %tmp44, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.125, i32 %tempo_base)
%tmp45 = load i32, i32* %e4_midi
%tmp46 = load double, double* %e4_dur
call void @play_note(i32 %tmp45, double %tmp46, i32 %instrument, i32 %tempo_base)
%tmp47 = load i32, i32* %c4_midi
%tmp48 = load double, double* %c4_dur
call void @play_note(i32 %tmp47, double %tmp48, i32 %instrument, i32 %tempo_base)
%tmp49 = load i32, i32* %d4_midi
%tmp50 = load double, double* %d4_dur
call void @play_note(i32 %tmp49, double %tmp50, i32 %instrument, i32 %tempo_base)
%tmp51 = load i32, i32* %b3_midi
%tmp52 = load double, double* %b3_dur
call void @play_note(i32 %tmp51, double %tmp52, i32 %instrument, i32 %tempo_base)

  ret i32 0
}
