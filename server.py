'''
This is the code to run a Flask server for the emotion detector service.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def em_detector():
    '''
    This function applies the emotion detector to some text that is passed
    in as a query parameter in an HTTP GET request.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = f"For the given statement, the system response is: \
        'anger': {result['anger']}, 'disgust': {result['disgust']}, \
        'fear': {result['fear']}, 'joy': {result['joy']}, and 'sadness': \
        {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."

    return output

@app.route("/")
def render_index_page():
    '''
    This function renders the Djinja template for the emotion detector's webpage.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
