# Titanic-survival-Prediction
This project predicts whether a passenger on the Titanic would have survived or not based on details like age, gender, passenger class, family onboard, fare paid, and port of embarkation.

I trained two different ML models – Logistic Regression and Random Forest – on the Titanic dataset. After training, I saved the best-performing model and integrated it into a Flask web app.

Then I deployed everything on Render 🚀 so that anyone can try it out directly from the browser

Live Demo : https://titanic-survival-prediction-2-kll7.onrender.com/

🔥 How it Works

The user enters passenger details in a simple form (class, gender, age, family count, ticket fare, etc.)

The trained ML model makes a prediction (1 = Survived, 0 = Did Not Survive)

The result is displayed instantly on the screen

🛠️ Tech Stack

->Python 

->Flask (for backend)

->Scikit-learn (ML models)

->Joblib (model saving/loading)

->HTML + CSS (frontend form)

->Render (deployment platform)
