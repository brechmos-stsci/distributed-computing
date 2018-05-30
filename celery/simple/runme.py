import numpy as np
from summer import sum_matrix

# This is the main code to run

#
# Create some random images to send to the processing machine
#
images = [np.random.random((256, 256)) for x in range(10)]

smoothed_images = sum_matrix(images)

print(smoothed_images)
