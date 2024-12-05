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

## Installation

1.  ***Clone repository***
``` bash
git clone https://github.com/kheehing/AI-ML-challenge
```
2.  ***Build docker img***  
   Change directory(cd) to where the repository is located.
``` bash
docker build -t flask-tensorflow-app .
```
3.1  ***Run docker container***
``` bash
docker run -p 5000:5000 flask-tensorflow-app
```
3.2  ***For macbook I have to run it on 5001:5000***
``` bash
docker run -p 5001:5000 flask-tensorflow-app
```


## API Endpoints
`POST /predict`
This endpoint accepts image files and returns predictions.

Request:
URL: `http://127.0.0.1:5000/predict`
Method: `POST`
Content-Type: `multipart/form-data`
Body: Upload an image file under the field name file.

Exmaple of how I `request` (under `testing request` in `test.ipynb`)

``` python
import os, re
import requests

# Define the API endpoint
API_URL = "http://127.0.0.1:5000/predict"


# Path to main folder
IMAGE_FOLDER = "data/cars196/test/"

total = 0
match = 0

# Loop through all subfolders in the directory
for root, dirs, files in os.walk(IMAGE_FOLDER):
    for dir_name in dirs:
        folder_path = os.path.join(root, dir_name)
        carType = re.search(r'([^/]+)$', folder_path).group(1)
        
        # Iterate over all images in the folder
        for image_name in os.listdir(folder_path):
            # Construct the full path to the image
            image_path = os.path.join(folder_path, image_name)
        
            # Ensure the file is an image (you can extend this check for other formats if needed)
            if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    # Open the image file in binary mode
                    with open(image_path, 'rb') as image_file:
                        # Send POST request with the image
                        response = requests.post(API_URL, files={'file': image_file})
                        
                    # Parse and print the response
                    if response.status_code == 200:
                        total += 1
                        predicted_label = response.json().get('predicted_label')
                        print(f'{predicted_label} : {carType}')
                        if predicted_label == carType:
                            match += 1
                        #print(f"Prediction for {image_name}: {response.json()}")
                    else:
                        total += 1
                        print(f"Failed to get prediction for {image_name}. Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error processing {image_name}: {e}")
                    print(f"response: {response.json()}")
```

Response:
Content-Type: `application/json`
Body: JSON object containing the predicted label and the confidence score.
```
{
  "predicted_label": "Bugatti Veyron 16.4 Coupe 2009",
  "confidence": 0.435992032289505
}
```

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

### Experimented with running Tensorflow on GPU
I have tried to run the project on the GPU instead but there seems to be error which I could not debug when running the code so i abandoned this approach.

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
