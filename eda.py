import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_curve, auc
from sklearn.linear_model import LogisticRegression


def plot_roc_curve(df):

    print("\n===== ROC CURVE =====\n")

    X = df.drop(
        ["label", "FraudFlag", "FinalScore", "anomaly_label", "IF_Score"], axis=1
    )

    X = X.select_dtypes(include=["number"])
    y = df["label"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)

    print("y_train distribution:\n", y_train.value_counts())
    print("y_test distribution:\n", y_test.value_counts())
    # Scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Model
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Probabilities
    y_prob = model.predict_proba(X_test)[:, 1]

    # ROC calculation
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    # Plot ROC
    plt.figure()
    plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
    plt.plot([0, 1], [0, 1], linestyle="--")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.legend()

    plt.show()


def run_eda():

    print("\n===== STARTING EDA =====\n")

    df = pd.read_csv("Data/labeled_data.csv")

    print("Dataset Shape:", df.shape)
    print("\nColumns:\n", df.columns)

    print("\n===== BASIC INFO =====")
    print(df.info())

    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())

    # Label Distribution
    print("\n===== LABEL DISTRIBUTION =====")
    print(df["label"].value_counts())

    plt.figure()
    df["label"].value_counts().plot(kind="bar")
    plt.title("Class Distribution (Fraud vs Normal)")
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.show()

    # Feature Engineering
    df["value_ratio"] = df["Net Value"] / (df["Total Value"] + 1)
    df["fee_to_value"] = df["TxnFee(ETH)"] / (df["Total Value"] + 1)

    # Distributions
    plt.figure()
    plt.hist(df["Total Value"], bins=50)
    plt.title("Distribution of Total Transaction Value")
    plt.xlabel("Total Value")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    plt.boxplot(df["Fee Ratio"])
    plt.title("Fee Ratio Distribution (Outliers Detection)")
    plt.ylabel("Fee Ratio")
    plt.show()

    plt.figure()
    plt.hist(df["Time Gap"], bins=50)
    plt.title("Distribution of Time Gaps Between Transactions")
    plt.xlabel("Time Gap")
    plt.ylabel("Frequency")
    plt.show()

    plt.figure()
    plt.hist(df["Block Gap"], bins=50)
    plt.title("Distribution of Block Gaps")
    plt.xlabel("Block Gap")
    plt.ylabel("Frequency")
    plt.show()

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=["number"])
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), cmap="coolwarm")
    plt.title("Feature Correlation Heatmap")
    plt.show()

    # Feature vs Label
    plt.figure()
    sns.boxplot(x="label", y="Fee Ratio", data=df)
    plt.title("Fee Ratio vs Fraud")
    plt.show()

    plt.figure()
    sns.boxplot(x="label", y="Total Value", data=df)
    plt.title("Total Value vs Fraud")
    plt.show()

    plt.figure()
    sns.boxplot(x="label", y="value_ratio", data=df)
    plt.title("Value Ratio vs Fraud")
    plt.show()

    plt.figure()
    sns.boxplot(x="label", y="fee_to_value", data=df)
    plt.title("Fee to Value vs Fraud")
    plt.show()

    # Insights
    print("\n===== KEY INSIGHTS =====")

    print("\n1. Class Imbalance:")
    print(" - Dataset is highly imbalanced with very few fraud cases")

    print("\n2. Total Value:")
    print(" - Highly skewed distribution with a few large transactions")

    print("\n3. Fee Ratio:")
    print(" - Presence of extreme outliers indicating anomalies")

    print("\n4. Time Gap and Block Gap:")
    print(" - Irregular patterns suggest unusual activity")

    print("\n5. Feature vs Fraud Behavior:")
    print(" - Fraud transactions show distinct distributions")
    print(" - Ratio-based features help capture anomalies")

    print("\n===== EDA COMPLETED =====\n")

    plot_roc_curve(df)


if __name__ == "__main__":
    run_eda()
