import cv2
import numpy as np

from tkinter import *
from tkinter import filedialog

index=0 #gloabal
message=[]

filename=""

window=Tk()
window.title("Linear Steganogarfy")
canvas=Canvas(window,width=500,height=500)
canvas.pack()

def readMessage():
    msg=str(textbox.get())
    print("Message: "+msg)
   
    for letter in msg:
        ascii_code=ord(letter)#convert letter to ASCİ (a=97)
        bin_ascii=bin(ascii_code)#convert Ascii(ınteger) to binary 97=0b1100001
        bin_ascii=bin_ascii[2:] #Splitting 0b1100001 to 1100001 # len:7
        print("Ascii code:"+bin_ascii) 
            
        for i in bin_ascii:#binary formda olan ascii üzerinde dön
            message.append(i) #ilgili biti message'a ekle
    
    
    window.destroy() #destroy the window
    
    #call main program 
    program()


def binary_change(img_data):
    #change string to list thats the only way you can change least sigficant bit

    global index
    #sum=bin(int(img_data,2) + int(message[index],2))
    
    piksel_frame=list(img_data) #piksel değerini liste(array) dönüştür
    size=len(img_data) #uzunluk bilgisini al
    """
    print("binary form of pixel: {} lsb:{} ".format(data,piksel_frame[size-1]))
    """
    piksel_frame[size-1]=message[index]#Lsb ile message ilgili bitini değiştir
    index=index+1 #next message bit için indexi arttır 

    img_data="".join(piksel_frame)#değiştirlen piksel frame'ini string çevir
    return img_data #pikseli döndür

def slctimg():
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg","*jpg"),("All Files","*.*")))
    lbl2=Label(window,text=filename,font=("arial",20)).place(x=100,y=50)
    print(filename)


#1kb mesaj


def program():

    path = r''+str(filename)    
    
    img=cv2.imread(path)

    #conver to grayscale img
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #for RGB
    #height,width,channels=img.shape

    height,width=img.shape


    cv2.imshow('image',img)
    print("height:{} width:{}, channels:1".format(height,width))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Read Message for Message.txt 
    print("Message:"+str(message))

    c=0
    for i in range(0,width):#witdh
        for y in range(0,height):#height

            if(c<len(message)):#Mesajın boyutunu geçtikten sonra encryption durmalı 
                data=bin(img[i][y])#index'deki pixeli binary olarak al
                """
                print("İlgili Piksel : {}".format(img[i][y])) #ilgili piksel değerini yaz
                """
                encrypted_pixel=binary_change(data)#Bilgi piksele gömülmüş piksel frame'i
                """
                print("Son hali : {}".format(encrypted_pixel))
                """
                img[i][y]=int(encrypted_pixel,2)#piksel bitlerini int formatını çevir
                                                # ve ilgili resim indexine piksel bilgisini tekrar yaz
                c=c+1 #next message bit
                
    cv2.imshow('image',img) 
    cv2.waitKey(0)
    cv2.imwrite('encryptedimg.png',img)
    cv2.destroyAllWindows()





lbl1=Label(window,text="Enter your message",font=("arial",20)).place(x=120,y=200)
textbox=StringVar()
entry_box=Entry(window,textvariable=textbox,width=50).place(x=120,y=300)

work=Button(window,text="Work",width=30,height=5,command=readMessage).place(x=250,y=400)

slctbutton=Button(window,text="Select Image",width=30,height=5,command=slctimg).place(x=100,y=100)



window.mainloop()


