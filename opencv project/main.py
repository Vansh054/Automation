import cv2
import numpy as np

image1 = cv2.imread("1.jpg")
image2 = cv2.imread("2.jpg")

outcome = cv2.addWeighted(image1,0.7,image2,0.3,0)
cv2.imshow('OUTPUT',outcome)
cv2.destroyAllWindows() 

