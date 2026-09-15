import pandas as pd
from scipy.stats import ttest_ind
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


# ==========================================
# 1. LOAD AND CLEAN THE DATA
# ==========================================

df = pd.read_csv("student_data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing Study Hours with median
df["Study_Hours"] = df["Study_Hours"].fillna(
    df["Study_Hours"].median()
)

# Fill missing Attendance with mean
df["Attendance_Pct"] = df["Attendance_Pct"].fillna(
    df["Attendance_Pct"].mean()
)

# Remove students with missing Marks
df = df.dropna(subset=["Marks"])


print("CLEANED DATA:")
print(df)


# ==========================================
# 2. CREATE TWO STUDY GROUPS
# ==========================================

# High Study = 5 hours or more
high_study = df[
    df["Study_Hours"] >= 5
]["Marks"]

# Low Study = less than 5 hours
low_study = df[
    df["Study_Hours"] < 5
]["Marks"]


# ==========================================
# 3. DISPLAY GROUP INFORMATION
# ==========================================

print("\n--- STUDY GROUPS ---")

print("High Study Marks:")
print(high_study.tolist())

print("\nLow Study Marks:")
print(low_study.tolist())


print("\n--- GROUP AVERAGES ---")

print(
    f"High Study Mean: {high_study.mean():.2f}"
)

print(
    f"Low Study Mean: {low_study.mean():.2f}"
)


# ==========================================
# 4. INDEPENDENT T-TEST
# ==========================================

t_stat, p_value = ttest_ind(
    high_study,
    low_study
)

print("\n--- T-TEST RESULTS ---")

print(
    f"T-statistic: {t_stat:.4f}"
)

print(
    f"P-value: {p_value:.4f}"
)


# ==========================================
# 5. INTERPRET THE RESULT
# ==========================================

alpha = 0.05

print("\n--- CONCLUSION ---")

if p_value < alpha:

    print(
        "Reject the Null Hypothesis (H0)."
    )

    print(
        "There is statistically significant "
        "evidence of a difference between "
        "the two study groups."
    )

else:

    print(
        "Fail to reject the Null Hypothesis (H0)."
    )

    print(
        "There is not enough statistical evidence "
        "to conclude that the two groups differ."
    )


# ==========================================
# 6. VISUALIZE THE TWO GROUPS
# ==========================================

group_data = pd.DataFrame({
    "Study Group": (
        ["High Study"] * len(high_study)
        + ["Low Study"] * len(low_study)
    ),
    "Marks": list(high_study) + list(low_study)
})


plt.figure(figsize=(8, 5))

sns.boxplot(
    x="Study Group",
    y="Marks",
    data=group_data
)

sns.stripplot(
    x="Study Group",
    y="Marks",
    data=group_data,
    color="black",
    size=8
)

plt.title(
    "Marks Comparison: High Study vs Low Study"
)

plt.xlabel("Study Group")
plt.ylabel("Marks")

plt.tight_layout()

plt.savefig(
    "week3_hypothesis_test.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()