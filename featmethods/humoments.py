from skimage import measure
import numpy as np

class huMoments:
    def __init__(self):
        pass

    # compute the Color Histogram
    def describe(self, image):

        #calculate daisy feature descriptors
        mc = measure.moments_central(image)
        mn = measure.moments_normalized(mc)
        mh = measure.moments_hu(mn)

        # return Hu moments
        return mh

    def calculate(self,image):
        return self.describe(image)
