import cv2
import numpy as np


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


#lsb bitleri ascii koduna dönüştürülüyor
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






img=cv2.imread('encryptedimg.png')

#conver to grayscale img
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#for RGB
#height,width,channels=img.shape

height,width=img.shape


cv2.imshow('image',img)
print("height:{} width:{}, channels:1".format(height,width))
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(0,width):#witdh #10
    for y in range(0,height):#height #216
        data=bin(img[i][y])
        """
        print(img[i][y])
        print(data)
        """
        encrypted_data=read_binary(data)
        msg.append(encrypted_data)



print(msg)
convert_to_Ascii(msg)

