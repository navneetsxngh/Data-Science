from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
with open('models/GNB.pkl', 'rb') as f:
    model = pickle.load(f)

# Load trained scaler
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)


@app.route('/evaluate', methods=['POST'])
def predict():

    data = {
        'Age': [float(request.form.get('Age'))],
        'EstimatedSalary': [float(request.form.get('EstimatedSalary'))]
    }

    df = pd.DataFrame(data)
    df_scaled = scaler.transform(df)

    prediction = model.predict(df_scaled)
    
    return jsonify({
        "prediction": int(prediction[0])
    })


if __name__ == '__main__':
    app.run(debug=True)