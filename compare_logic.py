import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu


def compare_players_stats(df: pd.DataFrame, player1: str, player2: str, pos: int) -> str:
    
    #  Filter by batting position
    pos_df = df[df["batting_position"] == pos].copy()

    #  Filter by player
    p1_df = pos_df[pos_df["batsman"] == player1]
    p2_df = pos_df[pos_df["batsman"] == player2]

    n1, n2 = len(p1_df), len(p2_df)

    # Same player check
    if player1 == player2:
        return " Please select two different players."

    # No data checks
    if n1 == 0 and n2 == 0:
        return f" Neither player has any innings at position {pos}."
    if n1 == 0:
        return f" {player1} has no innings at position {pos}."
    if n2 == 0:
        return f" {player2} has no innings at position {pos}."

    # READ FEATURES DIRECTLY FROM DATAFRAME ====

    # Runs
    p1_runs = p1_df["runs_scored"]
    p2_runs = p2_df["runs_scored"]

    # Average runs
    p1_avg = p1_runs.mean()
    p2_avg = p2_runs.mean()

    # Strike rate 
    p1_sr = p1_df["strike_rate"].mean()
    p2_sr = p2_df["strike_rate"].mean()

    # 30+ Consistency 
    p1_cons_30 = p1_df["is_30_plus"].mean() * 100
    p2_cons_30 = p2_df["is_30_plus"].mean() * 100

    # Boundary %
    if "boundary_pct" in df.columns:
        p1_bfreq = p1_df["boundary_pct"].mean()
        p2_bfreq = p2_df["boundary_pct"].mean()
    else:
        p1_bfreq = p2_bfreq = np.nan

    #  Mann–Whitney Test 
    can_test = n1 >= 3 and n2 >= 3 and n1 > 1 and n2 > 1

    if can_test:
        u_stat, p_value = mannwhitneyu(p1_runs, p2_runs, alternative="two-sided")
    else:
        u_stat, p_value = np.nan, np.nan

    #  Practical Scoring (Stats-based decision, NOT p-value only)

    p1_score = p1_avg * 0.7 + (p1_cons_30 / 10) * 0.3
    p2_score = p2_avg * 0.7 + (p2_cons_30 / 10) * 0.3

    if p1_score > p2_score:
        practical_winner = player1
    elif p2_score > p1_score:
        practical_winner = player2
    else:
        practical_winner = None

   

    lines = []

    lines.append(f"###  Comparison at batting position **{pos}**\n")

    # Player 1 stats
    lines.append(f"####  {player1}")
    lines.append(f"- Innings: **{n1}**")
    lines.append(f"- Average runs: **{p1_avg:.2f}**")
    lines.append(f"- Strike rate: **{p1_sr:.1f}**")
    lines.append(f"- 30+ consistency: **{p1_cons_30:.1f}%**")
    if not np.isnan(p1_bfreq):
        lines.append(f"- Boundary %: **{p1_bfreq:.2f}%**")
    lines.append("")

    # Player 2 stats
    lines.append(f"####  {player2}")
    lines.append(f"- Innings: **{n2}**")
    lines.append(f"- Average runs: **{p2_avg:.2f}**")
    lines.append(f"- Strike rate: **{p2_sr:.1f}**")
    lines.append(f"- 30+ consistency: **{p2_cons_30:.1f}%**")
    if not np.isnan(p2_bfreq):
        lines.append(f"- Boundary %: **{p2_bfreq:.2f}%**")
    lines.append("")

    # Test result
    if not can_test:
        lines.append(" **Note:** Sample size at this position is small. Statistical confidence is limited.\n")
    else:
        lines.append("###  Mann–Whitney U Test")
        lines.append(f"- U-statistic: **{u_stat:.2f}**")
        lines.append(f"- p-value: **{p_value:.4f}**")
        if p_value < 0.05:
            lines.append("Interpretation: The p-value is below 0.05, indicating a statistically "
        "significant difference in performance between the two players.")
        else:
            lines.append("Interpretation: The p-value is greater than 0.05, meaning the difference "
        "between the two players is not statistically significant. Cricket data "
        "has high variance and limited samples, so practical metrics like average "
        "runs, strike rate and consistency must also be considered.")
        lines.append("")

    # Final Interpretation
    lines.append("###  Final Interpretation (simple):")
    if practical_winner is None:
        lines.append(
            "Both players display similar performance at this position. "
            "Based on statistical and practical indicators, no clear winner can be identified."
        )
    else:
        other = player2 if practical_winner == player1 else player1
        lines.append(
            f"Based on overall historical performance, **{practical_winner}** appears stronger "
            f"at batting position **{pos}** compared to **{other}**."
        )
        lines.append(
            "This conclusion is based on average runs and 30+ consistency "
            "(with strike rate and boundary percentage as supporting indicators). "
            "The p-value is used as additional context, not the sole decision-maker."
        )

    return "\n".join(lines)
