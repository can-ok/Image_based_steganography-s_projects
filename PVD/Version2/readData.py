import cv2
import numpy as np
from random import randint
from random import seed
import random


index=0 #gloabal
msg=[]
meaningful_message=[]
fullmsg=[]

def ascii_to_Message(ascii_msg):
    for word in ascii_msg:
        num_ascii=int(word,2)#convert to ascii code
        letter=chr(num_ascii)#then convert ascii to Char
        meaningful_message.append(letter)
        fullmsg.append(meaningful_message)
    print(meaningful_message)


def convert_to_Ascii(msg):
    ascii_msg=[]
    word=""
    c=1
    for bit in msg:
        if(c%8==0):
            ascii_msg.append(word)
            word=""
            c=1
        
        word=word+bit
        c=c+1   
            
        

    #print(ascii_msg)
    ascii_to_Message(ascii_msg)



def read_binary(img_data):
    global index

    piksel_frame=list(img_data)
    #change string to list thats the only way you can change least sigficant bit
    size=len(img_data)
    #print("lsb "+piksel_frame[size-1])
    encrypted_data=piksel_frame[size-1]
    index=index+1
    return encrypted_data






img=cv2.imread('encryptedimg.png',0) #stego

#-----------Trick------------
#gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
x=cv2.imread('Airplane.png')
gray_img=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
##

height,width=gray_img.shape

cv2.imshow('image',gray_img)
print("height:{} width:{}, channels:1".format(height,width))

cv2.waitKey(0)
cv2.destroyAllWindows()

canny=cv2.Canny(gray_img,100,200)#find edges with canny edge


canny_pixels=[]
cnt=0
for i in canny:
    for y in i:
        if(y==255): #if it is white add that pixels to list for 
            canny_pixels.append(cnt)
        cnt+=1
random.Random(4).shuffle(canny_pixels)


rnd=len(canny_pixels)

for i in range(0,rnd):
    popped_pixel=canny_pixels.pop()
    

    i=int(popped_pixel/width)
    #print("row:"+str(i))
    y=popped_pixel%width

    data=bin(img[i][y])
    #print(img[i][y])
    #print(data)
    encrypted_data=read_binary(data)
    msg.append(encrypted_data)
       



convert_to_Ascii(msg)
