import cv2
import numpy as np
from random import randint
from random import seed
import random


index=0 #gloabal
message=[]


def readMessage():

    with open('message.txt','r') as file:
        for msg in file:
            print("Mesaj: {} len:{}".format(msg,len(msg)))
            for letter in msg:
                ascii_code=ord(letter)#convert letter to ASCİ a=97
                bin_ascii=bin(ascii_code)#convert Ascii(ınteger) to binary 97=0b1100001
                bin_ascii=bin_ascii[2:] #Splitting 0b1100001 to 1100001 # len:7
                print("Ascii code:"+bin_ascii) 
                
                for i in bin_ascii:
                    message.append(i)


    #close the file
    file.close()

def binary_change(img_data):
    
    global index
    #sum=bin(int(img_data,2) + int(message[index],2))
    
    piksel_frame=list(img_data)
    #change string to list thats the only way you can change least sigficant bit
    size=len(img_data)
    print("binary from of pixel: {} lsb:{} ".format(data,piksel_frame[size-1]))
    piksel_frame[size-1]=message[index] #LSB ile
    index=index+1
    piksel_frame[size-2]=message[index]  #LSB+2nd
    index=index+1
    img_data="".join(piksel_frame)
    return img_data

img=cv2.imread('Airplane.png')

#conver to grayscale img
#for RGB

#height,width,channels=img.shape

msg="canokan"
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Read Message for Message.txt 
readMessage()
print("Message:"+str(message))

allpixels=[]


# work with gray_image instead of img(has 3 channel)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert grayscale

height,width=gray_img.shape

canny=cv2.Canny(gray_img,100,200)#find edges with canny edge

cv2.imshow('img',canny)

cv2.imwrite('canny_img.png',canny)

cv2.waitKey(0)


canny_pixels=[]
cnt=0
for i in canny:
    for y in i:
        if(y==255): #if it is white add that pixels to list for 
            canny_pixels.append(cnt)
        cnt+=1

x=int(len(message)/2)

for x in range(0,x):
    popped_pixel=canny_pixels.pop()
    print(popped_pixel)
    i=int(popped_pixel/width)
    #print("row:"+str(i))
    y=popped_pixel%width
    #print("column:"+str(y))
    data=bin(gray_img[i][y])
    encrypted_pixel=binary_change(data)

    gray_img[i][y]=int(encrypted_pixel,2)

    


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.imwrite('encryptedimg.png',gray_img)
cv2.destroyAllWindows()
