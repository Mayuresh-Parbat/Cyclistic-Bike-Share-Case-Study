import sqlite3
import pandas as pd

df = pd.read_csv(r"C:\Users\mayur\OneDrive\Desktop\cyclistic-case-study\data\Processed\cyclistic_clean.csv")
conn = sqlite3.connect(r"C:\Users\mayur\OneDrive\Desktop\cyclistic-case-study\data\Processed\cyclistic.db")
df.to_sql("trips", conn, index=False, if_exists="replace")
conn.close()
print("✅ Data saved as cyclistic.db")
