import pandas as pd
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify
from matplotlib import pyplot as plt
from tensorflow.keras.models import load_model

## disable cuda
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

# loading H5 model
model = load_model('models/first.h5')

# API
app = Flask(__name__)

# Load the model
model = load_model('models/first.h5')

# Load the dict
def load_label_mapping(file_path):
    label_to_number = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into label and number
            label, number = line.rsplit(':', 1)  # Split from the right
            label_to_number[int(number.strip())] = label.strip()
    return label_to_number

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Check if an image is included in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'})
        
        file = request.files['file']

        # Ensure the file is not empty
        if file.filename == '':
            return jsonify({'error': 'No file selected'})

        # Read the image file as binary data
        image_bytes = file.read()

        # Decode the image using TensorFlow
        image = tf.image.decode_jpeg(image_bytes, channels=3)
        image = tf.image.resize(image, (224, 224))
        image = image / 255.0

        # Expand dimensions to match model input
        input_data = np.expand_dims(image, axis=0)

        # Make prediction
        prediction = model.predict(input_data)

        # Load the label-to-number mapping
        label_to_number = load_label_mapping('data/label_to_number.txt')

        # Get the index of the highest probability
        predicted_index = np.argmax(prediction[0])

        # Map the index to the class name
        predicted_label = label_to_number.get(predicted_index, "Unknown")
        confidence = prediction[0][predicted_index]

        # Return human-readable output
        return jsonify({
            'predicted_label': predicted_label,
            'confidence': float(confidence),
            # 'raw_output': prediction.tolist()  # Optional: Include raw prediction for debugging
        })

    except Exception as e:
        return jsonify({'error': str(e)})



app.run(debug=True, host='0.0.0.0')
