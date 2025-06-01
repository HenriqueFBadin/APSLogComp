
@.fmt_int = private constant [4 x i8] c"%d\0A\00"
@.fmt_float = private constant [4 x i8] c"%f\0A\00"
@.format_in = private constant [3 x i8] c"%d\00"

@scan_int = common global i32 0, align 4

; ====== Declarações Globais ======
@instrument = global i32 1, align 4  ; instrument = guitar
@tempo_base = global i32 120, align 4  ; tempo_base = 120
@seq1_midi = global [2 x i32] zeroinitializer
@seq1_dur = global [2 x double] zeroinitializer
@seq1_pauses = global [2 x double] zeroinitializer
@seq2_midi = global [2 x i32] zeroinitializer
@seq2_dur = global [2 x double] zeroinitializer
@seq2_pauses = global [2 x double] zeroinitializer

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
%x = alloca i32
store i32 5, i32* %x
%y = alloca double
store double 3.14, double* %y
%flag = alloca i1
store i1 1, i1* %flag
%n1_midi = alloca i32
%n1_dur = alloca double
%n2_midi = alloca i32
%n2_dur = alloca double
store i32 52, i32* %n2_midi
store double 0.500, double* %n2_dur
store i32 50, i32* getelementptr ([2 x i32], [2 x i32]* @seq1_midi, i32 0, i32 0)
store double 0.400, double* getelementptr ([2 x double], [2 x double]* @seq1_dur, i32 0, i32 0)
store double 0.200, double* getelementptr ([2 x double], [2 x double]* @seq1_pauses, i32 0, i32 0)
%tmp1 = load i32, i32* %n2_midi
%tmp2 = load i32, i32* %n2_midi
%tmp3 = load double, double* %n2_dur
store i32 %tmp2, i32* getelementptr ([2 x i32], [2 x i32]* @seq1_midi, i32 0, i32 1)
store double %tmp3, double* getelementptr ([2 x double], [2 x double]* @seq1_dur, i32 0, i32 1)
store double 0.600, double* getelementptr ([2 x double], [2 x double]* @seq1_pauses, i32 0, i32 1)
%tmp4 = load i32, i32* %n1_midi
%tmp5 = load i32, i32* %n1_midi
%tmp6 = load double, double* %n1_dur
store i32 %tmp5, i32* getelementptr ([2 x i32], [2 x i32]* @seq2_midi, i32 0, i32 0)
store double %tmp6, double* getelementptr ([2 x double], [2 x double]* @seq2_dur, i32 0, i32 0)
store double 1.000, double* getelementptr ([2 x double], [2 x double]* @seq2_pauses, i32 0, i32 0)
%tmp7 = load i32, i32* %n2_midi
%tmp8 = load i32, i32* %n2_midi
%tmp9 = load double, double* %n2_dur
store i32 %tmp8, i32* getelementptr ([2 x i32], [2 x i32]* @seq2_midi, i32 0, i32 1)
store double %tmp9, double* getelementptr ([2 x double], [2 x double]* @seq2_dur, i32 0, i32 1)
store double 2.000, double* getelementptr ([2 x double], [2 x double]* @seq2_pauses, i32 0, i32 1)
%tmp10 = load i32, i32* %x
%tmp11 = add i32 %tmp10, 2
store i32 %tmp11, i32* %x
%tmp12 = load double, double* %y
%tmp13 = fmul double %tmp12, 2.0
store double %tmp13, double* %y
store i1 1, i1* %flag
store i32 57, i32* %n1_midi
store double 1.000, double* %n1_dur
%tmp14 = load i32, i32* %n1_midi
%tmp15 = load double, double* %n1_dur
call void @play_note(i32 %tmp14, double %tmp15, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 1.2, i32 %tempo_base)
%tmp16 = alloca [2 x i32]
%tmp17 = alloca [2 x double]
%tmp18 = alloca [2 x double]
%tmp19 = getelementptr [2 x i32], [2 x i32]* %tmp16, i32 0, i32 0
store i32 53, i32* %tmp19
%tmp20 = getelementptr [2 x double], [2 x double]* %tmp17, i32 0, i32 0
store double 0.500, double* %tmp20
%tmp21 = getelementptr [2 x double], [2 x double]* %tmp18, i32 0, i32 0
store double 0.200, double* %tmp21
%tmp22 = getelementptr [2 x i32], [2 x i32]* %tmp16, i32 0, i32 1
store i32 52, i32* %tmp22
%tmp23 = getelementptr [2 x double], [2 x double]* %tmp17, i32 0, i32 1
store double 0.600, double* %tmp23
%tmp24 = getelementptr [2 x double], [2 x double]* %tmp18, i32 0, i32 1
store double 0.300, double* %tmp24
%tmp25 = getelementptr [2 x i32], [2 x i32]* %tmp16, i32 0, i32 0
%tmp26 = getelementptr [2 x double], [2 x double]* %tmp17, i32 0, i32 0
%tmp27 = getelementptr [2 x double], [2 x double]* %tmp18, i32 0, i32 0
call void @play_sequence(i32* %tmp25, double* %tmp26, double* %tmp27, i32 2, i32 %instrument, i32 %tempo_base)
%tmp28 = getelementptr [2 x i32], [2 x i32]* @seq1_midi, i32 0, i32 0
%tmp29 = getelementptr [2 x double], [2 x double]* @seq1_dur, i32 0, i32 0
%tmp30 = getelementptr [2 x double], [2 x double]* @seq1_pauses, i32 0, i32 0
call void @play_sequence(i32* %tmp28, double* %tmp29, double* %tmp30, i32 2, i32 %instrument, i32 %tempo_base)
%tmp31 = load i32, i32* %x
%tmp32 = icmp sgt i32 %tmp31, 3
br i1 %tmp32, label %then_89, label %else_89
then_89:
%tmp33 = load i32, i32* %n2_midi
%tmp34 = load double, double* %n2_dur
call void @play_note(i32 %tmp33, double %tmp34, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.7, i32 %tempo_base)
br label %endif_89
else_89:
%tmp35 = getelementptr [2 x i32], [2 x i32]* @seq2_midi, i32 0, i32 0
%tmp36 = getelementptr [2 x double], [2 x double]* @seq2_dur, i32 0, i32 0
%tmp37 = getelementptr [2 x double], [2 x double]* @seq2_pauses, i32 0, i32 0
call void @play_sequence(i32* %tmp35, double* %tmp36, double* %tmp37, i32 2, i32 %instrument, i32 %tempo_base)
br label %endif_89
endif_89:
%tmp38 = alloca i32
store i32 0, i32* %tmp38
br label %repeat_cond_96
repeat_cond_96:
%tmp39 = load i32, i32* %tmp38
%tmp40 = icmp slt i32 %tmp39, 3
br i1 %tmp40, label %repeat_body_96, label %repeat_exit_96
repeat_body_96:
%tmp41 = load i32, i32* %n1_midi
%tmp42 = load double, double* %n1_dur
call void @play_note(i32 %tmp41, double %tmp42, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
%tmp43 = add i32 %tmp39, 1
store i32 %tmp43, i32* %tmp38
br label %repeat_cond_96
repeat_exit_96:
%tmp44 = alloca i32
store i32 0, i32* %tmp44
br label %repeatwhile_cond_112
repeatwhile_cond_112:
%tmp45 = load i32, i32* %tmp44
%tmp46 = icmp slt i32 %tmp45, 2
%tmp47 = load i32, i32* %x
%tmp48 = icmp slt i32 %tmp47, 10
%tmp49 = and i1 %tmp46, %tmp48
br i1 %tmp49, label %repeatwhile_body_112, label %repeatwhile_exit_112
repeatwhile_body_112:
%tmp50 = load i32, i32* %n1_midi
%tmp51 = load i32, i32* %n1_midi
%tmp52 = load double, double* %n1_dur
%tmp53 = alloca [2 x i32]
%tmp54 = alloca [2 x double]
%tmp55 = alloca [2 x double]
%tmp56 = getelementptr [2 x i32], [2 x i32]* %tmp53, i32 0, i32 0
store i32 55, i32* %tmp56
%tmp57 = getelementptr [2 x double], [2 x double]* %tmp54, i32 0, i32 0
store double 0.500, double* %tmp57
%tmp58 = getelementptr [2 x double], [2 x double]* %tmp55, i32 0, i32 0
store double 0.200, double* %tmp58
%tmp59 = getelementptr [2 x i32], [2 x i32]* %tmp53, i32 0, i32 1
store i32 %tmp51, i32* %tmp59
%tmp60 = getelementptr [2 x double], [2 x double]* %tmp54, i32 0, i32 1
store double %tmp52, double* %tmp60
%tmp61 = getelementptr [2 x double], [2 x double]* %tmp55, i32 0, i32 1
store double 0.600, double* %tmp61
%tmp62 = getelementptr [2 x i32], [2 x i32]* %tmp53, i32 0, i32 0
%tmp63 = getelementptr [2 x double], [2 x double]* %tmp54, i32 0, i32 0
%tmp64 = getelementptr [2 x double], [2 x double]* %tmp55, i32 0, i32 0
call void @play_sequence(i32* %tmp62, double* %tmp63, double* %tmp64, i32 2, i32 %instrument, i32 %tempo_base)
%tmp65 = add i32 %tmp45, 1
store i32 %tmp65, i32* %tmp44
br label %repeatwhile_cond_112
repeatwhile_exit_112:
%tmp66 = load double, double* %y
%tmp67 = fsub double %tmp66, 1.0
store double %tmp67, double* %y
%tmp68 = load i32, i32* %x
%tmp69 = mul i32 %tmp68, 2
store i32 %tmp69, i32* %x
%tmp70 = load i32, i32* %n2_midi
%tmp71 = load i32, i32* %n2_midi
%tmp72 = load double, double* %n2_dur
%tmp73 = load i32, i32* %n1_midi
%tmp74 = load i32, i32* %n1_midi
%tmp75 = load double, double* %n1_dur
%tmp76 = alloca [4 x i32]
%tmp77 = alloca [4 x double]
%tmp78 = alloca [4 x double]
%tmp79 = getelementptr [4 x i32], [4 x i32]* %tmp76, i32 0, i32 0
store i32 50, i32* %tmp79
%tmp80 = getelementptr [4 x double], [4 x double]* %tmp77, i32 0, i32 0
store double 0.500, double* %tmp80
%tmp81 = getelementptr [4 x double], [4 x double]* %tmp78, i32 0, i32 0
store double 0.200, double* %tmp81
%tmp82 = getelementptr [4 x i32], [4 x i32]* %tmp76, i32 0, i32 1
store i32 %tmp71, i32* %tmp82
%tmp83 = getelementptr [4 x double], [4 x double]* %tmp77, i32 0, i32 1
store double %tmp72, double* %tmp83
%tmp84 = getelementptr [4 x double], [4 x double]* %tmp78, i32 0, i32 1
store double 1.000, double* %tmp84
%tmp85 = getelementptr [4 x i32], [4 x i32]* %tmp76, i32 0, i32 2
store i32 57, i32* %tmp85
%tmp86 = getelementptr [4 x double], [4 x double]* %tmp77, i32 0, i32 2
store double 0.400, double* %tmp86
%tmp87 = getelementptr [4 x double], [4 x double]* %tmp78, i32 0, i32 2
store double 0.100, double* %tmp87
%tmp88 = getelementptr [4 x i32], [4 x i32]* %tmp76, i32 0, i32 3
store i32 %tmp74, i32* %tmp88
%tmp89 = getelementptr [4 x double], [4 x double]* %tmp77, i32 0, i32 3
store double %tmp75, double* %tmp89
%tmp90 = getelementptr [4 x double], [4 x double]* %tmp78, i32 0, i32 3
store double 0.700, double* %tmp90
%tmp91 = getelementptr [4 x i32], [4 x i32]* %tmp76, i32 0, i32 0
%tmp92 = getelementptr [4 x double], [4 x double]* %tmp77, i32 0, i32 0
%tmp93 = getelementptr [4 x double], [4 x double]* %tmp78, i32 0, i32 0
call void @play_sequence(i32* %tmp91, double* %tmp92, double* %tmp93, i32 4, i32 %instrument, i32 %tempo_base)
%tmp94 = load i32, i32* %x
%tmp95 = icmp sgt i32 %tmp94, 2
%tmp96 = load double, double* %y
%tmp97 = sitofp i32 10 to double
%tmp98 = fcmp olt double %tmp96, %tmp97
%tmp99 = and i1 %tmp95, %tmp98
store i1 %tmp99, i1* %flag

  ret i32 0
}
