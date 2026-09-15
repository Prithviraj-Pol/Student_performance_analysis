import pandas as pd
import matplotlib
# use a non-GUI backend so scripts run on machines without Tcl/Tk
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD THE DATA
df = pd.read_csv("student_data.csv")

print("ORIGINAL MESSY DATA:")
print(df)

# 2. CLEAN THE DATA

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

print("\nCLEANED DATA:")
print(df)

# 3. BASIC STATISTICS

print("\nQUICK STATISTICS:")

print(f"Total valid students: {len(df)}")

print(f"Average Mark: {df['Marks'].mean():.1f}")

print(f"Highest Mark: {df['Marks'].max()}")

# 4. CREATE VISUALIZATIONS

plt.figure(figsize=(15, 5))

# Graph 1 - Attendance Distribution
plt.subplot(1, 3, 1)

sns.histplot(
    df["Attendance_Pct"],
    bins=5
)

plt.title("Attendance Distribution")
plt.xlabel("Attendance %")
plt.ylabel("Number of Students")


# Graph 2 - Study Hours vs Marks
plt.subplot(1, 3, 2)

sns.scatterplot(
    x="Study_Hours",
    y="Marks",
    data=df,
    s=100
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")


# Graph 3 - Marks by Student
plt.subplot(1, 3, 3)

sns.barplot(
    x="Name",
    y="Marks",
    data=df
)

plt.title("Final Marks by Student")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save graphs to a file (headless-friendly)
output_path = "analysis.png"
plt.savefig(output_path)
print(f"Saved figure to {output_path}")