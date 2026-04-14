# Imports
import scipy.io.wavfile as wav
import numpy as np
import sounddevice as sd

# Duration in number of seconds
NSECS = 1
# Sample rate in samples per second
SAMPLE_RATE = 48000
# Frequency in Hz (cycles per second)
FREQ = 440
AMPLITUDE = 8192
# Total number of samples in the whole thing
NSAMPLES = NSECS * SAMPLE_RATE

# Array of sample times
t = np.linspace(0, NSECS, num=NSAMPLES, endpoint=False)
f = AMPLITUDE * np.sin(2 * np.pi * FREQ * t)

f_int16 = f.astype(np.int16)

# Write to a WAV file
wav.write('sine.wav', SAMPLE_RATE, f_int16)

# Generate a clipped sine wave
f_half_amp = (AMPLITUDE * 2) * np.sin(2 * np.pi * FREQ * t)
f_clipped = np.clip(f_half_amp, -AMPLITUDE, AMPLITUDE)

f_clipped_int16 = f_clipped.astype(np.int16)

# Write to a WAV file
wav.write('clipped.wav', SAMPLE_RATE, f_clipped_int16)

# Play the clipped sine wave directly
print("Playing clipped sine wave...")
sd.play(f_clipped_int16, SAMPLE_RATE)
# Wait so the program doesn't end before the wave plays back completely
sd.wait()