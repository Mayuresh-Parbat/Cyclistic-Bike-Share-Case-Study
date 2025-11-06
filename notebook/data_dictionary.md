📘 Cyclistic Bike-Share — Data Dictionary

| Column                    | Description                     | Example                      | Data Type |
| ------------------------- | ------------------------------- | ---------------------------- | --------- |
| `ride_id`                 | Unique trip identifier          | C1D650626C8C899A             | Text      |
| `rideable_type`           | Type of bike used               | electric_bike / classic_bike | Text      |
| `started_at`              | Start timestamp of the ride     | 2024-03-21 14:20:00          | Datetime  |
| `ended_at`                | End timestamp of the ride       | 2024-03-21 14:45:00          | Datetime  |
| `start_station_name`      | Starting station name           | Streeter Dr & Grand Ave      | Text      |
| `end_station_name`        | Ending station name             | Michigan Ave & Oak St        | Text      |
| `start_lat` / `start_lng` | Latitude and longitude of start | 41.8923 / -87.6121           | Float     |
| `end_lat` / `end_lng`     | Latitude and longitude of end   | 41.9009 / -87.6236           | Float     |
| `member_casual`           | Rider type                      | member / casual              | Text      |
| `ride_length_min`         | Total ride duration in minutes  | 25.3                         | Float     |
| `day_of_week`             | Day of the week ride started    | Monday–Sunday                | Text      |
| `month`                   | Month number of the ride        | 1–12                         | Integer   |
| `hour_of_day`             | Hour of the day ride started    | 0–23                         | Integer   |

✅ Note:

* `ride_length_min` = `ended_at - started_at` (in minutes)
* Derived fields: `day_of_week`, `month`, and `hour_of_day` support trend & KPI analysis.
* Processed data saved in `data/processed/cyclistic_clean.csv` and `cyclistic.db`.


