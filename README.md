# EEG Disease Data Simulator and CNN-Attention Prototype

- A lightweight Python toolkit for:
  - generating synthetic EEG-like signals,
  - injecting disease-inspired EEG patterns,
  - extracting simple spectral features,
  - building a prototype labeled dataset,
  - supporting downstream deep learning experiments with a CNN + attention model.

---

## Project Overview

- This project provides a modular prototype pipeline for synthetic EEG experimentation.
- It is designed for:
  - research prototyping,
  - educational demonstrations,
  - testing preprocessing and classification workflows,
  - generating small simulated datasets before moving to real EEG data.
- The codebase includes:
  - EEG signal generation,
  - disease pattern injection,
  - feature extraction,
  - dataset building,
  - a CNN-attention model definition.

---

## What the Tool Currently Does

- Generates baseline synthetic EEG signals for a configurable set of EEG channels.
- Adds simple global artifacts/noise to the generated EEG.
- Injects simplified disease-inspired patterns for:
  - Alzheimer's disease (AD),
  - Parkinson's disease (PD),
  - Schizophrenia-like activity (SCZ).
- Extracts basic per-channel frequency-band features:
  - theta,
  - alpha,
  - beta.
- Builds a prototype dataset from generated signals.
- Defines a PyTorch CNN + attention model for EEG classification.

---

## Important Notes / Corrections

- This is a **prototype simulator**, not a clinically validated EEG generator.
- The disease injection functions are currently **simplified placeholders** based on added sinusoidal activity.
- The current `dataset_builder.py` generates only **AD-labeled** samples.
- The current `main_example.py` demonstrates only:
  - EEG generation,
  - AD injection,
  - feature extraction.
- The CNN-attention model is defined, but the minimal modular files do **not** include a full standalone PyTorch training pipeline.
- The larger `eeg_disease_data_simulator.py` file appears to contain notebook-style experiments, visualization utilities, and extra exploratory code.

---

## Project Structure

- `eeg_config.py`
  - stores default EEG configuration values,
  - defines the 10-20 channel system,
  - provides the time vector generator.

- `eeg_signal_generation.py`
  - generates baseline synthetic EEG signals,
  - creates global artifacts such as:
    - eye-blink-like low-frequency noise,
    - drift,
    - line noise.

- `disease_injectors.py`
  - injects simplified disease-inspired patterns into EEG:
    - `inject_ad_pattern(...)`
    - `inject_pd_pattern(...)`
    - `inject_schizo_pattern(...)`

- `feature_extraction.py`
  - computes simple frequency-band summary features:
    - theta,
    - alpha,
    - beta.

- `dataset_builder.py`
  - builds a small synthetic dataset from generated EEG samples,
  - currently labels generated samples as `AD`.

- `model_cnn_attention.py`
  - defines a 1D CNN + multi-head attention classifier in PyTorch,
  - outputs logits for 3 classes.

- `main_example.py`
  - demonstrates the basic pipeline from generation to feature extraction.

- `eeg_disease_data_simulator.py`
  - contains notebook-style exploratory code,
  - includes extended visualization and experimental sections,
  - should be treated as a research sandbox rather than the clean core API.

---

## Installation

- Clone or copy the project files into one folder.
- Create a Python environment.
- Install the main dependencies:

```bash
pip install numpy torch matplotlib
  model = CNN_Attention(n_channels=19, seq_len=2560)
  ```

---

