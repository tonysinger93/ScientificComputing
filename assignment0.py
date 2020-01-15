import cv2
import numpy as np
import math

def makeBorder(inputImage, scale):

    image = cv2.imread(inputImage)
    newImage = np.zeros((math.ceil(image.shape[0]*scale),math.ceil(image.shape[1]*scale), image.shape[2]))
    vBorder = (newImage.shape[0] - image.shape[0]) // 2
    hBorder = (newImage.shape[1] - image.shape[1]) // 2

    for i in range(newImage.shape[0]-1):
        for j in range(newImage.shape[1]-1):
            if vBorder <= i <= (newImage.shape[0] - vBorder-1) and hBorder <= j <= (newImage.shape[1] - hBorder-1):
                newImage[i][j] = image[i-vBorder][j-hBorder]

    cv2.imwrite('bigBusiness.jpg', newImage)

    #imshow only displays RGB values btwn zero and one
    #divide image by 255.0 to make RGB value btwn 0 and 1
    cv2.imshow('bigBusiness.jpg', newImage/255.0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

makeBorder('business.jpg',1.1)
