import streamlit as st
import time
import numpy as np
import cv2
import random
import importlib
import subprocess

import os
cwd = os.getcwd() # This fn will return the Current Working Directory

#get files names in test and text
# How many pictures in each directory. 
paths = os.path.join(cwd, "test/angry")
test_angry = os.listdir(paths)
len_angry = len(test_angry) # Number of files in angry directory. 

paths = os.path.join(cwd, "test/disgust")
test_disgust = os.listdir(paths)
len_disgust = len(test_disgust)

paths = os.path.join(cwd, "test/fear")
test_fear = os.listdir(paths)
len_fear = len(test_fear)

paths = os.path.join(cwd, "test/sad")
test_sad = os.listdir(paths)
len_sad = len(test_sad)
# Add the other directories if needed. 

def file_split():
    if random.random() < 0.8:
        return 1
    else:
        return 0

st.set_page_config(page_title="interactive")
st.sidebar.header("Take a picture")


st.markdown("# Take a neutral picture")
# form_neutral = st.form("NeutralForm", clear_on_submit=True)
# neutral_pictures = form_neutral.number_input("Enter the number of neutral images you want to take", min_value = 1, max_value=None, step=1)
# neutral_pictures = int(neutral_pictures)
# submit = form_neutral.form_submit_button("Send")
# pictures = []
count_neutral = 0
neutral_button_count = 0
toggle_state = st.checkbox('Take Neutral Photo {}'.format(count_neutral), key='button{}'.format(neutral_button_count))
while toggle_state:
    print("Neutral Loop executed")
    picture = st.camera_input("Neutral Expression!", key='camera{}'.format(neutral_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_neutral = file_split()
        if place_neutral == 1:
            filename = os.path.join('user_train/neutral', 'neutral_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/neutral', 'neutral_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Neutral Photo {}'.format(count_neutral), key='button{}'.format(neutral_button_count + 1))

#while st.button('Take Photo {}'.format(count_neutral), key='button{}'.format(neutral_button_count)):
#    print("Loop executed")
#    picture = st.camera_input("Neutral Expression!")
#    if picture is not None:
#        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
#        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
#        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
#        roi = cv2.resize(cv2_img, (48, 48))
#        path = "/test/"
#        cv2.imwrite(moment + '.jpg', roi) # path + moment
#    pictures.append(picture)
    count_neutral += 1
    neutral_button_count += 1
# Try making a separate directory first for storing the pics, so you know it's working. 
        
#Put global variables outside so that it isn't affected by the refresh of the page. 
#insert while loop inside if to take 5 pictures. (try, may not be solution)
#try to tag images that are taken by us. Tag it based on file name (this will remove need for previous solution, try this first). 

st.markdown("# Take an angry picture")
count_angry = 0
angry_button_count = 0
toggle_state = st.checkbox('Take Angry Photo {}'.format(count_angry), key='angry_button{}'.format(angry_button_count))
while toggle_state:
    print("Angry loop executed")
    picture = st.camera_input("Angry Expression!", key='angry_camera{}'.format(angry_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_angry = file_split()
        if place_angry == 1:
            filename = os.path.join('user_train/angry', 'angry_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/angry', 'angry_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Angry Photo {}'.format(count_angry), key='angry_button{}'.format(angry_button_count + 1))
    count_angry += 1
    angry_button_count += 1


st.markdown("# Take a sad picture")
count_sad = 0
sad_button_count = 0
toggle_state = st.checkbox('Take Sad Photo {}'.format(count_sad), key='sad_button{}'.format(sad_button_count))
while toggle_state:
    print("Sad loop executed")
    picture = st.camera_input("Sad Expression!", key='sad_camera{}'.format(sad_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_sad = file_split()
        if place_sad == 1:
            filename = os.path.join('user_train/sad', 'sad_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/sad', 'sad_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Sad Photo {}'.format(count_sad), key='sad_button{}'.format(sad_button_count + 1))
    count_sad += 1
    sad_button_count += 1

st.markdown("# Take a surprised picture")
count_surprised = 0
surprised_button_count = 0
toggle_state = st.checkbox('Take Surprised Photo {}'.format(count_surprised), key='surprised_button{}'.format(surprised_button_count))
while toggle_state:
    print("Surprised loop executed")
    picture = st.camera_input("Surprised Expression!", key='surprised_camera{}'.format(surprised_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_surprised = file_split()
        if place_surprised == 1:
            filename = os.path.join('user_train/surprise', 'surprised_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/surprise', 'surprised_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Surprised Photo {}'.format(count_surprised), key='surprised_button{}'.format(surprised_button_count + 1))
    count_surprised += 1
    surprised_button_count += 1

st.markdown("# Take a fearful picture")
count_fear = 0
fear_button_count = 0
toggle_state = st.checkbox('Take Fearful Photo {}'.format(count_fear), key='fear_button{}'.format(fear_button_count))
while toggle_state:
    print("Fear loop executed")
    picture = st.camera_input("Scared Expression!", key='fear_camera{}'.format(fear_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_fear = file_split()
        if place_fear == 1:
            filename = os.path.join('user_train/fear', 'fear_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/fear', 'fear_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Fearful Photo {}'.format(count_fear), key='fear_button{}'.format(fear_button_count + 1))
    count_fear += 1
    fear_button_count += 1        

st.markdown("# Take a happy picture")
count_happy = 0
happy_button_count = 0
toggle_state = st.checkbox('Take Happy Photo {}'.format(count_happy), key='happy_button{}'.format(happy_button_count))
while toggle_state:
    print("Happy loop executed")
    picture = st.camera_input("Happy Expression!", key='happy_camera{}'.format(happy_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_happy = file_split()
        if place_happy == 1:
            filename = os.path.join('user_train/happy', 'happy_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/happy', 'happy_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Happy Photo {}'.format(count_happy), key='happy_button{}'.format(happy_button_count + 1))
    count_happy += 1
    happy_button_count += 1

st.markdown("# Take a disgusted picture")
count_disgusted = 0
disgusted_button_count = 0
toggle_state = st.checkbox('Take Disgusted Photo {}'.format(count_disgusted), key='disgusted_button{}'.format(disgusted_button_count))
while toggle_state:
    print("Disgusted loop executed")
    picture = st.camera_input("Disgusted Expression!", key='disgusted_camera{}'.format(disgusted_button_count))
    if picture:
        moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
        cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
        cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
        roi = cv2.resize(cv2_img, (48, 48))
        place_disgusted = file_split()
        if place_disgusted == 1:
            filename = os.path.join('user_train/disgust', 'disgusted_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
        else:
            filename = os.path.join('user_test/disgust', 'disgusted_{}.jpg'.format(moment))
            cv2.imwrite(filename, roi)
    toggle_state = st.checkbox('Take Disgusted Photo {}'.format(count_disgusted), key='disgusted_button{}'.format(disgusted_button_count + 1))
    count_disgusted += 1
    disgusted_button_count += 1

def run_notebook():
    command = 'jupyter notebook Facial_Expression_Training.ipynb' 
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

if st.button("Retrain", key="retrain"):
    run_notebook()

