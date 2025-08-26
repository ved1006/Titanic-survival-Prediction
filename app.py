from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained Titanic ML model
model = joblib.load("titanic_model.pkl")  # Make sure this file is in the same folder

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Predict route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get values from form
        pclass = int(request.form["pclass"])
        sex = int(request.form["sex"])
        age = float(request.form["age"])
        sibsp = int(request.form["sibsp"])
        parch = int(request.form["parch"])
        fare = float(request.form["fare"])
        embarked = int(request.form["embarked"])  

        # Prepare input
        features = np.array([pclass, sex, age, sibsp, parch, fare, embarked]).reshape(1, -1)
        prediction = model.predict(features)[0]

        # Create result string
        result = "Survived" if prediction == 1 else "Did Not Survive"
        return render_template("result.html", result=result)

    except Exception as e:
        return render_template("result.html", result=f"Error: {str(e)}")

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
