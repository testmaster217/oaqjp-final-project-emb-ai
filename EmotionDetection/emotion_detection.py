import json
import requests

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    response = requests.post(url, json=obj, headers=headers)

    if response.status_code == 400:
        emotions = {
            'joy': None,
            'anger': None,
            'sadness': None,
            'fear': None,
            'disgust': None,
            'dominant_emotion': None
        }
    elif response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        max_score = 0
        dominant_emotion = ""
        for emotion in emotions.keys():
            if emotions[emotion] > max_score:
                max_score = emotions[emotion]
                dominant_emotion = emotion
        emotions["dominant_emotion"] = dominant_emotion

    return emotions