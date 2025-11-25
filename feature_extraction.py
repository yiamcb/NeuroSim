# feature_extraction.py
import numpy as np

def compute_bandpower(sig, fs, band):
    f1,f2 = band
    t = np.arange(len(sig))/fs
    osc = np.sin(2*np.pi*((f1+f2)/2)*t)
    return float(np.abs(np.dot(sig,osc))/len(sig))

def extract_features(eeg_dict, fs):
    feats = {}
    for ch, sig in eeg_dict.items():
        feats[ch] = {
            "theta": compute_bandpower(sig, fs, (4,7)),
            "alpha": compute_bandpower(sig, fs, (8,12)),
            "beta": compute_bandpower(sig, fs, (13,30)),
        }
    return feats
