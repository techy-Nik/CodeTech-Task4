import pandas as pd
import pickle 


loaded_model = pickle.load(open("C:/Users/harik/OneDrive/Desktop/Desktop/Desktop Projects/BMI APP/trained_model.sav", 'rb'))



bmi_category_mapping = {
    0: "Extremely Weak",
    1: "Weak",
    2: "Normal",
    3: "Overweight",
    4: "Obesity",
    5: "Extreme Obesity"
}

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