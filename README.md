# CS416P-Clipped

## wav.py
Creates and writes a one second long sine wave with a frequency of 440Hz, and a sample rate of 48,000 samples/second to a WAV file "sine.wav" and a clipped version of that same sine wave to another WAV file "clipped.wav", then plays the clipped sine wave directly.

Uses NumPy and SciPy to generate the samples, applying clipping, and write the WAV files.

Uses sounddevice to send the audio to speakers.

## Build Instructions
**The following libraries need to be installed:**
numpy
scipy
sounddevice

**Can be done with the following command:**
pip install numpy scipy sounddevice

## Running
**The script can be run directly from your terminal with the following command:**
python wav.py

## Reflection
**What I Did:**
Played with generating sine waves of different frequencies and durations, focused on a one second 440Hz sine wave to perform audio clipping on. I did this by doubling the amplitude and using the NumPy's clip module. I then exported both the unaltered sine wave and the clipped sine wave to their respective WAV files using SciPy's wavfile module.

**How It Went:**
Experimenting with clipping was interesting, and I think the most important part was making sure I had my equation set up correctly. It was a bit confusing at first that the values would be doubled in a 1/2 amplitude sine wave, but it's because the original values were a 1/4 amplitude. I had fun because it was something I had never tried doing before, and it was cool to be able to hear the changes I was making. 

**What's Still to be Done:**
It would be cool to implement a visualization for these waves for when the program is just run, and potentially experiment more with playing different lengths of different frequency waves directly.