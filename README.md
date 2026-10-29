# Multi-Stage Web Injection Attack: Synthetic Training Dataset

This private repository contains the complete synthetic dataset generated and used for training the context-aware sequential detection and forecasting models (LSTM + XGBoost + HMM) from the `AttackDetection` MongoDB database.

---

## 📊 Dataset Overview

The dataset models realistic multi-stage web injection attack trajectories against a modern web architecture, covering the 5 canonical kill-chain stages:
0. **NORMAL**: Benign user browsing, catalog search, static asset retrieval.
1. **RECON**: Active & passive discovery (`/whoami`, `/api/Challenges`, `/rest/user/whoami`).
2. **FUZZING**: Parameter boundary & edge testing (`-1`, `0`, `999999`, single quote anomalies).
3. **INJECTION**: Structured injection payloads (Boolean SQLi, UNION SELECT, XSS `<script>alert(1)</script>`).
4. **EXPLOITATION**: Confirmed unauthorized access (Admin JWT forgery, user schema exfiltration, IDOR).

---

## 🗂️ Included Collections & Files

| File | Records | Size | Description |
| :--- | :--- | :--- | :--- |
| **`dataset.npz`** | 10,000 windows | ~332 KB | Compact binary NumPy array containing pre-extracted feature tensors `X` (10000, 20, 23), target labels `y`, train/val/test splits, and HMM sequences. Ready for instant model training without MongoDB. |
| **`generated_training_windows.json.gz`** | 10,000 windows | ~1.2 MB | Complete context sliding windows collection (`generated_training_windows`) in compressed JSON. Balanced across all 5 stages (2,000 windows per stage). |
| **`generated_training_windows_part1.json`** | 2,500 windows | ~31 MB | Uncompressed JSON slice (records 1–2,500) for direct inspection. |
| **`generated_training_windows_part2.json`** | 2,500 windows | ~31 MB | Uncompressed JSON slice (records 2,501–5,000) for direct inspection. |
| **`generated_training_windows_part3.json`** | 2,500 windows | ~31 MB | Uncompressed JSON slice (records 5,001–7,500) for direct inspection. |
| **`generated_training_windows_part4.json`** | 2,500 windows | ~31 MB | Uncompressed JSON slice (records 7,501–10,000) for direct inspection. |
| **`generated_http_sessions.json`** | 11,853 requests | ~27 MB | Complete raw session stream collection (`generated_http_sessions`) across 500 multi-stage sessions. Used to derive HMM transition priors. |
| **`export_dataset.py`** | - | ~7 KB | Python utility that deterministically compiles raw MongoDB JSON documents into `dataset.npz`. |
| **`load_dataset_example.py`** | - | ~1 KB | Quickstart script demonstrating how to load both the NumPy binary and the raw JSON documents. |

---

## 📈 Stage Distribution in Training Windows (`generated_training_windows`)

| Stage Index | Stage Name | Number of Windows | Ratio |
| :---: | :--- | :---: | :---: |
| 0 | `NORMAL` | 2,000 | 20.0% |
| 1 | `RECON` | 2,000 | 20.0% |
| 2 | `FUZZING` | 2,000 | 20.0% |
| 3 | `INJECTION` | 2,000 | 20.0% |
| 4 | `EXPLOITATION` | 2,000 | 20.0% |
| **Total** | | **10,000** | **100.0%** |

---

## 🚀 Quickstart: Loading the Dataset

```python
import numpy as np

# Load compiled arrays directly
data = np.load("dataset.npz", allow_pickle=True)

X = data["X"]          # Shape: (10000, 20, 23) -> 10,000 windows, context len 20, 23 causal features
y = data["y"]          # Shape: (10000,) -> stage labels (0 to 4)
splits = data["splits"] # Array of "train", "validation", "test"

print(f"Loaded {X.shape[0]} training samples across {len(data['stages'])} stages.")
```

To load the full JSON documents:
```python
import gzip, json

with gzip.open("generated_training_windows.json.gz", "rt", encoding="utf-8") as f:
    windows = json.load(f)
```
