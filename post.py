#coding: utf-8
#https://github.com/ny4rlk0/Instagram-Post-Automation/
#Uploads all images on the same directory or sub directories to instagram. Only jpg files. 1 Post per jpg file.
current_upload_counter=0;new_counter=0
import os,sys,time,json;from random import randint
os.system("pip install opencv-python myigbot")
import cv2,pprint;from myigbot import MyIGBot

usr="USERNAME"
pw="PASSWORD"
photo_upload_counter=15 #How many photo you wanna upload?
Caption="""nyarlko.com!
Tags
--------------------------------
#anime #manga
You really should change this caption!
"""
size = (1024, 1024) #Photo Size
file_list=[] # JPG File list
bot = MyIGBot(usr,pw)# Login

def scanfiles():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith(".JPG") or file.endswith(".jpg"):
                file_list.append(os.path.join(file))
def resizephotos(name):
    img=cv2.imread(name)
    img2=cv2.resize(img,size)
    new_name="resized"+name
    cv2.imwrite(new_name,img2)
def uploadfiles(name):
    response="Error"
    global new_counter,current_upload_counter
    try:response = bot.upload_post(name, caption=Caption)
    except:print("HTTPS ERROR CODE: "+str(response))
    else:new_counter+= 1
    if str(response)=="200":
        print(name+" uploaded successfully! "+str(new_counter))
        current_upload_counter+=1
    else:
        print("HTTPS ERROR CODE: "+str(response))
def deletefiles(file1,file2):
    try:
        os.remove(file1)
        os.remove(file2)
    except:pass
def main():
    global new_counter,current_upload_counter,photo_upload_counter
    scanfiles()
    for name in file_list:
        resizephotos(name)
        uploadfiles("resized"+name)
        deletefiles(name,"resized"+name)
        if photo_upload_counter==current_upload_counter:
            break
        time.sleep(randint(5,11)) #Waits random seconds before post!    
main()
