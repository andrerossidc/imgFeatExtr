import matplotlib.pyplot as plt
from skimage.feature import hog
from skimage import data, exposure

class HOG:
    #VERIFICAR 1) block_norm=NONE ??  multichannel
	def __init__(self, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(3, 3), block_norm="L2-Hys", transform_sqrt=False, feature_vector=True, visualise=False):
		self.orientations = orientations
		self.pixels_per_cell = pixels_per_cell
		self.cells_per_block = cells_per_block
		self.transform_sqrt = transform_sqrt
		self.block_norm = block_norm
		self.visualise = visualise
		self.feature_vector = True
		#self.multichannel = multichannel

	def describe(self, image):
	    # This script generates a vector H of size : 9*9*9=729, where
	    # The first 9 is the number of orientations
	    # The second 9 is the number of cells per block : cells_per_block=(3, 3) (multiply 3*3)
	    # The last 9 is because this image have 94 x 27 pixels: 94/8=11 (88 pixels) and 27/8=3 (24 pixels).
	    # Thus, 9 blocks on height and 1 block on width in width block on width and

		H = hog(image, orientations=self.orientations, pixels_per_cell=self.pixels_per_cell,
			cells_per_block=self.cells_per_block, transform_sqrt=self.transform_sqrt, block_norm=self.block_norm,
			visualize=self.visualise) #, multichannel=self.multichannel)
		#print(H)
			#H = hog(image)

		return H

	def calculate(self,image):
		return self.describe(image)

#image = data.astronaut()
#image = image[:,:,0]
