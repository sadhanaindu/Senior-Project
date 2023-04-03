# Output the model's predictions.

from tensorflow.keras.models import model_from_json # Since we are importing the models from a JSON file. 
from tensorflow.python.keras.backend import set_session
import numpy as np

import tensorflow as tf

# These lines deal with memory allocation on the GPU. 
# We *might* need to change these settings in case the model doesn't run as it should locally, but I'm currently not sure how. 
# The course doesn't mention it so we might need to find out. 
config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.15
session = tf.compat.v1.Session(config=config)
set_session(session)

# Define facial expressions class. 
class FacialExpressionModel(object):

    # Create list of emotions. 
    EMOTIONS_LIST = ["Angry", "Disgust",
                     "Fear", "Happy",
                     "Neutral", "Sad",
                     "Surprise"]

    def __init__(self, model_json_file, model_weights_file):
        # load model from JSON file
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        # load weights into the new model
        self.loaded_model.load_weights(model_weights_file)
        #self.loaded_model.compile()
        self.loaded_model.make_predict_function()

    def predict_emotion(self, img):
        global session
        set_session(session)
        self.preds = self.loaded_model.predict(img)
        return FacialExpressionModel.EMOTIONS_LIST[np.argmax(self.preds)]
