import pandas as pd
from pathlib import Path

# Paths
OUT = Path("data/processed")

# Read combined CSV
df = pd.read_csv(OUT / "cyclistic_all_raw.csv")

# ✅ Convert to datetime explicitly
df["started_at"] = pd.to_datetime(df["started_at"], errors="coerce")
df["ended_at"] = pd.to_datetime(df["ended_at"], errors="coerce")

# ✅ Standardize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# ✅ Drop rows with missing or invalid dates
df = df.dropna(subset=["started_at", "ended_at", "member_casual"])

# ✅ Calculate ride length in minutes
df["ride_length_min"] = (df["ended_at"] - df["started_at"]).dt.total_seconds() / 60

# ✅ Remove negative or zero ride times
df = df[df["ride_length_min"] > 0]

# ✅ Add day_of_week column
df["day_of_week"] = df["started_at"].dt.day_name()

# ✅ Optional: Add month and hour columns
df["month"] = df["started_at"].dt.month
df["hour_of_day"] = df["started_at"].dt.hour

# ✅ Save cleaned dataset
df.to_csv(OUT / "cyclistic_clean.csv", index=False)

print("✅ Cleaned data saved as cyclistic_clean.csv")
