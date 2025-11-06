import pandas as pd
from pathlib import Path

RAW = Path("data/raw")        
OUT = Path("data/processed")
OUT.mkdir(parents=True, exist_ok=True)

all_files = list(RAW.glob("*.csv"))
frames = []

for f in all_files:
    print("Reading:", f.name)
    df = pd.read_csv(f)
    frames.append(df)

if len(frames) == 0:
    print("⚠️ No CSV files found! Check your path or file names.")
else:
    data = pd.concat(frames, ignore_index=True)
    data.to_csv(OUT / "cyclistic_all_raw.csv", index=False)
    print("✅ Combined all files into cyclistic_all_raw.csv")
