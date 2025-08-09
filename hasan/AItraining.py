import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# --- 1. Load data ---
df = pd.read_csv('game_data.csv', names=['period', 'result'])

# Convert Big/Small to 1/0
df['result'] = df['result'].map({'Big': 1, 'Small': 0})

# --- 2. Create features from last N results ---
N = 50  # how many previous results to use
X, y = [], []

for i in range(N, len(df)):
    X.append(df['result'].iloc[i-N:i].values)  # last N moves
    y.append(df['result'].iloc[i])             # current move

X = np.array(X)
y = np.array(y)

# --- 3. Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# --- 4. Train logistic regression ---
model = LogisticRegression()
model.fit(X_train, y_train)

# --- 5. Evaluate ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

# --- 6. Predict next move from latest data ---
latest_sequence = df['result'].iloc[-N:].values.reshape(1, -1)
prediction = model.predict(latest_sequence)[0]
proba = model.predict_proba(latest_sequence)[0]

print("\nLatest history:", latest_sequence.tolist()[0])
print(f"Predicted Next Move: {'Big' if prediction == 1 else 'Small'}")
print(f"Confidence - Small: {proba[0]*100:.2f}%, Big: {proba[1]*100:.2f}%")
