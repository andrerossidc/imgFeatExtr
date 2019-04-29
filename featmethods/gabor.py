#
# http://scikit-image.org/docs/dev/auto_examples/features_detection/plot_gabor.html

from skimage.filters import gabor_kernel
from skimage import io
from matplotlib import pyplot as plt

gk = gabor_kernel(frequency=0.2)
plt.figure()
io.imshow(gk.real)
io.show()

# more ripples (equivalent to increasing the size of the
# Gaussian spread)
gk = gabor_kernel(frequency=0.2, bandwidth=0.1)
plt.figure()
io.imshow(gk.real)
io.show()

gk = np.real(gk)
