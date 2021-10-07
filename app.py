from flask import Flask , render_template, request
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
import pandas as pd
import numpy as np
import re
import os

IMAGE_FOLDER = os.join.path('static', 'images')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

def init():
    global model,graph

    model = load_model('sentiment_analysis.h5')
    graph = tf.get_default_graph()

@app.route('/', method = ['GET','POST'])
def home():

    return render_template('home.html')

@app.route('/sentiment_analysis', method = ['GET','POST'])
def sent_analysis():
    text = request.form['text']
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    words = text.split()

    word_to_id = imdb.get_word_index()
    words = [[word_to_id[word] if (word in word_to_id and word_to_id[word] <=2000) else 0 for word in words]]
    x_test = sequence.pad_sequences(word, maxlen = 2000)

    predict_prob = model.predict(x_text)
    sentiment = ''
    if predict_prob > 0.5:
        sentiment = "Postive"
        img_file = os.path.join(IMAGE_FOLDER, 'Smilling_Emoji.png')
        
    else:
        sentiment = "Negetive"
        img_file = os.path.join(IMAGE_FOLDER, 'Sad_Emoji.png')

    percentage = np.round(predict_prob  - 0.5)*100

    return render_template('home.html', text = text, sentiment = sentiment, sent_percent = percentage, image = img_file)


if __name__ == "__main__":
    init()
    app.run(debug = True)