
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
@tempo_base = global i32 100, align 4  ; tempo_base = 100

declare i32 @printf(i8*, ...)
declare i32 @scanf(i8*, ...)

define i32 @main() {
entry:

%instrument = load i32, i32* @instrument
%tempo_base = load i32, i32* @tempo_base
%tmp8 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp8, i32 %instrument, i32 %tempo_base)
%tmp11 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp11, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp18 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp18, i32 %instrument, i32 %tempo_base)
%tmp21 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp21, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp28 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp28, i32 %instrument, i32 %tempo_base)
%tmp31 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp31, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp38 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp38, i32 %instrument, i32 %tempo_base)
%tmp41 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp41, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp48 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp48, i32 %instrument, i32 %tempo_base)
%tmp51 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp51, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp58 = sitofp i32 1 to double
call void @play_note(i32 56, double %tmp58, i32 %instrument, i32 %tempo_base)
%tmp61 = sitofp i32 1 to double
call void @play_note(i32 61, double %tmp61, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp68 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp68, i32 %instrument, i32 %tempo_base)
%tmp71 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp71, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp78 = sitofp i32 1 to double
call void @play_note(i32 50, double %tmp78, i32 %instrument, i32 %tempo_base)
%tmp81 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp81, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp88 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp88, i32 %instrument, i32 %tempo_base)
%tmp91 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp91, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.5, i32 %tempo_base)
%tmp98 = sitofp i32 1 to double
call void @play_note(i32 55, double %tmp98, i32 %instrument, i32 %tempo_base)
%tmp101 = sitofp i32 1 to double
call void @play_note(i32 60, double %tmp101, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp108 = sitofp i32 1 to double
call void @play_note(i32 53, double %tmp108, i32 %instrument, i32 %tempo_base)
%tmp111 = sitofp i32 1 to double
call void @play_note(i32 58, double %tmp111, i32 %instrument, i32 %tempo_base)
call void @pause_song(double 0.85, i32 %tempo_base)
%tmp118 = sitofp i32 2 to double
call void @play_note(i32 50, double %tmp118, i32 %instrument, i32 %tempo_base)
%tmp121 = sitofp i32 2 to double
call void @play_note(i32 55, double %tmp121, i32 %instrument, i32 %tempo_base)
%tmp124 = sitofp i32 2 to double
call void @pause_song(double %tmp124, i32 %tempo_base)


  ret i32 0
}
