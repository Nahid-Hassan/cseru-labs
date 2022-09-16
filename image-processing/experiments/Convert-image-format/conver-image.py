from PIL import Image

img = Image.open("lenna.jpeg")
img.save("lenna.png")

img = Image.open("dog.png")
rgb_img = img.convert('RGB') 
rgb_img.save("dog.jpeg")