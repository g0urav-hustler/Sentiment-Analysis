from flask import Flask , render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import one_hot
import nltk
nltk.download(['stopwords', 'wordnet'])
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import re
import os

IMAGE_FOLDER = os.path.join('static', 'images')

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER

model = load_model('models/lstm_model.h5')
lemmatizer = WordNetLemmatizer()

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/sentiment_analysis', methods = ['GET','POST'])
def sent_analysis():
    text = request.form['text']
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    text = text.split()

    # old method
    #words = text.split()
    #word_to_id = imdb.get_word_index()
   # words = [[word_to_id[word] if (word in word_to_id and word_to_id[word] <=2000) else 0 for word in words]]
    words = [lemmatizer.lemmatize(word) for word in text if word not in stopwords.words('english')]
    words = ' '.join(words)
    one_hot_text = [one_hot(words, 5000)]
    test_text = sequence.pad_sequences(one_hot_text, maxlen = 40)

    predict_prob = model.predict(test_text)
    sentiment = ''
    if predict_prob > 0.5:
        sentiment = "Postive"
        img_file = os.path.join(IMAGE_FOLDER, 'Smiling_Emoji.png')
        
    else:
        sentiment = "Negetive"
        img_file = os.path.join(IMAGE_FOLDER, 'Sad_Emoji.png')

    percentage = (predict_prob  - 0.5)*100
    percentage = percentage[0]

    return render_template('home.html', text = text, sentiment = sentiment, sent_percent = percentage, image = img_file)


if __name__ == "__main__":
    app.run(debug = True)