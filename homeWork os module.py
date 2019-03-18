# find all pdf, mp4, and txt files on your computer and write them to seperate txt files.

import os

pdfFiles = list()
mp4Files = list()
txtFiles = list()

pdfTXT = open("pdf Files.txt", "a", encoding = "utf-8")
mp4TXT = open("mp4 Files.txt", "a", encoding = "utf-8")
txtTXT = open("txt Files.txt", "a", encoding = "utf-8")

pdfTXT.write("######## ON C:/ ##########\n\n")
mp4TXT.write("######## ON C:/ ##########\n\n")
txtTXT.write("######## ON C:/ ##########\n\n")


for directory, folderName, fileName in os.walk("C:/"):
    for theFile in fileName:
        if theFile.endswith(".pdf"):
            pdfFiles.append(theFile)
            pdfTXT.write(theFile + "\n")
        elif theFile.endswith(".mp4"):
            mp4TXT.write(theFile + "\n")
            mp4Files.append(theFile)
        elif theFile.endswith(".txt"):
            txtTXT.write(theFile + "\n")
            txtFiles.append(theFile)


pdfTXT.write("\n\n######## ON D:/ ##########\n\n")
mp4TXT.write("\n\n######## ON D:/ ##########\n\n")
txtTXT.write("\n\n######## ON D:/ ##########\n\n")

for directory, folderName, fileName in os.walk("D:/"):
    for theFile in fileName:
        if theFile.endswith(".pdf"):
            pdfFiles.append(theFile)
            pdfTXT.write(theFile + "\n")
        elif theFile.endswith(".mp4"):
            mp4TXT.write(theFile + "\n")
            mp4Files.append(theFile)
        elif theFile.endswith(".txt"):
            txtTXT.write(theFile + "\n")
            txtFiles.append(theFile)

pdfTXT.close()
mp4TXT.close()
txtTXT.close()