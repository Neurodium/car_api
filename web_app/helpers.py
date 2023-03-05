import numpy as np

cats = {'void': [0, 1, 2, 3, 4, 5, 6],
     'flat': [7, 8, 9, 10],
     'construction': [11, 12, 13, 14, 15, 16],
     'object': [17, 18, 19, 20],
     'nature': [21, 22],
     'sky': [23],
     'human': [24, 25],
     'vehicle': [26, 27, 28, 29, 30, 31, 32, 33, -1]}


def color_mask(mask):
    """
        color labelIds image to get the real mask image
    :param mask: photo with labels
    :return: colorized photo
    """
    new = np.zeros((mask.shape[0], mask.shape[1], 3))
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i][j] in cats['void']:
                # void
                new[i][j][0] = 0
                new[i][j][1] = 0
                new[i][j][2] = 0
            elif mask[i][j] in cats['flat']:
                # flat
                new[i][j][0] = 128
                new[i][j][1] = 0
                new[i][j][2] = 128
            elif mask[i][j] in cats['construction']:
                # construction
                new[i][j][0] = 113
                new[i][j][1] = 125
                new[i][j][2] = 126
            elif mask[i][j] in cats['object']:
                # object
                new[i][j][0] = 255
                new[i][j][1] = 255
                new[i][j][2] = 0
            elif mask[i][j] in cats['nature']:
                # nature
                new[i][j][0] = 128
                new[i][j][1] = 180
                new[i][j][2] = 70
            elif mask[i][j] in cats['sky']:
                # sky
                new[i][j][0] = 52
                new[i][j][1] = 152
                new[i][j][2] = 219
            elif mask[i][j] in cats['human']:
                # human
                new[i][j][0] = 255
                new[i][j][1] = 0
                new[i][j][2] = 0
            elif mask[i][j] in cats['vehicle']:
                # vehicle
                new[i][j][0] = 0
                new[i][j][1] = 0
                new[i][j][2] = 255
    return new


def color_prediction(prediction):
    """
        color predicted image
    :param prediction: image predicted
    :return: colorized image
    """
    for i in range(prediction.shape[0]):
        for j in range(prediction.shape[1]):
            if prediction[i][j][0] == 0:
                # void
                prediction[i][j][0] = 0
                prediction[i][j][1] = 0
                prediction[i][j][2] = 0
            elif prediction[i][j][0] == 1:
                # flat
                prediction[i][j][0] = 128
                prediction[i][j][1] = 0
                prediction[i][j][2] = 128
            elif prediction[i][j][0] == 2:
                # construction
                prediction[i][j][0] = 113
                prediction[i][j][1] = 125
                prediction[i][j][2] = 126
            elif prediction[i][j][0] == 3:
                # object
                prediction[i][j][0] = 255
                prediction[i][j][1] = 255
                prediction[i][j][2] = 0
            elif prediction[i][j][0] == 4:
                # nature
                prediction[i][j][0] = 120
                prediction[i][j][1] = 180
                prediction[i][j][2] = 70
            elif prediction[i][j][0] == 5:
                # sky
                prediction[i][j][0] = 52
                prediction[i][j][1] = 152
                prediction[i][j][2] = 219
            elif prediction[i][j][0] == 6:
                # human
                prediction[i][j][0] = 255
                prediction[i][j][1] = 0
                prediction[i][j][2] = 0
            elif prediction[i][j][0] == 7:
                # vehicle
                prediction[i][j][0] = 0
                prediction[i][j][1] = 0
                prediction[i][j][2] = 255
    return prediction