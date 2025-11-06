import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect(r"C:\Users\mayur\OneDrive\Desktop\cyclistic-case-study\data\Processed\cyclistic.db")

# Run SQL query
query = "SELECT member_casual, COUNT(*) AS total_rides FROM trips GROUP BY member_casual;"
result = pd.read_sql(query, conn)

# Print the result
print(result)

conn.close()
