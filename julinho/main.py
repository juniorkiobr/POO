import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("image.jpg")
color = ('b','g','r')
cv2.imshow('BANANAN',img)
for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
