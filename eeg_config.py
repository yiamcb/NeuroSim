# eeg_config.py
import numpy as np

CHANNEL_SYSTEMS = {
    "10-20 (19)": [
        "Fp1","Fp2","F3","F4","C3","C4","P3","P4","O1","O2",
        "F7","F8","T3","T4","T5","T6","Fz","Cz","Pz"
    ]
}

DEFAULT_CHANNELS = CHANNEL_SYSTEMS["10-20 (19)"]
DEFAULT_FS = 256
DEFAULT_DURATION = 10

def make_time_vector(fs=DEFAULT_FS, duration=DEFAULT_DURATION):
    n = fs * duration
    return np.linspace(0, duration, n, endpoint=False)
