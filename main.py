import subprocess
import sys
import os
import time

print("\n===== STARTING FULL PIPELINE =====\n")

start_time = time.time()


def run_step(name, command):
    print(f"\n>>> {name}...")
    t0 = time.time()
    subprocess.run([sys.executable, command], check=True)
    print(f"✓ {name} completed in {time.time() - t0:.2f}s")



# STEP 1: FEATURE ENGINEERING

run_step(
    "Running Feature Engineering",
    "src/preprocessing/feature_engineering.py"
)


# STEP 2: ISOLATION FOREST

run_step(
    "Running Isolation Forest",
    "src/models/isolation_forest.py"
)


# STEP 3: MF-UFS

run_step(
    "Running MF-UFS Algorithm",
    "src/models/mfufs.py"
)


# STEP 4: CREATE LABELS

run_step(
    "Creating Labels",
    "src/evaluation/create_labels.py"
)


# VERIFY DATA EXISTS

if not os.path.exists("Data/new dataset/labeled_data.csv"):
    raise FileNotFoundError("❌ labeled_data.csv not found!")

print("\n Dataset ready for model training\n")


# IMPORT MODELS

from src.models.logistic_model import run_logistic
from src.models.svm_model import run_svm
from src.models.knn_model import run_knn
from src.models.decision_tree_model import run_decision_tree
from src.models.random_forest import run_random_forest




print("\n===== TRAINING MODELS =====\n")

print("5. Logistic Regression")
run_logistic()

print("\n6. SVM")
run_svm()

print("\n7. KNN")
run_knn()

print("\n8. Decision Tree")
run_decision_tree()

print("\n9. Random Forest")
run_random_forest()


# DONE

total_time = time.time() - start_time

print("\n===== PIPELINE COMPLETED SUCCESSFULLY =====")
print(f" Total execution time: {total_time:.2f} seconds\n")