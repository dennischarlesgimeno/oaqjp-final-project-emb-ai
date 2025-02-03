from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")
app.run(debug=True, port=5000)

#to define route for emotionDetector
@app.route('/emotionDetector')
def emotionDetector():
    user_input = request.args.get('userinput')
    result = emotion_detector(user_input)
    return(f"For the given statement, the system resonse is 'anger': {result['anger']}, 'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, 'sadness': {result['sadness']}, 'dominant_emotion': {result['dominant_emotion']}")
