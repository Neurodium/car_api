import tensorflow as tf
import segmentation_models as sm
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np


# API version
__version__ = "0.1.0"

# load segmentation model
custom_obj = {}
custom_obj['dice_loss'] = sm.losses.DiceLoss()
custom_obj['iou_score'] = sm.metrics.IOUScore()
custom_obj['f1-score'] = sm.metrics.FScore()

model = tf.keras.models.load_model('model/model.h5', custom_objects=custom_obj,
                                   compile=True, options=None)

BACKBONE = 'densenet169'
img_height, img_width = 256, 256


def get_prediction(image_filename):
    """
        get segmetned image from image filename
    """
    image = img_to_array(load_img(image_filename,
                                  target_size=(img_height, img_width))
                         )
    preprocess_input = sm.get_preprocessing(BACKBONE)
    image = preprocess_input(image)
    image = image.reshape((1, 256, 256, 3))
    pred = model.predict(image)
    predict = np.zeros((1, 256, 256, 3))
    for i in range(img_width):
        for j in range(img_height):
            predict[0][i][j] = pred[0][i][j].argmax()
    predict = predict[0].tolist()
    return predict


