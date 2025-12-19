# CricketIQ-Data-Driven-Player-Performance-Comparison
# Project Overview

Cricket player evaluation is often influenced by opinions, recent form bias, or simple averages, despite the availability of detailed match data. This project presents a data-driven and statistically validated framework to compare the performance of two cricketers using IPL ball-by-ball data.
The goal is to determine whether observed differences in performance are statistically significant rather than assumed.
The system combines exploratory data analysis, feature engineering, and hypothesis testing with an interactive interface to provide objective and interpretable player comparisons.

 # Objectives

- Convert subjective player comparisons into quantifiable and measurable insights
- Compare players role-wise by restricting analysis to the same batting position
- Apply statistical hypothesis testing to validate performance differences
- Make advanced analytics accessible through an interactive web interface

# Dataset

Source: Kaggle IPL Dataset (2008–2024)
Data Used:
- Ball-by-ball deliveries data
- Match-level metadata
Innings are reconstructed from delivery-level records to compute accurate player metrics.

# Technology Stack

- Python – Core programming language
- Pandas & NumPy – Data preprocessing and aggregation
- SciPy (stats) – Mann–Whitney U Test for non-parametric hypothesis testing
- Matplotlib / Seaborn – Data visualization and validation
- Streamlit – Interactive web-based user interface
- Jupyter Notebook – Exploratory analysis and development

# Methodology

- Collect and clean ball-by-ball IPL data
- Filter data by selected batting position
- Generate innings-level performance metrics
- Formulate null and alternative hypotheses
- Apply the Mann–Whitney U Test
- Visualize and interpret results
- Present outputs through an interactive interface

# Key Features

- Position-specific player comparison
- Handles skewed and unequal cricket data
- Statistically valid performance evaluation
- Clear, human-readable result interpretation
- Interactive and user-friendly design

# Output

The application displays:
- Player-wise performance metrics
- Statistical test results (p-value based decision)
- Visual comparisons for better interpretability

# Limitations

- Batting performance only
- IPL T20 format focused
- No predictive modeling
- Limited match-context factors

# Future Scope

- Include venue, opposition, and match situation
- Extend analysis to ODIs and Test cricket
- Add bowling and all-rounder evaluation
- Integrate predictive performance models

# Conclusion

This project demonstrates how statistical analysis and hypothesis testing can bring objectivity and transparency to cricket performance evaluation. By combining rigorous analytics with an interactive interface, it bridges the gap between raw data and meaningful decision-making.

