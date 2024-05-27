# signal_functions.py

import numpy as np
import matplotlib.pyplot as plt
from obspy import read
from scipy import signal
from ipywidgets import interact, fixed, RadioButtons

def interactive_plot(signal_type, freq=1.0, num_steps=10, file_path=''):
    st = read(file_path)
    sp = st[0].stats.sampling_rate
    waveform = st[0].data

    # Create a time array based on the length of the waveform
    t = np.linspace(0, len(waveform) / 1, len(waveform))

    if signal_type == 'Sine Signal':
        # Generate a sine wave with the given frequency
        signal = np.sin(2 * np.pi * freq * t)
    elif signal_type == 'Step Signal':
        signal = np.zeros_like(t)
        for i in range(num_steps):
            signal[(t >= i * len(waveform) / num_steps) & (t < (i + 1) * len(waveform) / num_steps)] = i % 2

    convolved_signal = np.convolve(signal, waveform, mode='same')
    t_conv = np.linspace(0, len(convolved_signal) / 1, len(convolved_signal))

    # Rest of the plotting code remains unchanged
    plt.figure(figsize=(10, 6))
    plt.subplot(3, 1, 1)
    plt.plot(t, signal, label=signal_type)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(signal_type)
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(waveform, label='MiniSEED Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('MiniSEED Wave')
    plt.grid(True)
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(t_conv, convolved_signal, label='Convolved Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Convolved Signal')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Plot the spectrograms
    plt.figure(figsize=(10, 9))

    # Signal
    plt.subplot(3, 1, 1)
    plt.specgram(signal, Fs=sp, NFFT=1024, noverlap=512)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of ' + signal_type)

    # MiniSEED wave
    plt.subplot(3, 1, 2)
    plt.specgram(waveform, Fs=sp, NFFT=1024, noverlap=512)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of MiniSEED Wave')

    # Convolved signal
    plt.subplot(3, 1, 3)
    plt.specgram(convolved_signal, Fs=sp, NFFT=1024, noverlap=512)
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')
    plt.title('Spectrogram of Convolved Signal')

    plt.tight_layout()
    plt.show()

def update_interactive_plot(signal_type, file_path=''):
    if signal_type == 'Sine Signal':
        interact(interactive_plot, signal_type=fixed(signal_type), freq=(0.1, 20.0, 0.1), num_steps=fixed(10), file_path=fixed(file_path))
    elif signal_type == 'Step Signal':
        interact(interactive_plot, signal_type=fixed(signal_type), freq=fixed(1.0), num_steps=(1, 20, 1), file_path=fixed(file_path))

interact(update_interactive_plot, signal_type=RadioButtons(options=['Sine Signal', 'Step Signal']), file_path='');

