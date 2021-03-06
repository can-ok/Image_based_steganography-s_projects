import numpy as np
from math import log, e
import math
import pandas as pd
import cv2
from tkinter import *
from tkinter import filedialog
from skimage.measure import compare_ssim

from matplotlib import pyplot as plt

index=0 #gloabal
orginal_image=[]

encrypted_image=[]

filename=""

window=Tk()
window.title("Linear Steganogarfy")
canvas=Canvas(window,width=500,height=500)
canvas.pack()


def entropy(labels, base=2):#log2 base
    vc = pd.Series(labels).value_counts(normalize=True, sort=False)
    base = e if base is None else base
    return -(vc * np.log(vc)/np.log(base)).sum()


def slctimg():
    global filename
    filename=filedialog.askopenfilename(initialdir="/",title="Select A file",filetype=(("jpeg","*jpg"),("All Files","*.*")))
    lbl2=Label(window,text=filename,font=("arial",20)).place(x=100,y=50)
    print(filename)


    
def UIQI(img1,img2):
    x_mean=np.mean(img1)
    y_mean=np.mean(img2)
    
    x_var=np.var(img1,ddof=1)
    y_var=np.var(img2,ddof=1)
    

    #x_std=np.std(img1,ddof=1)
    x_std=x_var**(1/2)
    y_std=y_var**(1/2)

    

    l=img1-x_mean
    r=img2-y_mean
    n=img1.size
    cov= (l*r).sum()/(n-1)

  


    q1=(cov)/(x_std*y_std)

    q2=(2*x_mean*y_mean)/((x_mean**2)+(y_mean**2))
    
    q3=(2*x_std*y_std)/((x_var)+(y_var))

    Q=q1*q2*q3

    print("UIQI :"+str(Q))
    """
    Q2=(4*cov*x_mean*y_mean)/((x_var+y_var)*(x_mean**2+y_mean**2))

    print("UIQI :"+str(Q2))
    """

def cal():
    window.destroy() #destroy the window
    program()

def program():

    path = 'Fishing Boat.png'
    img=cv2.imread(path)
    img2=cv2.imread('encryptedimg.png')

    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    #conver to grayscale img
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    """
    plt.hist(img2.ravel(),256,[0,256])
    plt.show()
    """
    #for RGB
    #height,width,channels=img.shape

    height,width=img.shape

    #print("cv2 PSNR:"+str(cv2.PSNR(img,img2)))
    
    ##SSIM

    



    #print("SSIM: {}".format(ssim(img,img2)))


    cv2.imshow('image',img)
    print("height:{} width:{}, channels:1".format(height,width))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #Read Message for Message.txt 


    for i in range(0,width):#witdh
        for y in range(0,height):#height
            orginal_image.append(img[i][y])
            encrypted_image.append(img2[i][y])

    cv2.imshow('image',img) 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ###########################################

    #Performance evalutation Techniques
   
    
    
    
   


work=Button(window,text="Calculate",width=30,height=5,command=cal).place(x=250,y=400)

slctbutton=Button(window,text="Select Image",width=30,height=5,command=slctimg).place(x=100,y=100)



window.mainloop()



"""
arr1=np.asarray([125,255,132,90])
arr2=np.asarray([127,254,135,90])

mse,psnr_Db=psnr(arr1,arr2)
print("MSE:{} PSNR:{}".format(mse,psnr_Db))

"""


print("Entropy:"+str(entropy(orginal_image)))

arr1=np.asarray(orginal_image)
arr2=np.asarray(encrypted_image)


UIQI(arr1,arr2)