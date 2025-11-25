# eeg_signal_generation.py
import numpy as np
from eeg_config import make_time_vector

def generate_global_artifacts(t, fs):
    return {
        "eye_blink": np.sin(2*np.pi*1*t)*0.1,
        "nonstationary_drift": np.sin(2*np.pi*0.2*t)*0.3,
        "line_noise": np.sin(2*np.pi*50*t)*0.05,
    }

def add_advanced_noise(signal, fs, t, ch, global_art):
    return signal + sum(global_art.values())

def generate_eeg(channels, fs, duration, stimulus="resting_ec"):
    t = make_time_vector(fs, duration)
    global_art = generate_global_artifacts(t, fs)
    eeg = {}
    for ch in channels:
        base = np.random.normal(0,0.2,len(t))
        eeg[ch] = add_advanced_noise(base, fs, t, ch, global_art)
    return t, eeg
