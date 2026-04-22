def run_logistic():
    import pandas as pd
    import joblib
    import os
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import (
        classification_report,
        confusion_matrix,
        accuracy_score,
        precision_score,
        recall_score,
        f1_score
    )
    from sklearn.preprocessing import StandardScaler
    from imblearn.over_sampling import SMOTE

    print("\n===== LOGISTIC REGRESSION =====")

    # -----------------------------
    # LOAD DATA
    # -----------------------------
    df = pd.read_csv("Data/new dataset/labeled_data.csv")

    features = [
        "Value_z",
        "GasCost_z",
        "GasEfficiency_z",
        "TimeGap_z",
        "BlockGap_z"
    ]

    X = df[features].fillna(0)
    y = df["label"]

    # -----------------------------
    # TRAIN-TEST SPLIT
    # -----------------------------
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # -----------------------------
    # SCALING
    # -----------------------------
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # -----------------------------
    # HANDLE IMBALANCE (IMPORTANT)
    # -----------------------------
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    # -----------------------------
    # MODEL
    # -----------------------------
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train, y_train)

    # -----------------------------
    # PREDICTION
    # -----------------------------
    preds = model.predict(X_test)

    # -----------------------------
    # FULL REPORT
    # -----------------------------
    print("\n Confusion Matrix:")
    print(confusion_matrix(y_test, preds))

    print("\n Classification Report:")
    print(classification_report(y_test, preds))

    # -----------------------------
    # SAVE MODEL + SCALER (FOR UI)
    # -----------------------------
    os.makedirs("Models", exist_ok=True)

    joblib.dump(model, "Models/logistic.pkl")
    joblib.dump(scaler, "Models/logistic_scaler.pkl")

    print("\n Model + Scaler saved (ready for UI)")


if __name__ == "__main__":
    run_logistic()