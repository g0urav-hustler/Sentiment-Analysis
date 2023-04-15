<h1 align = 'center' >Thought Analyzer  </h1>

**Web** : https://thought-analyzer.onrender.com

**Api :** https://1wna3xut2i.execute-api.us-east-1.amazonaws.com/Thought-anlyzer-app/predict_func



## Overview 
#### It was website that predicts your thought wheather it is positive or negetive.

## Technical Aspects

### About Dataset

For this problem we are using twitter messages dataset.

Download dataset from [Kaggle](https://www.kaggle.com/kazanova/sentiment140)

```
target: Polarity of the tweet (0 = negative, 2 = neutral, 4 = positive)

ids: The ids of the tweet (2048)

date: the date of the tweet (Sat May 16 23:58:44 UTC 2009)

flag: The query (lyx). If there is no query, then this value is NO_QUERY.

user: The user that tweeted (robotickilldozr)

text: Messages from the users

```

### Data Preprocessing

- Only target and text data is useful, drop other columns
- Clean the messages, remove unwanted symbols like @,#,!,& etc.
- Stemming the words in the message. For that I use PorterStemmer. For more info use [reference](https://www.geeksforgeeks.org/python-stemming-words-with-nltk/)
- Words into numbers. For that I use imdb word library. It has more than 50,000 words. 
- Padding the messages so that length of all messages should be equal. To understand padding use [reference](https://www.tensorflow.org/guide/keras/masking_and_padding)

Now the data is ready for building the model.

#### About Models
1. First build simple Logistic Regression model. It's accuracy was only around **53%**.
2. Build Random Forest Classifier that gives little bit better accuracy of around **57%**.
3. Now build a LSTM model which gives a better accuracy of around **73%**.

Selecting LSTM model as final model as it gives best accuracy amoung all model.

### Technology Used 
![](https://img.shields.io/badge/Python-3.7-blue.svg)
![](https://img.shields.io/badge/TF-2.6.0-blue.svg)
![](https://img.shields.io/badge/NLTK-3.6.3-blue.svg)
![](https://img.shields.io/badge/Flask-1.1.1-blue.svg)
![](https://img.shields.io/badge/Docker-20.10.12-blue.svg)
![](https://img.shields.io/badge/Heroku-7.59.1-blue.svg)

----------------------------
## Setup and Intallation

Open your terminal and change the directory to project folder
```
$ cd [your-project-folder]
```
Clone the repo in your exiting project folder
```
$ git clone https://github.com/g0urav-hustler/Thought-Analyzer.git
```
Making virual environment 
```
$ python3 -m [your-virtual-env-name] [project-directory-path]
```
Activate virtual environment 
```
$ source [your-virtual-env-name]/bin/activate
```
Install all the requirements
```
$ pip install -r requirements.txt
```
Now your setup has been completed, you can run this app by
```
python app.py
```
----------------------------
## Dockerization and Deployment
The app has deploy on heroku platform using a docker container.

Pre-requisite: Docker and Heroku intalled on your computer.

To install Docker, see [Reference](https://runnable.com/docker/getting-started/)

To install Heroku see [Reference](https://devcenter.heroku.com/articles/heroku-cli)

Docker command to build the docker container
```
$ docker build -t [your-app-name]:latest .
 ```
To run the docker container
``` 
$ docker run -p80:8000 [your-app-name]
```
To see docker container 
```
$ docker images
```
Login to your heroku account
```
$ heroku container:login
```
Create a web app on heroku
```
$ heroku create [your-app-name]
```
Tag your docker container as heroku web app
```
$ docker tag [your-app-name]:latest registry.heroku.com/[your-app-name]/web
```
Pushing the docker container on the web
```
$ docker push registry.heroku.com/[your-app-name]/web
```
Releasing the web app
```
$ heroku container:release web -a [your-app-name]
```

----------------------------
## Repository Overview
```
├── models
│   └──lstm_model.h5
├── notebooks 
│   └──thought_analyzer.ipynb
├── readme resources
├── static 
│   └──style.css
├── templates
│   └── home.html
├── Dockerfile
├── LICENSE
├── README.md
├── app.py
└── requirements.txt
```
----------------------------
MIT License

Copyright (c) 2021 Gourav Chouhan

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
© 2021 GitHub, Inc.
Terms
Privacy

----------------------------

### If you like this repo and it is useful, please don't forget to give a ⭐.
