import sounddevice as sd
import numpy as np

sd.default.device = 1   

duration = 3
fs = 44100

print("🎙️ Recording raw audio for 3 seconds... CLAP or SPEAK")
audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

print("📈 Max audio level detected:", np.max(np.abs(audio)))
