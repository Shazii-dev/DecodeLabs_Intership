# ==========================================
# DecodeLabs - Project 2: Data Classification
# Supervised Learning Pipeline
# ==========================================

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score

def run_classification_pipeline():
    print("=== PROJECT 2 PIPELINE INITIATED ===\n")

    # 1. RAW MATERIAL: Iris Domain 
    print("[1] Loading Iris Domain Data...")
    iris = load_iris()
    X = iris.data  # Features (like Sepal Length)
    y = iris.target # Classes (Types of flowers)

    # 2. THE MASTER BLUEPRINT: Train-Test Split [cite: 289, 294]
    # Splitting data into 80% Train and 20% Test 
    # shuffle=True ensures the data is randomized (shuffled) 
    print("[2] Splitting Data (80% Training, 20% Testing) and Shuffling...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, shuffle=True)

    # 3. TUNING THE ENGINE: K-Nearest Neighbors Algorithm [cite: 326, 327, 332]
    # Setting K=5. Avoiding K=1 to prevent Noise/Overfitting.
    print("[3] Initializing KNeighborsClassifier (K=5)...")
    model = KNeighborsClassifier(n_neighbors=5)

    # 4. THE WORKFLOW: Fit and Predict [cite: 334]
    print("[4] Training the model and making predictions...")
    model.fit(X_train, y_train) # Training the model 
    predictions = model.predict(X_test) # Testing the model on new data 

    # 5. OUTPUT VALIDATION & DIAGNOSTIC TOOLS [cite: 339, 341]
    print("\n=== OUTPUT VALIDATION ===")
    
    # Accuracy Metric 
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy:  {accuracy * 100:.2f}%")
    
    # Precision and F1 Score (The Harmonic Mean) [cite: 350, 351]
    # average='macro' is used because Iris has 3 classes, not just 2.
    precision = precision_score(y_test, predictions, average='macro')
    f1 = f1_score(y_test, predictions, average='macro')
    print(f"Precision: {precision:.4f}")
    print(f"F1 Score:  {f1:.4f} (Harmonic Mean)")
    
    # The Diagnostic Tool: Confusion Matrix [cite: 341]
    # Maps out TP, FP, TN, FN (Missed Detections) [cite: 343, 344, 346, 347, 348]
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, predictions)
    print(cm)
    
    print("\n=== PIPELINE COMPLETED ===")

# Run the pipeline
if __name__ == "__main__":
    run_classification_pipeline()