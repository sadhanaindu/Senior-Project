"""
# Testing the UI capabilities of streamlit:
"""
import cv2
import streamlit as st
from PIL import Image
import numpy as np
import time
from streamlit.components.v1 import html

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import model
from model import FacialExpressionModel

st.set_page_config(page_title="Take_A_Test")
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
    st.video("https://www.youtube.com/watch?v=5DqTuWve9t8&ab_channel=Calm")
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
                excersise.container().warning("Keep taking the exam!")
                
            else:
                excersise.container().warning("Do the breathing excersise found below!")
                time.sleep(35)
                
            
            times = times - 1
            
            timer.container().warning(times)

else:
    st.write('Stopped')