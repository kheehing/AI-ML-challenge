# AI/ML challenge
 develop and deploy solution using AI


project is running on 
Python 3.10
Tensorflow 2.10
Numpy 1.23.5
Scipy 1.9.3


set up anaconda env:

1. conda create -n py310 python=3.10
2. conda activate py310
3. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
4. python -m pip install "tensorflow=2.10"

test env

import tensorflow as tf
tf.config.list_physical_devices('GPU')

tf.test.is_gpu_available() - should return true