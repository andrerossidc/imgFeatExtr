#import mahotas as mt
import numpy as np
from skimage import feature

##  Gray Level Co-occurrence Matrix
class GLCM:
        def __init__(self, axis=[0, np.pi/4]):
            self.axis = axis

        def features(self, image, measure):
            #Calculate the grey-level co-occurrence matrix.
            #result = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
            glcm = feature.greycomatrix(image, [1], self.axis, normed=True, symmetric=True)
            glcmFeat = feature.greycoprops(glcm, measure)

            return glcmFeat

        def allFeatures(self, image):
            #Calculate the grey-level co-occurrence matrix.
            #result = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
            #glcmFeat = []
            #print(type(image))
            #print(image.shape)
            glcm = feature.greycomatrix(image, [1], [0, np.pi/4], normed=True, symmetric=True)
            #print(type(feature.greycoprops(glcm, 'contrast')))
            glcmFeat = feature.greycoprops(glcm, 'contrast').reshape(-1,)
            #print(type(glcmFeat))
            #print(glcmFeat)
            glcmFeat = np.concatenate((glcmFeat, feature.greycoprops(glcm, 'dissimilarity').reshape(-1,)))
            glcmFeat = np.concatenate((glcmFeat, feature.greycoprops(glcm, 'homogeneity').reshape(-1,)))
            glcmFeat = np.concatenate((glcmFeat, feature.greycoprops(glcm, 'ASM').reshape(-1,)))
            glcmFeat = np.concatenate((glcmFeat, feature.greycoprops(glcm, 'energy').reshape(-1,)))
            glcmFeat = np.concatenate((glcmFeat, feature.greycoprops(glcm, 'correlation').reshape(-1,)))

            return glcmFeat

        def calculate(self,image):
            return self.allFeatures(image)
