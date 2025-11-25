# disease_injectors.py
import numpy as np

def inject_ad_pattern(eeg, t, fs, severity="Moderate"):
    out = {}
    for ch, sig in eeg.items():
        out[ch] = sig + np.sin(2*np.pi*5*t)*0.5
    return out, ["P3","P4","Pz","O1","O2"]

def inject_pd_pattern(eeg, t, fs, severity="Moderate"):
    out = {}
    for ch, sig in eeg.items():
        out[ch] = sig + np.sin(2*np.pi*20*t)*0.3
    return out, ["F3","F4","C3","C4"]

def inject_schizo_pattern(eeg, t, fs, severity="Moderate"):
    out = {}
    for ch, sig in eeg.items():
        out[ch] = sig + np.sin(2*np.pi*35*t)*0.4
    return out, ["Fz","Cz","Pz"]
