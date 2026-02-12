from PIL import Image

image = Image.open('pillow.png')
print(image.format)
print(image.size)
print(image.mode)
