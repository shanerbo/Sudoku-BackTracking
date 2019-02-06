import pandas as pd
import numpy as np
import os
import scipy.ndimage
from skimage.feature import hog
from skimage import data, color, exposure
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib
df = pd.read_csv(r"D:\Erbo's Script\MNIST\mnist\train-labels.csv", names=['file', 'value'])
rawImages = []
features = []
labels = []
training_directory = "D:/Erbo's Script/MNIST/mnist/test-images/"
def image_to_feature_vector(image, size=(48, 48)):
    # resize the image to a fixed size, then flatten the image into
    # a list of raw pixel intensities
    return cv2.resize(image, size).flatten()
for filename in os.listdir(training_directory):
    if (filename.endswith('.jpg')):
        label = df.loc[df['file'] == 'train-images/0.jpg']['value'].values[0]
        image = cv2.imread(training_directory+filename)
        pixels = image_to_feature_vector(image)
        rawImages.append(pixels)
        #features.append(hist)
        labels.append(label)

rawImages = np.array(rawImages)
# features = np.array(features)
labels = np.array(labels)
(trainRI, testRI, trainRL, testRL) = train_test_split(rawImages, labels)
model = KNeighborsClassifier(n_neighbors=15)
model.fit(trainRI, trainRL)
acc = model.score(testRI, testRL)