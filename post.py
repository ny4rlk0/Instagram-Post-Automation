#coding: utf-8
#https://github.com/ny4rlk0/Instagram-Post-Automation/
#Uploads all images on the same directory or sub directories to instagram. Only jpg files. 1 Post pepr jpg file.
import os,sys,time,json
from random import randint
os.system("pip install opencv-python")
import cv2,pprint
os.system("pip install myigbot")
from myigbot import MyIGBot
usr="Enter_Username"
pw="Enter_Password"
Caption=""" nyarlko.com

Tags
--------------------------------
#movie #joke #anime
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
                time.sleep(randint(4,11))
                response = bot.upload_post(new_name, caption=Caption)
                if str(response)=="200":
                    print(name+" uploaded successfully!")
                else:
                    print("HTTPS CODE: "+str(response))
                try:
                    os.remove(new_name)
                    os.remove(name)
                except:pass
