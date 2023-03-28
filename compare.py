import cv2
import numpy as np

# Load images
img1 = cv2.imread("./output/frame_0000.jpg")
img2 = cv2.imread("./output/frame_0000_copy.jpg")

# Convert images to grayscale
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Convert images to numpy arrays
array1 = np.array(gray1)
array2 = np.array(gray2)

# Compute mean squared error (MSE)
mse = np.mean((array1 - array2) ** 2)

# Compute structural similarity index (SSIM)
# ssim = cv2.compareStructures(gray1, gray2, cv2.HISTCMP_CORREL)

# Print results
print(f"MSE: {mse}")
# print(f"SSIM: {ssim}")
