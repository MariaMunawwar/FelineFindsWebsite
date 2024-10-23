
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

file_path = '/content/Feline.csv'
data = pd.read_csv(file_path)

# Define feature matrix X and target vector y
X = data.drop('Illness', axis=1)
y = data['Illness']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

#Print column names with their indices
for i, column in enumerate(data.columns):
    print(f"Index: {i}, Column Name: {column}")

# Create a pipeline
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression

numeric_features = [1, 4]
categorical_features = [2, 3, 5, 6, 7, 8]

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Define the pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=1000, random_state=42))
])

# Fit the model
clf = pipeline.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Example new data
new_data = pd.DataFrame({
    'Age (Years)': [3],
    'Breed': ['Ragdoll'],
    'Gender': ['M'],
    'Weight (lbs)': [9],
    'Environment': ['Indoor'],
    'Symptom 1': ['Lethargy'],
    'Symptom 2': ['Diarrhea'],
    'Symptom 3': ['Painful abdomen']
})

# Make predictions for new data
new_predictions = clf.predict(new_data)

# Print the predictions
print("Predicted Illness:", new_predictions)

