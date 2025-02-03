from EmotionDetection.emotion_detection import emotion_detector

# to list predetermined inputs
inputs = ['I am glad this happened', 'I am really mad about this', 'I feel disgusted just hearing about this','I am so sad about this','I am really afraid that this will happen']

# test loop
for text_to_analyse in inputs:
    result = emotion_detector(text_to_analyse)['dominant_emotion']
    print(f"{text_to_analyse} {result}")
