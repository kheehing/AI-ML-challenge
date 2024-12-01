# Flask TensorFlow Image Classification App
This project is to develop and deploy solution using a containerized Flask application that serves a TensorFlow model for classifications of the car images(Stanford Cars Dataset)(car196). The model classifies images into different categories, and the API is exposed via a RESTful endpoint.

## Project Overview

This application is designed to:
- Load a pre-trained TensorFlow model.
- Expose a prediction API via a Flask web server.
- Accept image files through HTTP requests and return predictions.

### Features:
- **Image Classification**: Classifies images based on a pre-trained TensorFlow model.
- **Flask API**: RESTful API exposed via Flask to accept images and return predictions.
- **Containerized with Docker**: The application is packaged as a Docker container for easy deployment.

## Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**: [Install Docker](https://www.docker.com/get-started) to build and run the containerized application.
- **Python** (for local testing): [Install Python](https://www.python.org/downloads/) if you'd like to test locally before containerizing.

## Environment
I ran this project on both my PC and my laptop so while one device is training, I can work on other parts of the project on another device.

### Windows PC 
Python version: 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)]
Operating System: Windows-11-10.0.22631-SP0

Library Versions:
scipy: 1.14.0
h5py: 3.11.0
torch: 2.3.1
torchvision: 0.18.1
tensorflow: 2.16.2
tensorflow_datasets: 4.9.7
matplotlib: 3.9.1
numpy: 1.26.4
Pillow: 10.2.0
keras: 3.4.1
sklearn: Not Installed

## Docker

I installed the docker with the following commands:
'''
docker build -t flask-tensorflow-app .
'''

I ran the docker image with the follow commands:
'''
docker run -p 5000:5000 flask-tensorflow-app
'''


### Experimented with running Tensorflow on GPU
I have tried to run the project on the GPU instead but there seems to be error when running the code so i abadoned this approach.

Environment / Library Versions:
Python 3.10
Tensorflow 2.10
Numpy 1.23.5
Scipy 1.9.3

setting up anaconda env:
1. conda create -n py310 python=3.10
2. conda activate py310
3. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
4. python -m pip install "tensorflow=2.10"

#### testing GPU env
import tensorflow as tf
tf.config.list_physical_devices('GPU')

tf.test.is_gpu_available() # should return true