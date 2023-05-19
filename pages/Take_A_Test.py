"""
# Testing the UI capabilities of streamlit:
"""
import cv2
import streamlit as st
from PIL import Image
import numpy as np
import time
from streamlit.components.v1 import html
import random

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import model
from model import FacialExpressionModel


st.set_page_config(page_title="Take_A_Test")

# Embed CSS styles
def set_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #f1f1f1;
        }

        h1, h2, h3 {
            font-family: "Arial", sans-serif;
            color: #333333;
        }

        p {
            font-family: "Verdana", sans-serif;
            font-size: 14px;
            color: #555555;
        }

        .button {
            background-color: #007bff;
            color: #ffffff;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }

        .button:hover {
            background-color: #0056b3;
        }

        .main-container {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 10px;
        }

        .container {
            background-color: #ffffff;
            border: 1px solid #dddddd;
            padding: 10px;
            border-radius: 5px;
        }

        .placeholder-container {
            flex: 1;
            margin-right: 10px;
        }

        .timer-container {
            flex: 1;
            margin-right: 10px;
        }

        .exercise-container {
            flex: 1;
        }

        </style>
        """,
        unsafe_allow_html=True
    )

set_css()
warning_style = """
    <style>
    .custom-warning {
        background-color: #ffcc00;
        color: #333333;
        padding: 8px;
        border-radius: 4px;
        font-weight: bold;
    }
    </style>
"""
timer_style = """
<style>
.timer-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-left: 100px;
  margin-bottom: 10px;
  width: 500px;
  height: 50px;
  background-color: #f2f2f2;
  border-radius: 10px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.timer-text {
  font-size: 24px;
  font-weight: bold;
  color: #333333;
}
</style>
"""

video_style =  """
<style>
.video-container {
  max-width: 800px;
  margin: 20px auto;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}

.video {
  width: 100%;
  height: 0;
  padding-bottom: 56.25%;
  position: relative;
}

.video iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
</style>
"""
# Render the CSS style
st.markdown(video_style, unsafe_allow_html=True)

st.markdown(timer_style, unsafe_allow_html=True)

st.markdown(warning_style, unsafe_allow_html=True)


st.markdown("# Take an Exam")
st.sidebar.header("Take Exam")

form = st.form("myForm", clear_on_submit=True)
times = form.number_input("Exam time in minutes")
times = times * 60
submit = form.form_submit_button("Send")


facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Import the face detector. 
model = FacialExpressionModel("model.json", "model_weights.h5") # Load the config for the model and the weights. 

placeholder = st.empty()
timer = st.empty()
excersise = st.empty()
FRAME_WINDOW = st.image([])
c = cv2.VideoCapture(0)

if(submit):
    
    #show or hide video after imbedding. No need to refresh
    while times >= 0:
        _, fr = c.read()
        FRAME_WINDOW.image(fr)
        gray_fr = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY) # Make sure the loaded video is grayscale.

        #excersise = st.empty()

        faces = facec.detectMultiScale(gray_fr, 1.3, 5)
        for (x, y, w, h) in faces: 
            fc = gray_fr[y:y+h, x:x+w]
            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis]) # Predict the new emotion.
            placeholder.container().warning(pred)
            if pred in {"Happy", "Neutral", "Surprise", "Disgust"}:
                time.sleep(1)
                

            else:
                excersise.container().markdown('<div class="custom-warning">Do the breathing exercise found above!</div>', unsafe_allow_html=True)
                vid = random.randint(1, 3)
                placeholder.write(video_style, unsafe_allow_html=True)
                if (vid == 1):
                    placeholder.video("https://www.youtube.com/watch?v=5DqTuWve9t8&ab_channel=Calm")

                    time.sleep(35)
                    placeholder.empty()
                
                if (vid == 2):
                    placeholder.video("https://www.youtube.com/watch?v=xbF4NBTukAI")

                    time.sleep(90)
                    placeholder.empty()
                
                if (vid == 3):
                    placeholder.video("https://www.youtube.com/watch?v=uxayUBd6T7M")
                    time.sleep(60)
                    placeholder.empty()
            
                
            
            times = times - 1
            
            timer.container().markdown(f'<div class="timer-container"><span class="timer-text">{times}</span></div>', unsafe_allow_html=True)

else:
    st.write('Stopped')
