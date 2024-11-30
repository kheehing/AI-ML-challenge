# AI/ML challenge
 develop and deploy solution using AI

## Environment
I ran this project on both my PC and my laptop so while one device is training, I can work on other parts of the project.

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

### Macbook (M1 chip)



Library Versions:








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