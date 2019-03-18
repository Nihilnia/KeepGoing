from PIL import Image, ImageFilter

myImage = Image.open("nihil.jpg")

myImage.show()

#How to save as another image file?

myImage.save("nihil2.jpg")

for f in range(3, 6):
    myImage.save("nihil" + str(f) + ".jpg")

#Rotate!

myImage.rotate(188).save("nihil11.jpg")


#Convert to black and white!
myImage.convert(mode = "L").save("blackAndWhite.png")


#Change the sizes!

myImage.thumbnail((200, 200))
myImage.convert(mode = "L").save("200x200.jpg")

#Blur!

myImage.filter(ImageFilter.GaussianBlur(10)).save("nihil50.jpg")

myImage2 = Image.open("nihil.jpg")
myImage2.filter(ImageFilter.GaussianBlur(5)).save("blury.jpg")

#Cut the area!

ATATURKimage = Image.open("ataturk.jpg")
cutting = (42, 14, 2839, 3758)
ATATURKimage.crop(cutting).save("ataturk2.jpg")