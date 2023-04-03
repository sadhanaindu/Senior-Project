import streamlit as st
import time
import numpy as np
import cv2

import os
cwd = os.getcwd() # This fn will return the Current Working Directory

#get files names in test and text
paths = cwd + "/test/angry"
test_angry = os.listdir(paths)
len_angry = len(test_angry)
count_angry = 0

paths = cwd + "/test/disgust"
test_disgust = os.listdir(paths)

paths = cwd + "/test/disgust"
test_disgust = os.listdir(paths)


st.set_page_config(page_title="interactive")
st.sidebar.header("Take a picture")

st.markdown("# Take a neutral picture")
picture = st.camera_input("Neutral Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    path = "/test/"
    cv2.imwrite(moment + '.jpg', roi)

#Put global variables outside so that it isn't affected by the refresh of the page. 
#insert while loop inside if to take 5 pictures. (try, may not be solution)
#try to tag images that are taken by us. Tag it based on file name (this will remove need for previous solution, try this first). 
st.markdown("# Take an angry picture")
picture = st.camera_input("Angry Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    path = "/test/"
    sti = str(count_angry) 
    cv2.imwrite(sti + '.jpg', roi)
    count_angry = count_angry + 1
    # moment = test_angry[count_angry]
    # cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    # cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    # roi = cv2.resize(cv2_img, (48, 48))
    # moment = "/test/angry/" + moment
    # moment_path = cwd + moment
    # st.markdown(moment)
    # os.remove(moment_path)
    # cv2.imwrite(moment, roi)
    # count_angry = count_angry + 1

st.markdown("# Take a sad picture")
picture = st.camera_input("Sad Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    cv2.imwrite(moment + '.jpg', roi)

st.markdown("# Take a surprised picture")
picture = st.camera_input("Surprised Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    cv2.imwrite(moment + '.jpg', roi)

st.markdown("# Take a fearful picture")
picture = st.camera_input("Scared Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    cv2.imwrite(moment + '.jpg', roi)

st.markdown("# Take a happy picture")
picture = st.camera_input("Happy Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    cv2.imwrite(moment + '.jpg', roi)

st.markdown("# Take a disgusted picture")
picture = st.camera_input("Disgusted Expression!")
if picture:
    moment=time.strftime("%Y-%b-%d__%H_%M_%S",time.localtime())
    cv2_img = cv2.imdecode(np.frombuffer(picture.getbuffer(), np.uint8), cv2.IMREAD_COLOR)
    cv2_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
    roi = cv2.resize(cv2_img, (48, 48))
    cv2.imwrite(moment + '.jpg', roi)

