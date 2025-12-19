import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from compare import compare_players_stats

# Load processed data
df = pd.read_csv("processed_data/player_match_df.csv")

st.title("Cricket Player Comparison (Stats-based)")

players = sorted(df["batsman"].unique())

col1, col2 = st.columns(2)
with col1:
    p1 = st.selectbox("Select Player 1", players, key="p1")
with col2:
    p2 = st.selectbox("Select Player 2", players, key="p2")

pos = st.number_input("Enter batting position", min_value=1, max_value=11, value=3, step=1)

# SINGLE button 
if st.button("Compare"):

    #  Text summary from compare.py
    result_md = compare_players_stats(df, p1, p2, pos)
    st.markdown(result_md)

    #  Graphs
    pos_df = df[
        (df["batting_position"] == pos) &
        (df["batsman"].isin([p1, p2]))
    ]

    if pos_df.empty:
        st.warning("No innings available for these players at this position.")
    else:
        def player_stats(sub):
            return {
                "avg_runs": sub["runs_scored"].mean(),
                "avg_sr": sub["strike_rate"].mean(),
                "consistency_30": sub["is_30_plus"].mean() * 100,
                "boundary_pct": sub["boundary_pct"].mean()
            }

        p1_stats = player_stats(pos_df[pos_df["batsman"] == p1])
        p2_stats = player_stats(pos_df[pos_df["batsman"] == p2])

        labels = [p1, p2]

        #  Average Runs 
        fig1, ax1 = plt.subplots(figsize=(4, 4))
        ax1.pie(
            [p1_stats["avg_runs"], p2_stats["avg_runs"]],
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )
        ax1.set_title(f"Average Runs Share at Position {pos}")
        st.pyplot(fig1)

        #   Strike Rate
        fig2, ax2 = plt.subplots(figsize=(4, 4))
        ax2.pie(
            [p1_stats["avg_sr"], p2_stats["avg_sr"]],
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )
        ax2.set_title(f"Strike Rate Share at Position {pos}")
        st.pyplot(fig2)

        #  30+ Consistency 
        fig3, ax3 = plt.subplots(figsize=(4, 4))
        ax3.pie(
            [p1_stats["consistency_30"], p2_stats["consistency_30"]],
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )
        ax3.set_title(f"30+ Consistency Share at Position {pos}")
        st.pyplot(fig3)

        #  Boundary % 
        fig4, ax4 = plt.subplots(figsize=(4, 4))
        ax4.pie(
            [p1_stats["boundary_pct"], p2_stats["boundary_pct"]],
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )
        ax4.set_title(f"Boundary % Share at Position {pos}")
        st.pyplot(fig4)
