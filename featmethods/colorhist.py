from skimage import feature
import numpy as np
import cv2

class colorHist:
    # bins is the number of bins in histogram for each image channel
    # color is the color mode: RGB or HSV
    def __init__(self, bins, color="RGB"):
        # store the number of points and radius
        self.bins = bins
        self.color= color


    # compute the Color Histogram
    def describe(self, image):

        hist = []

        # compute the color histogram for each level
        if (len(image.shape) > 2):
            #check if user chose HSV. Default image is RGB
            if (self.color == "HSV"):
                image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
            for i in range(image.shape[2]):
                hist.append(cv2.calcHist([image], [i], None, [bins], [0, 256]))
        else:
            hist.append(cv2.calcHist([image], [0], None, [self.bins], [0, 256]))

        hist = np.asarray(hist)

        # normalize the histogram
        cv2.normalize(hist, hist)
        # falt histogram
        hist.flatten()

        # return the histogram
        return hist

    def calculate(self,image):
        return self.describe(image)
