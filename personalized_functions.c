#include <stdio.h>
#include <stdlib.h>

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
  return 0;
}

void play_note(int midi_note, double duration, int instrument, int tempo) {
  // Converte duração em batidas para segundos
  double duration_seconds = duration * (60.0 / tempo);

  const char *inst = decode_instrument(instrument);
  char filepath[256];
  sprintf(filepath, "%s/%d.wav", inst, midi_note);

  char command[1024];
  sprintf(command,
          "powershell -Command \"& '%s' --intf dummy --play-and-exit "
          "--stop-time=%.2f '%s'\"",
          "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe", duration_seconds,
          filepath);

  printf("Executando: %s\n", command); // debug
  system(command);
}

void play_sequence(int *notes, double *durations, int size, int instrument,
                   int tempo) {
  for (int i = 0; i < size; i++) {
    play_note(notes[i], durations[i], instrument, tempo);
  }
}

void pause_song(double duration, int tempo) {
  // Converte duração em batidas para segundos
  double duration_seconds =
      duration * (60.0 / tempo); // Você precisa passar tempo_base aqui

  char command[128];
  sprintf(command, "powershell -Command \"Start-Sleep -Seconds %.2f\"",
          duration_seconds);
  printf("Executando: %s\n", command); // debug
  system(command);
}