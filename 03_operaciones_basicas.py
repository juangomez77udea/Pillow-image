from PIL import Image

image = Image.open('pillow.png')
image = image.convert('RGB')
image.save('pillow_cambiada.jpg')
image.thumbnail((200, 200))
image.save('pillow_miniatura.jpg')
