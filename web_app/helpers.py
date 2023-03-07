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
                prediction[i][j] = [0, 0, 0]
            elif prediction[i][j][0] == 1:
                # flat
                prediction[i][j] = [128, 0, 128]
            elif prediction[i][j][0] == 2:
                # construction
                prediction[i][j] = [113, 125, 126]
            elif prediction[i][j][0] == 3:
                # object
                prediction[i][j] = [255, 255, 0]
            elif prediction[i][j][0] == 4:
                # nature
                prediction[i][j] = [120, 180, 70]
            elif prediction[i][j][0] == 5:
                # sky
                prediction[i][j] = [52, 152, 219]
            elif prediction[i][j][0] == 6:
                # human
                prediction[i][j] = [255, 0, 0]
            elif prediction[i][j][0] == 7:
                # vehicle
                prediction[i][j] = [0, 0, 255]
    return prediction