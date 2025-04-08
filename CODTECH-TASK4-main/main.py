import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
bmi_data = pd.read_csv('bmi.csv')

# Display the first few rows of the dataset
bmi_data.head()
bmi_data.shape

# Encode the 'Gender' column
label_encoder = LabelEncoder()
bmi_data['Gender'] = label_encoder.fit_transform(bmi_data['Gender'])  # Male -> 1, Female -> 0

# Separate features (X) and target (y)
X = bmi_data[['Gender', 'Height', 'Weight']]  # Features
y = bmi_data['Index']  # Target (0 to 5)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the accuracy on the training dataset
train_predictions = model.predict(X_train)
train_accuracy = accuracy_score(y_train, train_predictions)

# Evaluate the accuracy on the testing dataset
test_predictions = model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)

# Print accuracy scores
print(f"Training Accuracy: {train_accuracy:.2f}")
print(f"Testing Accuracy: {test_accuracy:.2f}")

# Define a mapping for the BMI category
bmi_category_mapping = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obesity",
    5: "Extreme Obesity"
}

# Save the trained model using pickle
filename = "trained_model.sav"
with open(filename, 'wb') as file:
    pickle.dump(model, file)

# Load the saved model
loaded_model = pickle.load(open(filename, 'rb'))

# Function to predict BMI category
def predict_bmi():
    try:
        # Take user inputs
        gender = input("Enter Gender (Male/Female): ").strip().lower()
        height = float(input("Enter Height in cm: "))
        weight = float(input("Enter Weight in kg: "))

        # Encode gender to match the model input
        gender_encoded = 1 if gender == "male" else 0

        # Prepare the input data as a DataFrame with feature names
        input_data = pd.DataFrame([[gender_encoded, height, weight]], columns=['Gender', 'Height', 'Weight'])

        # Make prediction
        predicted_class = loaded_model.predict(input_data)[0]

        # Get the BMI category
        predicted_bmi_category = bmi_category_mapping[predicted_class]

        # Display the result
        print(f"\nPredicted BMI Category: {predicted_bmi_category}")
    except Exception as e:
        print("Error in input or prediction:", e)

# Call the function to predict BMI
predict_bmi()