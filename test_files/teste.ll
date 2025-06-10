
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
%x = alloca i32
store i32 5, i32* %x
%y = alloca double
store double 3.14, double* %y
%flag = alloca i1
store i1 1, i1* %flag
%n1 = alloca %note
%n2 = alloca %note
%n2_pitch = getelementptr %note, %note* %n2, i32 0, i32 0
store i32 52, i32* %n2_pitch
%n2_duration = getelementptr %note, %note* %n2, i32 0, i32 1
store double 0.5, double* %n2_duration
%x_val1 = load i32, i32* %x
%tmp_binop_42 = add i32 %x_val1, 2
store i32 %tmp_binop_42, i32* %x
%y_val2 = load double, double* %y
%tmp_binop_48 = fmul double %y_val2, 2.0
store double %tmp_binop_48, double* %y
store i1 1, i1* %flag
%n1_pitch_ptr3 = getelementptr %note, %note* %n1, i32 0, i32 0
store i32 57, i32* %n1_pitch_ptr3
%n1_duration_ptr4 = getelementptr %note, %note* %n1, i32 0, i32 1
store double 1.0, double* %n1_duration_ptr4
%n1_pitch_ptr5 = getelementptr %note, %note* %n1, i32 0, i32 0
%n1_tmp_pitch7 = load i32, i32* %n1_pitch_ptr5
%n1_duration_ptr6 = getelementptr %note, %note* %n1, i32 0, i32 1
%n1_tmp_duration8 = load double, double* %n1_duration_ptr6
call void @play_note(i32 %n1_tmp_pitch7, double %n1_tmp_duration8, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 1.2, i32 %tempo_base)
call void @play_note(i32 53, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
call void @play_note(i32 52, double 0.6, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.3, i32 %tempo_base)
call void @play_note(i32 50, double 0.4, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
%n2_pitch_ptr9 = getelementptr %note, %note* %n2, i32 0, i32 0
%n2_tmp_pitch11 = load i32, i32* %n2_pitch_ptr9
%n2_duration_ptr10 = getelementptr %note, %note* %n2, i32 0, i32 1
%n2_tmp_duration12 = load double, double* %n2_duration_ptr10
call void @play_note(i32 %n2_tmp_pitch11, double %n2_tmp_duration12, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.6, i32 %tempo_base)
%x_val13 = load i32, i32* %x
%tmp_binop_94 = icmp sgt i32 %x_val13, 3
br i1 %tmp_binop_94, label %then_102, label %else_102
then_102:
%n2_pitch_ptr14 = getelementptr %note, %note* %n2, i32 0, i32 0
%n2_tmp_pitch16 = load i32, i32* %n2_pitch_ptr14
%n2_duration_ptr15 = getelementptr %note, %note* %n2, i32 0, i32 1
%n2_tmp_duration17 = load double, double* %n2_duration_ptr15
call void @play_note(i32 %n2_tmp_pitch16, double %n2_tmp_duration17, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.7, i32 %tempo_base)
br label %endif_102
else_102:
%n1_pitch_ptr18 = getelementptr %note, %note* %n1, i32 0, i32 0
%n1_tmp_pitch20 = load i32, i32* %n1_pitch_ptr18
%n1_duration_ptr19 = getelementptr %note, %note* %n1, i32 0, i32 1
%n1_tmp_duration21 = load double, double* %n1_duration_ptr19
call void @play_note(i32 %n1_tmp_pitch20, double %n1_tmp_duration21, i32 %instrument, i32 %tempo_base)
%tmp32 = sitofp i32 1 to double
call void @pause_song(double %tmp32, i32 %tempo_base)
%n2_pitch_ptr22 = getelementptr %note, %note* %n2, i32 0, i32 0
%n2_tmp_pitch24 = load i32, i32* %n2_pitch_ptr22
%n2_duration_ptr23 = getelementptr %note, %note* %n2, i32 0, i32 1
%n2_tmp_duration25 = load double, double* %n2_duration_ptr23
call void @play_note(i32 %n2_tmp_pitch24, double %n2_tmp_duration25, i32 %instrument, i32 %tempo_base)
%tmp35 = sitofp i32 2 to double
call void @pause_song(double %tmp35, i32 %tempo_base)
br label %endif_102
endif_102:
%repeat_counter26 = alloca i32
store i32 0, i32* %repeat_counter26
br label %repeat_cond_118
repeat_cond_118:
%repeat_val27 = load i32, i32* %repeat_counter26
%repeat_cmp28 = icmp slt i32 %repeat_val27, 3
br i1 %repeat_cmp28, label %repeat_body_118, label %repeat_exit_118
repeat_body_118:
%n1_pitch_ptr29 = getelementptr %note, %note* %n1, i32 0, i32 0
%n1_tmp_pitch31 = load i32, i32* %n1_pitch_ptr29
%n1_duration_ptr30 = getelementptr %note, %note* %n1, i32 0, i32 1
%n1_tmp_duration32 = load double, double* %n1_duration_ptr30
call void @play_note(i32 %n1_tmp_pitch31, double %n1_tmp_duration32, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
%repeat_next33 = add i32 %repeat_val27, 1
store i32 %repeat_next33, i32* %repeat_counter26
br label %repeat_cond_118
repeat_exit_118:
br label %repeat_while_cond_143
repeat_while_cond_143:
%x_val34 = load i32, i32* %x
%tmp_binop_125 = icmp slt i32 %x_val34, 10
br i1 %tmp_binop_125, label %repeat_while_body_143, label %repeat_while_exit_143
repeat_while_body_143:
%repeat_counter35 = alloca i32
store i32 0, i32* %repeat_counter35
br label %repeat_cond_142
repeat_cond_142:
%repeat_val36 = load i32, i32* %repeat_counter35
%repeat_cmp37 = icmp slt i32 %repeat_val36, 2
br i1 %repeat_cmp37, label %repeat_body_142, label %repeat_exit_142
repeat_body_142:
call void @play_note(i32 55, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
%n1_pitch_ptr38 = getelementptr %note, %note* %n1, i32 0, i32 0
%n1_tmp_pitch40 = load i32, i32* %n1_pitch_ptr38
%n1_duration_ptr39 = getelementptr %note, %note* %n1, i32 0, i32 1
%n1_tmp_duration41 = load double, double* %n1_duration_ptr39
call void @play_note(i32 %n1_tmp_pitch40, double %n1_tmp_duration41, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.6, i32 %tempo_base)
%x_val42 = load i32, i32* %x
%tmp_binop_140 = add i32 %x_val42, 1
store i32 %tmp_binop_140, i32* %x
%repeat_next43 = add i32 %repeat_val36, 1
store i32 %repeat_next43, i32* %repeat_counter35
br label %repeat_cond_142
repeat_exit_142:
br label %repeat_while_cond_143
repeat_while_exit_143:
%y_val44 = load double, double* %y
%tmp_binop_151 = fsub double %y_val44, 1.0
store double %tmp_binop_151, double* %y
%x_val45 = load i32, i32* %x
%tmp_binop_157 = mul i32 %x_val45, 2
store i32 %tmp_binop_157, i32* %x
call void @play_note(i32 50, double 0.5, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.2, i32 %tempo_base)
%n2_pitch_ptr46 = getelementptr %note, %note* %n2, i32 0, i32 0
%n2_tmp_pitch48 = load i32, i32* %n2_pitch_ptr46
%n2_duration_ptr47 = getelementptr %note, %note* %n2, i32 0, i32 1
%n2_tmp_duration49 = load double, double* %n2_duration_ptr47
call void @play_note(i32 %n2_tmp_pitch48, double %n2_tmp_duration49, i32 %instrument, i32 %tempo_base)
%tmp170 = sitofp i32 1 to double
call void @pause_song(double %tmp170, i32 %tempo_base)
call void @play_note(i32 57, double 0.4, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.1, i32 %tempo_base)
%n1_pitch_ptr50 = getelementptr %note, %note* %n1, i32 0, i32 0
%n1_tmp_pitch52 = load i32, i32* %n1_pitch_ptr50
%n1_duration_ptr51 = getelementptr %note, %note* %n1, i32 0, i32 1
%n1_tmp_duration53 = load double, double* %n1_duration_ptr51
call void @play_note(i32 %n1_tmp_pitch52, double %n1_tmp_duration53, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.7, i32 %tempo_base)
%x_val54 = load i32, i32* %x
%tmp_binop_187 = icmp sgt i32 %x_val54, 2
%y_val55 = load double, double* %y
%cast_r_190 = sitofp i32 10 to double
%tmp_binop_190 = fcmp olt double %y_val55, %cast_r_190
%tmp_binop_191 = and i1 %tmp_binop_187, %tmp_binop_190
store i1 %tmp_binop_191, i1* %flag
%flag_val56 = load i1, i1* %flag
br i1 %flag_val56, label %then_319, label %else_319
then_319:
%tmp199 = sitofp i32 2 to double
call void @pause_song(double %tmp199, i32 %tempo_base)
%tmp202 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp202, i32 %instrument, i32 %tempo_base)
%tmp205 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp205, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp212 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp212, i32 %instrument, i32 %tempo_base)
%tmp215 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp215, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp222 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp222, i32 %instrument, i32 %tempo_base)
%tmp225 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp225, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp232 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp232, i32 %instrument, i32 %tempo_base)
%tmp235 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp235, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp242 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp242, i32 %instrument, i32 %tempo_base)
%tmp245 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp245, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp252 = sitofp i32 1 to double
call void @play_note(i32 56, double %tmp252, i32 %instrument, i32 %tempo_base)
%tmp255 = sitofp i32 1 to double
call void @play_note(i32 61, double %tmp255, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp262 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp262, i32 %instrument, i32 %tempo_base)
%tmp265 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp265, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp272 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp272, i32 %instrument, i32 %tempo_base)
%tmp275 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp275, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp282 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp282, i32 %instrument, i32 %tempo_base)
%tmp285 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp285, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp292 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp292, i32 %instrument, i32 %tempo_base)
%tmp295 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp295, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp302 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp302, i32 %instrument, i32 %tempo_base)
%tmp305 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp305, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp312 = sitofp i32 2 to double
call void @play_note(i32 50, double %tmp312, i32 %instrument, i32 %tempo_base)
%tmp315 = sitofp i32 2 to double
call void @play_note(i32 55, double %tmp315, i32 %instrument, i32 %tempo_base)
%tmp318 = sitofp i32 2 to double
call void @pause_song(double %tmp318, i32 %tempo_base)
br label %endif_319
else_319:
br label %endif_319
endif_319:


  ret i32 0
}
