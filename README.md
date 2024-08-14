# Fake News Detection Flask App

## Overview

This project is a Flask application for detecting fake news. It uses machine learning models (SVM and KNN) to classify news content as fake or real.

## Project Structure

- `app.py`: Main Flask application script that handles routing and prediction logic.
- `vectorizer.joblib`: Pre-trained TF-IDF vectorizer used to transform text data.
- `knn_model_Update.joblib`: Pre-trained KNN model used for predictions.
- `svc_model_update.pkl`: Pre-trained SVM model used for predictions.
- `static/`: Directory for static files like CSS and JavaScript.
- `templates/`: Directory for HTML templates used for rendering web pages.
- `requirements.txt`: List of Python packages required for the project.

## Prerequisites

Before running the Flask application, ensure you have Python 3.x installed on your system. 

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/fake-news-detection.git
   cd fake-news-detection

#    - Create a virtual environment:

    -> python -m venv venv

        + Activate the virtual environment:

            -> venv\Scripts\activate

2. Install Dependencies

#    - Install the required Python packages:
    -> pip install -r requirements.txt
3. Running the Application

#   - Start the Flask application with:

    -> python app.py

4. Web Interface

#   - Open your web browser and go to http://127.0.0.1:5000.
#   - Enter the news content into the text area.
#   - Choose the model you want to use for prediction (SVM or KNN).
#   - Click the "Predict" button to see the result.

5. API Endpoint

#   - You can also interact with the application programmatically using the following API endpoint:
#   - URL: http://127.0.0.1:5000/predict
#   - Method: POST
#   - Headers: Content-Type: application/json
#   - Request Body:
    {
        "model": "svm",
        "text": "Sample news text here."
    }

#   - Response:
    {
    "prediction": 1,    
    "model": "svm"
    }

6. Troubleshooting

#   404 Not Found: Ensure that the URL is correct and that the Flask application is running.
#   500 Internal Server Error: Check the Flask application logs for detailed error information. Ensure all required #   files are present and correctly named.

#   ------------------------------- THANK FOR READING -------------------------------