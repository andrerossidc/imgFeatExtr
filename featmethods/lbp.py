from skimage import feature
import numpy as np


class LBP:
    def __init__(self, P=24, R=8, method="uniform"):
        # store the number of points and radius
        self.P = P
        self.R = R
        self.method = method

    def describe(self, image, eps=1e-7):
        # compute the Local Binary Pattern representation
        # of the image, and then use the LBP representation
        # to build the histogram of patterns
        lbp = feature.local_binary_pattern(image, self.P, self.R, method=self.method)

        #n_bins = int(lbp.max() + 1)
        #hist, _ = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))
        (hist, _) = np.histogram(lbp.ravel(),  bins=np.arange(0, self.P + 3), range=(0, self.P + 2))
        #(hist, _) = np.histogram(lbp, normed=True, bins=n_bins, range=(0, n_bins))

        # normalize the histogram
        hist = hist.astype("float")
        hist /= (hist.sum() + eps)

        # return the histogram of Local Binary Patterns
        return hist

    def calculate(self,image):
        return self.describe(image)
