from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

# to define route for home page
@app.route('/')
def home():
    return render_template('index.html')

#to define route for emotionDetector
@app.route('/emotionDetector')
def emotionDetector():
    user_input = request.args.get('textToAnalyze')
    result = emotion_detector(user_input)
    return(f"For the given statement, the system resonse is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}, 'dominant_emotion': {result['dominant_emotion']}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)