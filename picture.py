import cv2
import numpy as np
if __name__ == '__main__':
    img = cv2.imread("me.jpg")
    # img1 = np.zeros_like(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j,0] == 6 and img[i,j,1] == 6 and img[i,j,2]:
                img[i,j,:] = [214,6,6]
    cv2.imshow("img",img)
    cv2.waitKey(0)