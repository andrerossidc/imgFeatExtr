#import mahotas as mt
import numpy as np
from skimage import feature

##  Gray Level Co-occurrence Matrix
class GLCM:
        def __init__(self, distances=1, angles=[0, np.pi/4, np.pi/2, 3*np.pi/4]):
            self.distances = distances
            self.angles = angles

        def describe(self, image):
            #Calculate the grey-level co-occurrence matrix.
            #result = greycomatrix(image, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4])
            #glcmFeat = []
            #print(type(image))
            #print(image.shape)
            glcm = feature.greycomatrix(image, self.distances, self.angles, normed=True, symmetric=True)
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
            return self.describe(image)
