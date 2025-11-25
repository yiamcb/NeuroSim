# dataset_builder.py
from eeg_signal_generation import generate_eeg
from disease_injectors import inject_ad_pattern, inject_pd_pattern, inject_schizo_pattern

def build_dataset(channels, fs, duration, n_samples=10):
    X = []
    y = []
    for _ in range(n_samples):
        t, eeg = generate_eeg(channels, fs, duration)
        diseased, _ = inject_ad_pattern(eeg, t, fs)
        X.append(diseased)
        y.append("AD")
    return X, y
