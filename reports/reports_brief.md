🚴‍♂️ Cyclistic Bike-Share Case Study — ASK Phase



&nbsp;🧭 Business Task



Analyze Cyclistic’s bike-share trip data to identify usage differences between casual riders and annual members, and provide data-driven recommendations to convert casual riders into annual members.



---



🏢 Company Background



Cyclistic is a bike-share program based in Chicago offering two rider types:



Casual Riders — single-ride or day-pass users

Annual Members — yearly subscribers



The marketing team believes increasing annual memberships is key to long-term growth.



---



🎯 Project Goal



Help the marketing team design data-backed campaigns that encourage casual riders to become annual members.



---



❓ Key Questions



1\. How do annual members and casual riders use Cyclistic bikes differently? (behavioral patterns)

2\. When (time, day, or season) do each group ride the most? (promotion planning)

3\. What is the average ride duration for each rider type? (engagement insight)

4\. Which stations are most popular for each rider group? (location-based marketing)

5\. What factors might encourage casual riders to become members? \*(conversion strategy)



---



📈 Expected Outcomes



~ Clear, data-backed insights on user behavior

~ Visualization of ride patterns, times, and durations

~ 3 actionable marketing recommendations for membership growth



---



🧩 Data Source & Quality Factors



| Quality Factor    | Explanation                                             |

| ----------------- | ------------------------------------------------------- |

| Reliable      | Comes directly from Divvy (official public data source) |

| Original      | Collected by Cyclistic’s real system                    |

| Comprehensive | Covers all ride data for each month                     |

| Current       | Updated monthly, includes latest trips                  |

| Cited\*        | Public license from Divvy’s open data portal            |



📘 Data Source:\[Divvy Trip Data](https://divvy-tripdata.s3.amazonaws.com/index.html)

Used under the license provided for the \*\*Google Data Analytics Capstone Project.



---



🔍 Summary of Analysis



\* Combined 12 CSV files → one unified dataset using Python.

\* Cleaned and validated timestamps, missing values, and duplicates.

\* Created calculated fields:



&nbsp; `ride\_length\_min` (duration in minutes)

&nbsp; `day\_of\_week`, `month`, `hour\_of\_day`

\* Stored processed data in SQLite (`cyclistic.db`).

\* SQL queries performed for KPI-level insights.

\* Dashboard built in Power BI with dynamic filters and KPIs.



---



💡 Insights Summary



| Insight              | Observation                                                  |

| -------------------- | ------------------------------------------------------------ |

| Ride Behavior    | Members: frequent short trips; Casuals: longer leisure rides |

| Timing               | Members active on weekdays; Casuals on weekends              |

| Ride Duration        | Members avg 12.6 mins; Casuals avg 25.3 mins                 |

| Seasonal Pattern     | March–June → highest usage                                   |

| Opportunity          | Weekend-focused offers can convert casuals                   |



---



🧠 Recommendations



1\. Weekend Membership Campaigns: Offer weekend discounts for casual users.

2\. Loyalty Incentives: Give casuals reward points after 5 rides toward membership.

3\. Corporate Partnerships: Promote annual plans to companies for employee commuting.



---



🧰 Tools \& Technologies



Python · Pandas · SQLite · SQL · Power BI · GitHub



---



👨‍💻 Author



Mayuresh Parbat

📍 Pune, India

🎯 Data Analyst  Excel | Python | SQL | Power BI |

🔗 \[LinkedIn Profile](www.linkedin.com/in/mayuresh-parbat-a32b4133a)



