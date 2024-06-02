from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

def preprocess(payload):
    country = {
        'Europe': 0.,
        'Japan': 0.,
        'USA': 0.,
    }
    if payload['Country'] == 'Europe':
        country['Europe'] = 1
    if payload['Country'] == 'Japan':
        country['Japan'] = 1
    if payload['Country'] == 'USA':
        country['USA'] = 1

    return np.array([
        float(payload['Cylinders']),
        float(payload['Displacement']),
        float(payload['Horsepower']),
        float(payload['Weight']),
        float(payload['Acceleration']),
        float(payload['ModelYear']),
        float(payload['Europe']),
        float(payload['Japan']),
        float(payload['USA']),
    ])

@app.route("/")
def home():
    return "<h3>텐서플로 자동차 연비 예측 플라스크 서비스 컨테이너</h3>"

@app.route("/predict", methods=['POST'])
def predict():
    """
    Input sample:
    {
        "Cylinders": 8,
        "Displacement": 390.0,
        "Horsepower": 190,
        "Weight": 3850,
        "Acceleration": 8.5,
        "ModelYear": 2019,
        "Country": "USA",
    }

    Output sample:
    {
        "MPG": [16.075947]
    }
    """
    model = tf.keras.models.load_model('./mlp-model')
    preprocessed_payload = preprocess(request.json)
    prediction = list(model(preprocessed_payload)[0].numpy())
    prediction = [float(x) for x in prediction]
    return jsonify({'MPG': prediction})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)