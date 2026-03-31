- **NeuroSim** : a clinically informed synthetic EEG simulation toolkit for generating multichannel EEG, injecting disease-relevant patterns, extracting band features, and preparing data for AI benchmarking.
- **Manuscript scope** = the submitted NeuroSim framework targets **AD, PD, SCZ, EPI, and FTD**, supports configurable simulation settings, real-time visualization, metadata-aware exports, and CNN-attention benchmarking for explainable neurodiagnostic research.
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

- **Research-to-code alignment**
  - The manuscript describes the broader NeuroSim vision.
  - The uploaded `.py` files provide a practical starting repository that can be extended toward the full manuscript functionality.

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

## Current Scope vs Full Manuscript Scope

- **Full manuscript scope**
  - multi-disorder simulation across **AD, PD, SCZ, EPI, FTD**,
  - configurable severity,
  - GUI-driven interaction,
  - visualization and export,
  - CNN-attention benchmarking,
  - explainability-oriented analysis.

- **Current modular `.py` scope**
  - baseline EEG generation,
  - AD / PD / SCZ injection,
  - simple feature extraction,
  - AD-only dataset builder,
  - 3-class CNN-attention model head,
  - demo script.

- **Practical interpretation**
  - Use this repo as a **research codebase starter**.
  - Extend it incrementally toward the full paper implementation.

---

## Installation

- **Python version**
  - Recommended: **Python 3.10+**

- **Minimal dependencies for the modular scripts**
  - `numpy`
  - `torch`

- **Additional dependencies for the extended prototype script**
  - `matplotlib`
  - `scipy`
  - `pandas`
  - `mne`
  - `ipywidgets`
  - `seaborn`
  - `scikit-learn`
  - `statsmodels`
  - `umap-learn`
  - `tensorflow`

- **Step 1 — clone the repository**
  ```bash
  git clone https://github.com/<your-username>/NeuroSim.git
  cd NeuroSim
  ```

- **Step 2 — create and activate a virtual environment**
  ```bash
  python -m venv .venv
  ```

  - **Windows**
    ```bash
    .venv\Scripts\activate
    ```

  - **macOS / Linux**
    ```bash
    source .venv/bin/activate
    ```

- **Step 3 — install minimal requirements**
  ```bash
  pip install numpy torch
  ```

- **Step 4 — install full prototype requirements (optional)**
  ```bash
  pip install matplotlib scipy pandas mne ipywidgets seaborn scikit-learn statsmodels umap-learn tensorflow
  ```

---

## Quick Start

- **Fastest way to verify the tool works**
  ```bash
  python main_example.py
  ```

- **What this demo does**
  - loads default EEG configuration,
  - generates baseline EEG,
  - injects an AD-like pattern,
  - extracts theta / alpha / beta features,
  - prints the result to the console.

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

## Supported Disease Logic

- **In the manuscript**
  - AD
  - PD
  - SCZ
  - EPI
  - FTD

- **In the lightweight modular scripts right now**
  - AD
  - PD
  - SCZ

- **In the extended prototype script**
  - broader experimental support is present for:
    - AD,
    - PD,
    - SCZ,
    - EPI,
    - FTD.

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

## How NeuroSim Relates Functionally to LLMs

- **NeuroSim is not an LLM**
  - It is a **signal simulation and benchmarking tool**.
  - Its main outputs are EEG time series, features, labels, and model-ready tensors.

- **NeuroSim + LLMs = strong workflow pairing**
  - LLMs can help users:
    - generate experiment plans,
    - suggest disease injection settings,
    - write training scripts,
    - summarize extracted EEG features,
    - auto-document simulation runs,
    - explain model outputs in human-readable language.

- **Practical LLM integration ideas**
  - **Config generation**
    - Use an LLM to convert a natural-language request into simulation parameters.
    - Example:
      - “Generate moderate AD-like EEG for 19 channels, 256 Hz, 10 seconds.”
  - **Code generation**
    - Use an LLM to create new injectors for EPI, FTD, sleep staging, or task paradigms.
  - **Metadata summarization**
    - Use an LLM to turn JSON metadata and extracted features into experiment summaries.
  - **Experiment automation**
    - Use an LLM agent to orchestrate loops over diseases, severities, and channel systems.
  - **Explainability reporting**
    - Use an LLM to convert feature trends, attention weights, and attribution maps into readable reports.

- **Why the pairing is useful**
  - NeuroSim produces structured synthetic EEG.
  - LLMs make the workflow easier to:
    - configure,
    - document,
    - interpret,
    - scale.

- **Important boundary**
  - LLMs should assist with orchestration and interpretation.
  - NeuroSim should remain responsible for the actual EEG signal generation and quantitative benchmarking.

---

## Recommended Next Improvements

- **Codebase cleanup**
  - split `eeg_disease_data_simulator.py` into smaller modules,
  - move plotting and benchmarking into separate files,
  - add a true `requirements.txt`.

- **Dataset builder upgrades**
  - support mixed diseases,
  - support severity labels,
  - output NumPy arrays directly,
  - add train / validation / test splitting.

- **Model upgrades**
  - expand from 3 classes to the full disease list,
  - add training loop and evaluation scripts,
  - add checkpoint saving,
  - add confusion matrix export.

- **Feature upgrades**
  - Welch PSD features,
  - entropy,
  - spectral edge frequency,
  - connectivity metrics,
  - topographic summaries.

- **Research upgrades**
  - add explicit metadata export,
  - add `.edf` / `.mat` / `.csv` save functions,
  - add real-to-synthetic transfer tests,
  - add explainability utilities for model interpretation.

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

## Citation / Background

- **Project manuscript**
  - *NeuroSim: Clinically-Informed Multi-Disorder EEG Simulator with Personalized Pattern Injection and AI-Driven Neurological Modeling*

- **If you use this repository in research**
  - cite the manuscript,
  - describe the exact repository commit used,
  - report which disease injectors and parameter settings were enabled.

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

## In One Line

- **NeuroSim** helps you generate clinically inspired synthetic EEG, inject disease-like signal patterns, extract interpretable features, and prepare data for AI and LLM-assisted neuroinformatics workflows.
