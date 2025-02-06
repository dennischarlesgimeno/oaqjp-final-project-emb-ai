import requests, json

def emotion_detector(text_to_analyse):
    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        myobj = { "raw_document": { "text": text_to_analyse } }
        response = requests.post(url, json = myobj, headers=header)
        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            emotion_predictions = formatted_response['emotionPredictions'][0]
            emotion = emotion_predictions['emotion']
            dominant_emotion = max(emotion, key=emotion.get)
    
            ## to assign scores to each label
            anger_score = emotion['anger']
            disgust_score = emotion['disgust']
            fear_score = emotion['fear']
            joy_score = emotion['joy']
            sadness_score = emotion['sadness']

            return {
            'anger': anger_score, 
            'disgust': disgust_score, 
            'fear': fear_score, 
            'joy': joy_score, 
            'sadness': sadness_score, 
            'dominant_emotion': dominant_emotion
            }
        elif response.status_code == 400:
            value = {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
            }
            return value

    except KeyError:
        return "KeyError"
        