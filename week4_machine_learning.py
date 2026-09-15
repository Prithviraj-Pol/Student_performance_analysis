import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)


# ==========================================
# 1. CREATE A SYNTHETIC DATASET
# ==========================================

np.random.seed(42)

study_hours = np.random.uniform(1, 10, 100)

attendance = np.random.uniform(50, 100, 100)

# Generate marks using study hours + attendance
marks = (
    study_hours * 5
    + attendance * 0.4
    + np.random.normal(0, 5, 100)
)


df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Attendance_Pct": attendance,
    "Marks": marks
})


# ==========================================
# 2. CREATE TARGET VARIABLE
# ==========================================

# 75 or above = High Performer
df["High_Performance"] = (
    df["Marks"] >= 75
).astype(int)


print("FIRST 10 STUDENTS:")
print(df.head(10))


print("\nCLASS DISTRIBUTION:")
print(df["High_Performance"].value_counts())


# ==========================================
# 3. DEFINE FEATURES AND TARGET
# ==========================================

X = df[
    ["Study_Hours", "Attendance_Pct"]
]

y = df["High_Performance"]


# ==========================================
# 4. SPLIT DATA INTO TRAINING AND TESTING
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


print("\nDATA SPLIT:")
print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))


# ==========================================
# 5. CREATE AND TRAIN MODEL
# ==========================================

model = LogisticRegression()

model.fit(
    X_train,
    y_train
)


print("\nModel training completed.")


# ==========================================
# 6. MAKE PREDICTIONS
# ==========================================

predictions = model.predict(X_test)


# ==========================================
# 7. EVALUATE MODEL
# ==========================================

accuracy = accuracy_score(
    y_test,
    predictions
)

precision = precision_score(
    y_test,
    predictions,
    zero_division=0
)

recall = recall_score(
    y_test,
    predictions,
    zero_division=0
)

conf_matrix = confusion_matrix(
    y_test,
    predictions
)


print("\n========== MODEL RESULTS ==========")

print(
    f"Accuracy:  {accuracy * 100:.2f}%"
)

print(
    f"Precision: {precision * 100:.2f}%"
)

print(
    f"Recall:    {recall * 100:.2f}%"
)

print("\nConfusion Matrix:")
print(conf_matrix)


# ==========================================
# 8. DETAILED CLASSIFICATION REPORT
# ==========================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Low Performer",
            "High Performer"
        ],
        zero_division=0
    )
)


# ==========================================
# 9. CONFUSION MATRIX VISUALIZATION
# ==========================================

plt.figure(figsize=(7, 5))

sns.heatmap(
    conf_matrix,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=[
        "Predicted Low",
        "Predicted High"
    ],
    yticklabels=[
        "Actual Low",
        "Actual High"
    ]
)

plt.title(
    "Confusion Matrix - Student Performance"
)

plt.xlabel("Predicted")

plt.ylabel("Actual")

plt.tight_layout()

plt.savefig(
    "week4_confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()