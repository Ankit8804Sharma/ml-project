import pandas as pd
import matplotlib.pyplot as plt

def run_eda():

    print("\n===== STARTING EDA =====\n")

    df = pd.read_csv("Data/processed_ethereum.csv")

    print("Dataset Shape:", df.shape)
    print("\nColumns:\n", df.columns)

    print("\n===== BASIC INFO =====")
    print(df.info())

    print("\n===== MISSING VALUES =====")
    print(df.isnull().sum())

    print("\n===== STATISTICAL SUMMARY =====")
    print(df.describe())

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

    print("\n===== KEY INSIGHTS =====")

    print("\n1. Total Value:")
    print(" - Highly skewed distribution (few very large transactions)")

    print("\n2. Fee Ratio:")
    print(" - Extreme outliers detected → strong anomaly indicator")

    print("\n3. Time Gap:")
    print(" - Irregular intervals suggest burst or unusual activity")

    print("\n4. Block Gap:")
    print(" - Sudden jumps indicate irregular blockchain activity")

    print("\n===== EDA COMPLETED =====\n")


if __name__ == "__main__":
    run_eda()