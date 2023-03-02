from flask import Flask, jsonify
from model import get_prediction
import os

os.environ['SM_FRAMEWORK'] = 'tf.keras'

app = Flask(__name__)

path = 'images/'
images = os.listdir(path)

@app.route('/')
def home():
    return '<p>Segmentation model</p>'


@app.route('/prediction/<int:photo_id>')
def predict_segments(photo_id):
    return jsonify(prediction=get_prediction(path + images[photo_id]))


# to run the app in a docker and access to it
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
