import joblib
import re
import string
from flask import Flask, request, jsonify, render_template

# Load the trained vectorizer and models
vectorizer = joblib.load('vectorizer.joblib')
knn_model = joblib.load('knn_model_Update.joblib')
svm_model = joblib.load('svc_model_update.pkl')

app = Flask(__name__)

def convertData(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W", " ", text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

def vectorize(text):
    txt_p = convertData(text)
    txt_p = vectorizer.transform([txt_p])
    return txt_p

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        model_name = data.get("model")
        text = data.get("text")

        if not text or not model_name:
            return jsonify({"error": "Missing input data."}), 400

        vectorized_text = vectorize(text)

        # Check which model to use and get prediction
        if model_name == 'svm':
            prediction = svm_model.predict(vectorized_text)
        elif model_name == 'knn':
            prediction = knn_model.predict(vectorized_text)
        else:
            return jsonify({"error": "Invalid model selected."}), 400

        # Convert prediction to native Python type for JSON serialization
        prediction_value = int(prediction[0])  # Assuming prediction[0] is a NumPy int64

        return jsonify({"prediction": prediction_value, "model": model_name})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
