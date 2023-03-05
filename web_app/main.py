import numpy as np
from flask import Flask, render_template
from urllib.request import urlopen
import json
import os
from skimage import io
from helpers import color_prediction, color_mask



app = Flask(__name__)

path_photos = 'static/photos/'
path_masks = 'static/labels/'
path_predictions = 'static/predictions/'
url = 'https://car-predict-23.herokuapp.com/prediction/'

@app.route('/')
def home():  # homepage of list of images and urls for prediction
    images = os.listdir(path_photos)
    img_pth = []
    urls = []
    for image in images:
        img_pth.append(f"photos/{image}") # images
        urls.append(f"segmentation/{image}") # urls
    return render_template('home.html', len=len(img_pth), images=img_pth, urls=urls)

@app.route('/segmentation/<photo>')
def seg_images(photo):
    # get prediction from inference model
    response = urlopen(url + photo)
    data_json = json.loads(response.read())
    pred = np.array(data_json['prediction'])
    # create a colorized photo based on the labels predicted
    pred = color_prediction(pred)
    pred_fname = photo.replace("_leftImg8bit.png", "_prediction.png")
    # save predicted image
    io.imsave(path_predictions + pred_fname, pred)
    mask_fname = photo.replace("_leftImg8bit.png", "_color_mask.png")
    return render_template('predict.html',
                           photo=f'photos/{photo}',
                           mask=f'labels/{mask_fname}',
                           seg=f'predictions/{pred_fname}')

# to run the app in a docker and access to it
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
