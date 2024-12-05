import os, re
import requests

# Define the API endpoint
API_URL = "http://127.0.0.1:5001/predict"


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

print(f'match/total (%): {match/total*100}')
print(f'match: {match}')
print(f'total: {total}')