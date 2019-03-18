# os module

import os
from datetime import datetime

# # list of the directory

# for f in os.listdir():
#     print(f)

# # getting current directory

# print("Current dir:", os.getcwd())

# # changing directory

# os.chdir(r"C:\Users\Nihl\Desktop")
# print("Current dir:", os.getcwd())


# #Creating a folder
# os.chdir(r"C:\Users\Nihl\Desktop\Nihil\KeepGoing")
# os.mkdir("Silicon Valley")

# # Creating nested folders

# os.makedirs(r"MotherFolder/BabyFolder")
# os.mkdir("MotherFolder/SisterFolder")

# # Deleting a folder
# os.rmdir(r"MotherFolder/BabyFolder") #Oh no.. Baby folder is dead.

# # Deleting nested folders

# os.removedirs("MotherFolder")

# # Rename a folder

# os.rename("MotherFolder", "FatherFolder")

# # Properties of a folder

# now = datetime.now()

# print(os.stat("FatherFolder"))
# print(datetime.fromtimestamp(os.stat("FatherFolder").st_mtime))

# # W A L K ! (os.walk)

import time

startTime = time.time()
files = 0
for dirWay, folderNames, fileNames in os.walk(r"C:/"):
    for f in fileNames:
        if f.endswith(".txt"):
                print(f)
                files += 1
    
finishTime = time.time()
print("\n\n# # # # Scan is completed # # # #\n")
print("Total result {} files on C:/".format(files))
print("Process time:", finishTime - startTime, "seconds..")