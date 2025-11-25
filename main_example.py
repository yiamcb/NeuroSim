# main_example.py
from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION
from eeg_signal_generation import generate_eeg
from disease_injectors import inject_ad_pattern
from feature_extraction import extract_features

if __name__ == "__main__":
    t, eeg = generate_eeg(DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION)
    diseased, _ = inject_ad_pattern(eeg, t, DEFAULT_FS)
    feats = extract_features(diseased, DEFAULT_FS)
    print("Example features:", feats)
