import pandas as pd
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
# 2. BASIC STATISTICS
# ==========================================

print("\nCORRELATION VALUES:")

print(
    df[["Study_Hours", "Attendance_Pct", "Marks"]].corr()
)

# ==========================================
# 3. VISUALIZATION SETTINGS
# ==========================================

sns.set_theme(style="whitegrid")

plt.figure(figsize=(16, 10))

# ==========================================
# GRAPH 1: BAR CHART
# Final Marks by Student
# ==========================================

plt.subplot(2, 3, 1)

sns.barplot(
    x="Name",
    y="Marks",
    data=df
)

plt.title("1. Final Marks by Student")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=45)


# ==========================================
# GRAPH 2: SCATTER PLOT
# Study Hours vs Marks
# ==========================================

plt.subplot(2, 3, 2)

sns.regplot(
    x="Study_Hours",
    y="Marks",
    data=df
)

plt.title("2. Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")


# ==========================================
# GRAPH 3: BOX PLOT
# Distribution of Marks
# ==========================================

plt.subplot(2, 3, 3)

sns.boxplot(
    y=df["Marks"]
)

plt.title("3. Distribution of Marks")
plt.ylabel("Marks")


# ==========================================
# GRAPH 4: CORRELATION HEATMAP
# ==========================================

plt.subplot(2, 3, 4)

numeric_df = df[
    ["Study_Hours", "Attendance_Pct", "Marks"]
]

correlation_matrix = numeric_df.corr()

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("4. Correlation Heatmap")


# ==========================================
# GRAPH 5: ATTENDANCE DISTRIBUTION
# ==========================================

plt.subplot(2, 3, 5)

sns.histplot(
    df["Attendance_Pct"],
    kde=True,
    bins=5
)

plt.title("5. Attendance Distribution")
plt.xlabel("Attendance %")
plt.ylabel("Number of Students")


# ==========================================
# 4. SAVE THE DASHBOARD
# ==========================================

plt.tight_layout()

plt.savefig(
    "week2_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()