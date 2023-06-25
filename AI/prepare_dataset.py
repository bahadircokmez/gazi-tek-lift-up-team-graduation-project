import os
import random
import sys
import cv2
import datetime 
import imutils
import glob

res = input("\r\nPlease enter model name: ")

dirLst = os.listdir("data")
if res in dirLst:
    print("\r\nError. Model directory already exists. Please choose some other name or delete the current directory\r\n")
    sys.exit() 

print("Making directory structure")
os.makedirs("data/{}/Annotations".format(res))
os.makedirs("data/{}/ImageSets/Main".format(res))
os.makedirs("data/{}/JPEGImages".format(res)) 

def rrmdir(path):
    for entry in os.scandir(path):
        if entry.is_dir():
            rrmdir(entry)
        else:
            os.remove(entry)
    os.rmdir(path)

'''
fileLst = os.listdir('videos')
fileLst.remove('readme.txt')
if len(fileLst) == 0:
    print("No test video found in videos dir.")
    rrmdir("data/{}".format(res))
    sys.exit(0)
elif len(fileLst) > 1:
    print("Multiple videos found in videos dir. Please enter the name of the video to use\r")
    print(fileLst)
    vname = input("Please enter the full name of the video to use for dataset with extension(.mp4): ")
elif len(fileLst) == 1:
    vname = fileLst[0]
    '''

#cap = cv2.VideoCapture('videos/{}'.format(vname))

# Adjust saveImg value as per your choice
# High value will have less images saved
# Low value will have large images saved 
#saveImg = 10



x="/*"
s = f"/home/bitirme/jetson-train/images{x}.jpg"
counter = 0

result = glob.glob(s)
counter = len(result)
allFiles = []
for i in result:
    image = i.split('images/')[1]
    print(image)
    allFiles.append(image)


testNum = int(counter * 0.10)
testFileLst = []
while True:
    ap = random.choice(allFiles)
    if ap not in testFileLst:
        testFileLst.append(ap)
        if len(testFileLst) == testNum:
            break

trainFileLst = list(set(testFileLst).symmetric_difference(set(allFiles)))

f = open("data/{}/ImageSets/Main/test.txt".format(res), 'w+')
for test in testFileLst:
    test = test.split(".jpg")
    f.write(test[0] + "\n")
f.close()
f = open("data/{}/ImageSets/Main/val.txt".format(res), 'w+')
for test in testFileLst:
    test = test.split(".jpg")
    f.write(test[0] + "\n")
f.close()

f = open("data/{}/ImageSets/Main/train.txt".format(res), 'w+')
for train in trainFileLst:
    train = train.split(".jpg")
    f.write(train[0] + "\n")
f.close()
f = open("data/{}/ImageSets/Main/trainval.txt".format(res), 'w+')
for train in trainFileLst:
    train = train.split(".jpg")
    f.write(train[0] + "\n")
f.close()







