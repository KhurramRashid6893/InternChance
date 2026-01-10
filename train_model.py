import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

# Create data directory if not exists
if not os.path.exists('data'):
    os.makedirs('data')

# Load the dataset
# Assuming 'data/internship_data.csv' is available in the structure
df = pd.read_csv('data/internship_data.csv')

# Define features and target
X = df[['cgpa', 'dsa', 'projects', 'hackathons', 'certs']]
y = df['shortlisted']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")