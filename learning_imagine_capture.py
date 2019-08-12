import numpy as np
import cv2
from PIL import ImageGrab


print("this is a Github commit test...")

img = ImageGrab.grab()    #grabs a screenshot
#img_np = np.array(img)   //transforms the image into a format that cv can accept (an array of pixels)
print(img.show())        #img.show() to open the img to the user

#image_np = np.array(img)

