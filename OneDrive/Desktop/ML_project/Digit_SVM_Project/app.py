from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['pixels']

    pixels = np.array(data).reshape(1, -1)

    pred = model.predict(pixels)[0]
    prob = model.predict_proba(pixels)

    confidence = round(max(prob[0]) * 100, 2)

    return jsonify({
        "prediction": int(pred),
        "confidence": confidence
    })

if __name__ == "__main__":
    app.run(debug=True)