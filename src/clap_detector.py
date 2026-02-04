import sounddevice as sd
import numpy as np
import time

def detect_claps(duration=3, threshold=0.15, min_gap=0.25):
    """
    duration  : seconds to listen
    threshold : loudness required to count as a clap
    min_gap   : minimum time between claps (debounce)
    """

    fs = 44100
    print("👏 Listening for claps...")

    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    audio = np.abs(audio.flatten())

    clap_count = 0
    last_clap_time = 0

    for i, value in enumerate(audio):
        if value > threshold:
            current_time = i / fs
            if current_time - last_clap_time > min_gap:
                clap_count += 1
                last_clap_time = current_time

    return clap_count
