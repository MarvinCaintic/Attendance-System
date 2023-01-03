#!/usr/bin/env python
# coding: utf-8

# # Logs

# Author - Marvin Bedio Caintic
# 
# Study - Development of Face Clustering using KMeans clustering algorithm

# # Library installation

# In[4]:


# pip install tensorflow==1.2.0 --ignore-installed
# pip install nightly
# pip install numpy
# pip install mahotas
# pip install keras
# pip install sklearn
# pip install OpenCv
# pip install pandas
# pip install scikit-image
# pip install ipython
# pip install imutils
# pip install --upgrade tensorflow --user


# # Library calls

# In[5]:


import os
import cv2
import sys
import glob
import pickle
import shutil
import argparse
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QImage
import mahotas as mt
import numpy as np
import pandas as pd
import skimage.color
import skimage.io
import skimage.viewer
import tensorflow as tf
import scipy.stats as sp
from sklearn.model_selection import train_test_split
from scipy.stats import norm, kurtosis
from IPython.display import Image
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from imutils import build_montages

#pca
import sklearn.cluster as sklc
import sklearn.decomposition as skld
import sklearn.metrics as sklm

# for loading/processing the images  
from tensorflow.keras.preprocessing.image import load_img 
from tensorflow.keras.preprocessing.image import img_to_array 
from tensorflow.keras.applications.vgg16 import preprocess_input 

# models 
from tensorflow.keras.applications.vgg16 import VGG16 
from tensorflow.keras.models import Model

# clustering and dimension reduction
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.cluster import MiniBatchKMeans

# CNN
from tensorflow.keras.layers import Input, Lambda, Dense, Flatten,Conv2D
from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator,load_img
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import MaxPooling2D


# # Dataset preparation

# Change the root directory value to the complete path directory of required folder for face recognition folder.

# In[2]:


root_dir = "E:\\required folder for face recognition\\"


# Haarcascade classifier are referenced to their respective variables

# In[3]:


face_classifier = cv2.CascadeClassifier(root_dir + "imported\\haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(root_dir + "imported\\haarcascade_mcs_eyepair_big.xml")
nose_classifier = cv2.CascadeClassifier(root_dir + "imported\\haarcascade_nose.xml")
mouth_classifier = cv2.CascadeClassifier(root_dir + "imported\\haarcascade_mouth.xml")


# # Method Acquire Dataset

# Parameter:
# - **type, path** (video -> location of the input video OR images -> directory where the input images lies*).
# - **return** -> images
# In[5]:


def face_cropped(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if faces is None:
        return None
    facesWithColor = []
    for(x,y,w,h) in faces:
      facesWithColor.append(img[y:y+h, x:x+w])
    return facesWithColor


# Methods to verify the face recordings

# In[6]:


def eyes_cropped(face):
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    eyes_pair = eye_classifier.detectMultiScale(gray, 1.3, 5)

    if eyes_pair is None:
      return None
    for(x,y,w,h) in eyes_pair:
        return face[y:y+h, x:x+w]
def nose_cropped(face):
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    nose = nose_classifier.detectMultiScale(gray, 1.3, 5)

    if nose is None:
      return None
    for(x,y,w,h) in nose:
        return face[y:y+h, x:x+w]
def mouth_cropped(face):
    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
    mouth = mouth_classifier.detectMultiScale(gray, 1.3, 5)

    if mouth is None:
      return None
    for(x,y,w,h) in mouth:
        return face[y:y+h, x:x+w]
def verify(face):
    return eyes_cropped(face) is not None and nose_cropped(face) is not None and mouth_cropped(face) is not None


# Pre processing main method
# -**return** All verified face recordings gathered

# In[7]:


import pickle
import time
import os

def recognize(gray_image):
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition'))
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read(root_dir + "\\output\\classifier.xml")
    
    id, pred = clf.predict(gray_image)
    confidence = int(100*(1-pred/300))
    
    return id, confidence

    
# In[8]:


def getImages(path):
    images = []
    img_id = 0
    ext = ['png', 'jpg', 'gif']    # Add image formats here
    files = []
    [files.extend(glob.glob(path + '*.' + e)) for e in ext]
    for file in files:
        if cv2.imread(file) is not None:
            images.append(cv2.resize(cv2.imread(file), (224, 224), interpolation = cv2.INTER_AREA))
    return images




    
def train():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Database\\required folder for face recognition'))
    def train_classifier(data_dir):
        path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
        faces = []
        ids = []
        
        for image in path:
            img = cv2.imread(image)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split(".")[0])
            
            faces.append(imageNp)
            ids.append(id)
        ids = np.array(ids)
        
        #Train the classifier then save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, np.array(ids))
        clf.write(root_dir + "\\output\\classifier.xml")
    train_classifier(root_dir + "\\KNOWN_FACES")
    