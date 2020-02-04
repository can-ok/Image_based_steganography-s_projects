import cv2
import pandas as pd

img=cv2.imread('Airplane.png')


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


canny=cv2.Canny(gray_img,150,200)

cv2.imshow('img',canny)

cv2.imwrite('canny_img.png',canny)

cv2.waitKey(0)

print(canny[:1]) #As you see we represent edges with 255=1(white)

cnt=0
for i in canny[:1]:
    for x in i:
        cnt+=1

print(cnt)
