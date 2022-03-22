#coding: utf-8
import os,sys,time,json
from random import randint
os.system("pip install opencv-python")
import cv2,pprint
os.system("pip install myigbot")
from myigbot import MyIGBot
usr="ENTER_USERNAME"
pw="ENTER_PASSWORD"
Caption=""" Some caption text

Tags
--------------------------------
#anime #manga
IPA
"""
size = (1024, 1024) #Photo Size
file_list=[] # JPG File list
bot = MyIGBot(usr,pw)
#After Login
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        if file.endswith(".JPG") or file.endswith(".jpg"):
            file_list.append(os.path.join(file))
for name in file_list:
                img=cv2.imread(name)
                img2=cv2.resize(img,size)
                cv2.imshow("img2",img2)
                new_name="resized"+name
                cv2.imwrite (new_name,img2)
                time.sleep(randint(4,10))
                response = bot.upload_post(new_name, caption=Caption)
                print(response+" <----- 200 ise = BAŞARILI YÜKLEME")
                #os.remove(new_name+".REMOVE_ME")
