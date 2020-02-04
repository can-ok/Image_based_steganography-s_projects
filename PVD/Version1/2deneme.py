import cv2
import pandas as pd
import numpy 


img=cv2.imread('Airplane.png')


gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


canny=cv2.Canny(gray_img,150,200)

cv2.imshow('img',canny)

cv2.imwrite('canny_img.png',canny)

cv2.waitKey(0)

print(canny[:1]) #As you see we represent edges with 255=1(white)

canny_pixels=[]
cnt=0
for i in canny:
    for y in i:
        if(y==255):
            canny_pixels.append(cnt)
        cnt+=1


print(canny_pixels)

            
height,width=gray_img.shape

i=int(199/height)
y=int(199%width)
print("{} {}".format(i,y))
canny[i][y]=1

print(canny[:1])