<h1 align = 'center' >Thought Analyzer  </h1>

**Website** = [Thought Analyzer](https://thought-analyzer.herokuapp.com/)

## Overview 
#### It was website that predicts your thought wheather it is positive or negetive.

### Web view:
![]()
----------------------------
### Technology Used 
![](https://img.shields.io/badge/Python-3.7-blue.svg)
![](https://img.shields.io/badge/TF-2.6.0-blue.svg)
![](https://img.shields.io/badge/TF-2.6.0-blue.svg)
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
$ git clone https://github.com/g0urav-hustler/Crop-Production-Optimization.git
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