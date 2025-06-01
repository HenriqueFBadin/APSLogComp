#include <stdio.h>
#include <stdlib.h>
#include <unistd.h> // For sleep() on Linux

const char *note_names[] = {"C",  "C#", "D",  "D#", "E",  "F",
                            "F#", "G",  "G#", "A",  "A#", "B"};

char *decode_instrument(int instrument) {
  if (instrument == 0) {
    return "piano";
  } else if (instrument == 1) {
    return "guitar";
  } else if (instrument == 2) {
    return "violin";
  }
  return "unknown";
}

void play_note(int midi_note, double duration, int instrument, int tempo) {
  double duration_seconds = duration * (60.0 / tempo);
  const char *inst = decode_instrument(instrument);
  
  char filepath[256];
  sprintf(filepath, "%s/%d.wav", inst, midi_note);

  // Use Linux's VLC command (assuming VLC is installed)
  char command[1024];
  sprintf(command,
            "/mnt/c/Windows/System32/cmd.exe /c \"start /B C:\\PROGRA~1\\VideoLAN\\VLC\\vlc.exe "
            "--intf dummy --play-and-exit --stop-time=%.2f \"%s\"\"",
            duration_seconds, filepath);

  printf("Playing: %s\n", command); // Debug
  system(command);
}

void pause_song(double duration, int tempo) {
    double duration_seconds = duration * (60.0 / tempo);
    printf("Tempo: %f\n", duration);
    
    char command[128];
    sprintf(command, 
            "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command \"Start-Sleep -Seconds %.2f\"",
            duration_seconds);
    
    printf("Pausing: %s\n", command); // Debug
    system(command);
}

void play_sequence(int *notes, double *durations, double *pauses, int size, int instrument, int tempo) {

    for (int i = 0; i < size; i++) {
        play_note(notes[i], durations[i], instrument, tempo);
        
        // Aplica pausa se não for a última nota e pausa > 0
        if (pauses[i] > 0) {
            pause_song(pauses[i], tempo);
        }
    }
}