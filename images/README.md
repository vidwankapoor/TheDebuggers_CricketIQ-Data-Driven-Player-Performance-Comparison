# Application Screenshots & UI Walkthrough

This section provides a visual walkthrough of the application, demonstrating the complete flow from player selection to statistical comparison and final interpretation.

- Main Application Interface
  
The main page of the Streamlit application where users interact with the system. It serves as the entry point for selecting players and configuring the comparison.

- Player Selection Panel

This screen allows users to select:
+ Two cricketers for comparison
+ The batting position at which the comparison should be performed
+ Restricting the comparison to a specific batting position ensures role-based fairness.

# Comparison Output – Metrics & Interpretation

- Comparison View 1
Displays player-wise innings count and key performance metrics derived from ball-by-ball data.

- Comparison View 2
Shows calculated statistics such as average runs, strike rate, and boundary contribution for both players.

- Comparison View 3
Pie chart visualization comparing the share of average runs contributed by each player at the selected batting position.

- Comparison View 4
Visual representation highlighting differences in performance distribution between the two players.

- Comparison View 5
Displays consistency-based metrics (e.g., frequency of 30+ scores), helping evaluate reliability across innings.

- Comparison View 6 – Statistical Test Result
Shows the output of the Mann–Whitney U Test, including the p-value and final interpretation indicating whether the observed performance difference is statistically significant.
