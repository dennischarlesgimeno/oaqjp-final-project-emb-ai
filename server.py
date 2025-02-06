"""This module contains the codes for the server including error handling"""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# error handler for 400
@app.errorhandler(400)
def bad_request_error():
    """To handle 400 Bad Request errors"""
    response = jsonify({'error': 'Bad Request', 'message': 'Invalid text! Please try again!'})
    response.status_code = 400
    return response

# to define route for home page
@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html')

# Define route for emotionDetector
@app.route('/emotionDetector')
def emotion_detector_serv():
    """handle emotion detection requests"""
    user_input = request.args.get('textToAnalyze')
    result = emotion_detector(user_input)
    response = (
    f"For the given statement, the system resonse is 'anger': {result['anger']}, "
    f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
    f"'sadness': {result['sadness']}, 'dominant_emotion': {result['dominant_emotion']}"
    )
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
