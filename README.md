- **NeuroSim** : a clinically informed synthetic EEG simulation toolkit for generating multichannel EEG, injecting disease-relevant patterns, extracting band features, and preparing data for AI benchmarking.
- NeuroSim framework targets **AD, PD, SCZ, EPI, and FTD**, supports configurable simulation settings, real-time visualization, metadata-aware exports, and CNN-attention benchmarking for explainable neurodiagnostic research.
- **Current code snapshot in this repository** = a compact modular implementation for:
  - baseline EEG generation,
  - AD / PD / SCZ pattern injection,
  - simple feature extraction,
  - lightweight dataset building,
  - a CNN-attention model stub,
  - an extended notebook-style Python script with richer interactive analysis utilities.

---

## Highlights

- **Clinically motivated synthetic EEG generation**
  - Mimics disease-relevant spectral changes described in the manuscript.
  - Supports region-aware pattern injection concepts such as posterior slowing in AD, motor beta changes in PD, and frontocentral abnormalities in SCZ.

- **AI-ready pipeline**
  - Generates synthetic signals that can be used for:
    - data augmentation,
    - model benchmarking,
    - representation learning,
    - explainability studies,
    - hypothesis testing when real EEG data is limited.

- **Two implementation layers**
  - **Lightweight modular scripts** for clean reuse in Python projects.
  - **`eeg_disease_data_simulator.py`** for expanded interactive exploration, visualization, and prototype workflows.
---

## Repository Structure

- **`eeg_config.py`**
  - Defines the EEG channel system.
  - Provides default sampling rate and duration.
  - Builds the time vector used throughout the pipeline.

- **`eeg_signal_generation.py`**
  - Generates baseline synthetic EEG.
  - Adds simple global artifacts:
    - eye blink,
    - nonstationary drift,
    - line noise.

- **`disease_injectors.py`**
  - Injects disease-style modifications into baseline EEG.
  - Includes:
    - `inject_ad_pattern(...)`
    - `inject_pd_pattern(...)`
    - `inject_schizo_pattern(...)`

- **`feature_extraction.py`**
  - Computes simple bandpower-style features.
  - Extracts:
    - theta,
    - alpha,
    - beta.

- **`dataset_builder.py`**
  - Builds a small synthetic dataset.
  - **Current behavior**:
    - generates baseline EEG,
    - injects **AD** pattern,
    - returns `X` and `y`.
  - **Important**:
    - it imports PD and SCZ injectors,
    - but currently labels and builds only **AD** samples.

- **`model_cnn_attention.py`**
  - Defines a simple PyTorch CNN-attention classifier.
  - Useful as a starting point for EEG sequence benchmarking.

- **`main_example.py`**
  - Minimal runnable example.
  - Demonstrates:
    - EEG generation,
    - AD injection,
    - feature extraction,
    - printing extracted features.

- **`eeg_disease_data_simulator.py`**
  - Extended prototype script converted from a notebook.
  - Includes richer logic for:
    - interactive widgets,
    - plotting,
    - topographic visualization,
    - additional disease workflows,
    - experimental analyses,
    - prototype benchmarking utilities.
  - Best treated as an **exploration / prototype script**, not yet a cleaned production module.

- **`NeuroSim_JBHI_SubmittedVersion.pdf`**
  - Manuscript describing the broader NeuroSim framework, motivation, methodology, and validation scope.

---

## Step-by-Step Usage

### 1) Configure the EEG setup

- Open **`eeg_config.py`**.
- Adjust the defaults if needed:
  - `DEFAULT_CHANNELS`
  - `DEFAULT_FS`
  - `DEFAULT_DURATION`

- Example:
  ```python
  from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION
  ```

### 2) Generate baseline EEG

- Use **`generate_eeg(...)`** from `eeg_signal_generation.py`.
- Inputs:
  - `channels`
  - `fs`
  - `duration`
  - `stimulus` (currently placeholder-friendly in the lightweight version)

- Example:
  ```python
  from eeg_signal_generation import generate_eeg
  from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION

  t, eeg = generate_eeg(DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION)
  ```

- Output:
  - `t` = time vector
  - `eeg` = dictionary mapping channel name -> signal array

### 3) Inject a disease pattern

- Use one of the injectors from **`disease_injectors.py`**.
- Available in the modular code:
  - `inject_ad_pattern(...)`
  - `inject_pd_pattern(...)`
  - `inject_schizo_pattern(...)`

- Example:
  ```python
  from disease_injectors import inject_ad_pattern

  diseased_eeg, affected_channels = inject_ad_pattern(eeg, t, DEFAULT_FS, severity="Moderate")
  ```

- Output:
  - `diseased_eeg` = modified EEG dictionary
  - `affected_channels` = list of channels associated with the injection rule

### 4) Extract features

- Use **`extract_features(...)`** from `feature_extraction.py`.
- Example:
  ```python
  from feature_extraction import extract_features

  features = extract_features(diseased_eeg, DEFAULT_FS)
  print(features)
  ```

- Extracted per-channel features:
  - theta
  - alpha
  - beta

### 5) Build a small synthetic dataset

- Use **`build_dataset(...)`** from `dataset_builder.py`.
- Example:
  ```python
  from dataset_builder import build_dataset
  from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION

  X, y = build_dataset(DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION, n_samples=20)
  ```

- Current behavior:
  - builds repeated **AD-injected** samples only.

- Suggested next extension:
  - add disease selection,
  - mix AD / PD / SCZ labels,
  - return array tensors instead of raw dictionaries.

### 6) Run the CNN-attention model

- Use **`CNN_Attention`** from `model_cnn_attention.py`.
- Example:
  ```python
  import torch
  from model_cnn_attention import CNN_Attention

  model = CNN_Attention(n_channels=19, seq_len=2560)
  x = torch.randn(8, 19, 2560)  # batch, channels, time
  y = model(x)
  print(y.shape)
  ```

- Expected output shape:
  - `(batch_size, 3)`

- Important:
  - the current head size is **3 classes**,
  - so adjust the final layer if you expand to more diseases.

### 7) Explore the extended prototype script

- Open **`eeg_disease_data_simulator.py`** in:
  - Jupyter,
  - Google Colab,
  - or another notebook-friendly environment.

- Use this script when you want:
  - interactive controls,
  - richer plotting,
  - topographic maps,
  - additional disease experiments,
  - exploratory benchmarking.

---

## Example End-to-End Workflow

- **Goal**
  - generate baseline EEG,
  - inject a disease pattern,
  - extract features,
  - prepare model-ready data.

- **Workflow**
  - Step 1: set channel list, sampling rate, and duration.
  - Step 2: call `generate_eeg(...)`.
  - Step 3: call one injector.
  - Step 4: call `extract_features(...)`.
  - Step 5: convert the channel dictionary to a tensor or array.
  - Step 6: train or evaluate `CNN_Attention`.

- **Minimal example**
  ```python
  from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION
  from eeg_signal_generation import generate_eeg
  from disease_injectors import inject_pd_pattern
  from feature_extraction import extract_features

  t, eeg = generate_eeg(DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION)
  diseased_eeg, affected = inject_pd_pattern(eeg, t, DEFAULT_FS, severity="Moderate")
  features = extract_features(diseased_eeg, DEFAULT_FS)

  print("Affected channels:", affected)
  print("Feature keys:", list(features.keys())[:5])
  ```
---

## Why This Tool Is Useful

- **For EEG researchers**
  - Generates controllable synthetic brain signals for rapid experiments.
  - Makes it easier to test ideas before accessing sensitive real clinical data.

- **For ML / DL researchers**
  - Produces structured synthetic samples for early benchmarking.
  - Helps stress-test architectures under known spectral perturbations.
  - Supports low-data prototyping.

- **For neuroinformatics and personalized healthcare work**
  - Encodes clinically inspired priors into a reproducible simulation pipeline.
  - Helps study disease-dependent signal separability.
  - Supports explainability-oriented experimentation.

- **For teaching and demonstrations**
  - Provides a compact, easy-to-read codebase for showing:
    - synthetic EEG generation,
    - artifact injection,
    - disease modulation,
    - feature extraction,
    - model benchmarking.

---

## Functional Benefits

- **Reproducibility**
  - Standardized defaults for channels, sampling rate, and duration.
  - Clear code separation between generation, injection, features, and modeling.

- **Interpretability**
  - Disease logic is explicit in code.
  - Affected channels are returned directly by injectors.
  - Feature extraction is transparent and easy to inspect.

- **Extensibility**
  - Add new disease modules as separate injectors.
  - Replace simple bandpower with PSD-based or wavelet-based features.
  - Upgrade the model head for multi-class or severity-aware training.

- **Data augmentation potential**
  - Helpful when real EEG datasets are small, imbalanced, or privacy-restricted.

- **Benchmarking value**
  - Lets you test whether known disease-specific perturbations are learnable by neural models.

---

## Important Notes

- **Research-use orientation**
  - This repository is suitable for:
    - simulation,
    - benchmarking,
    - data augmentation experiments,
    - teaching,
    - prototype development.

- **Not a clinical diagnostic device**
  - Treat the outputs as **research simulation data**.
  - Do not use this repository alone for medical diagnosis.

- **Code maturity note**
  - The repository currently mixes:
    - clean modular scripts,
    - a large exploratory prototype script.
  - Refactoring is recommended before production use.

---

## Minimal Demo Command Summary

- **Run the demo**
  ```bash
  python main_example.py
  ```

- **Build a tiny dataset**
  ```python
  from dataset_builder import build_dataset
  from eeg_config import DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION

  X, y = build_dataset(DEFAULT_CHANNELS, DEFAULT_FS, DEFAULT_DURATION, n_samples=10)
  ```

- **Instantiate the classifier**
  ```python
  from model_cnn_attention import CNN_Attention

  model = CNN_Attention(n_channels=19, seq_len=2560)
  ```

---

