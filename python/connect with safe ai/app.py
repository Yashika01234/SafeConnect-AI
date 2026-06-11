from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = ""
    confidence = 0
    risk = ""
    recommendation = ""

    if request.method == "POST":

        message = request.form["message"]

        prediction = model.predict([message])[0]

        probabilities = model.predict_proba([message])[0]

        confidence = round(max(probabilities) * 100, 2)

        if confidence < 50:
            prediction = "uncertain"
            risk = "Unknown"
            recommendation = "Need More Analysis"

        else:

            if prediction == "normal":
                risk = "10%"
                recommendation = "Safe Message"

            elif prediction == "spam":
                risk = "60%"
                recommendation = "Mark as Spam"

            elif prediction == "harassment":
                risk = "85%"
                recommendation = "Report User"

            elif prediction == "sexual":
                risk = "95%"
                recommendation = "Block User"

            elif prediction == "cyberbullying":
                risk = "90%"
                recommendation = "Immediate Review"

            elif prediction == "threat":
                risk = "98%"
                recommendation = "Urgent Action Required"

            elif prediction == "scam":
                risk = "92%"
                recommendation = "Block and Investigate"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        risk=risk,
        recommendation=recommendation
    )

if __name__ == "__main__":
    app.run(debug=True)