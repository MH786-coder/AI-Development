import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

# ==== SETTINGS ====
DATA_FILE = "data.csv"
WINDOW_SIZE = 5  # last N results for training

# Ensure CSV exists with correct columns
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=['period', 'result']).to_csv(DATA_FILE, index=False)

def get_next_period():
    """Get the next period number (last period + 1)."""
    df = pd.read_csv(DATA_FILE)
    if df.empty:
        return 10001  # starting period
    return int(df['period'].iloc[-1]) + 1

def append_result(result):
    """Append the latest result to the CSV file with sequential period."""
    period = get_next_period()
    df = pd.DataFrame([[period, result]], columns=['period', 'result'])
    df.to_csv(DATA_FILE, mode='a', header=False, index=False)

def load_and_prepare_data():
    """Load and prepare training data."""
    df = pd.read_csv(DATA_FILE)

    if 'result' not in df.columns:
        raise ValueError("CSV file is missing the 'result' column. Please fix the file format.")

    df['result'] = df['result'].map({'Big': 1, 'Small': 0})
    df = df.dropna()

    if len(df) <= WINDOW_SIZE:
        return None, None

    X, y = [], []
    for i in range(WINDOW_SIZE, len(df)):
        X.append(df['result'].iloc[i-WINDOW_SIZE:i].values)
        y.append(df['result'].iloc[i])
    return X, y

def train_and_predict():
    """Train the model and predict the next move."""
    X, y = load_and_prepare_data()
    if X is None:
        print("Not enough data yet...")
        return

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    if len(X_test) > 0:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy*100:.2f}%")

    latest_sequence = X[-1]
    prediction = model.predict([latest_sequence])[0]
    proba = model.predict_proba([latest_sequence])[0]

    print("Latest history:", latest_sequence)
    print(f"Predicted Next Move: {'Big' if prediction == 1 else 'Small'}")
    print(f"Confidence - Small: {proba[0]*100:.2f}%, Big: {proba[1]*100:.2f}%")
    print("-" * 40)

print("Real-Time Prediction AI (type 'exit' to stop)")
while True:
    current_result = input("Enter current result (Big/Small): ").strip().capitalize()
    if current_result.lower() == "exit":
        break
    if current_result not in ["Big", "Small"]:
        print("Invalid input! Please enter 'Big' or 'Small'.")
        continue

    append_result(current_result)
    train_and_predict()
