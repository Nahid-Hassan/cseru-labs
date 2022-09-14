from PIL import Image

# To convert the image From JPG to PNG : {Syntax}
img = Image.open("Image.jpg")
img.save("Image.png")

# To convert the Image From PNG to JPG
img = Image.open("Image.png")
img.save("Image.jpg")
