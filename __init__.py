"""
Last updatedsud on Thu Des 16 17:22 2017
@author: Christophe
A top-level wrapper of Davi Frossard's work.
Details: http://www.cs.toronto.edu/~frossard/post/vgg16/
Also see info in ./vgg16.py.
"""

import tensorflow as tf
from functools import partial
from .vgg16 import vgg16_model

MODEL_DIR = './vgg16/vgg16_weights.npz'
sess = tf.Session()


class vgg16:
    inputs = tf.placeholder(tf.float32, [None, 224, 224, 3])
    model = vgg16_model(inputs, MODEL_DIR, sess)
    predict = partial(model.predict, sess)
    relu1_1 = model.conv1_1
    relu2_1 = model.conv2_1
    relu3_1 = model.conv3_1
    relu4_1 = model.conv4_1
    relu5_1 = model.conv5_1
    bottom = model.pool5
