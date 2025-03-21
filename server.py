""" Emotion Detection Flask API """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """ reder the index page """
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    """ Call the emotion detector API """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        ret_val = "Invalid text! Please try again!"
    else:
        ret_val = "For the given statement, the system response is" + \
        " 'anger': " + str(response['anger']) + \
        ", 'disgust': " + str(response['disgust']) + \
        ", 'fear': " + str(response['fear']) + \
        ", 'joy': " + str(response['joy']) + \
        " and 'sadness': " + str(response['sadness']) + \
        ". The dominant emotion is " + response['dominant_emotion'] + "."

    return ret_val

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    