"""
Example Script: How to Load the Synthetic Training Dataset
"""

import gzip
import json
import numpy as np

# --- 1. Load the pre-compiled numpy arrays (Instant, ready for model training) ---
print("Loading dataset.npz...")
data = np.load("dataset.npz", allow_pickle=True)
print("Keys:", list(data.keys()))
print("X shape (windows, timesteps, features):", data["X"].shape)
print("y shape (labels):", data["y"].shape)
print("Stages:", data["stages"])
print("Feature keys:", data["feature_keys"])

# --- 2. Load the raw training windows from JSON.GZ ---
print("\nLoading generated_training_windows.json.gz...")
with gzip.open("generated_training_windows.json.gz", "rt", encoding="utf-8") as f:
    windows = json.load(f)
print(f"Loaded {len(windows):,} sliding training windows.")
print("Sample window target stage:", windows[0].get("target_stage"))

# --- 3. Load the raw HTTP session sequences ---
print("\nLoading generated_http_sessions.json...")
with open("generated_http_sessions.json", "r", encoding="utf-8") as f:
    sessions = json.load(f)
print(f"Loaded {len(sessions):,} raw session requests.")
