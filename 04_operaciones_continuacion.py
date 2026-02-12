from PIL import Image
from PIL import ImageFilter

image = Image.open('pillow.png')
image.transpose(Image.FLIP_LEFT_RIGHT).save('pillow_flip.png')
image.rotate(120).save('pillow_rotada.png')
image.crop((200, 50, 450, 300)).save('pillow_recortada.png')
image_grey = image.convert('L')
image_grey.save('pillow_grises.png')

image_filtrada = image.filter(ImageFilter.BLUR)
image_filtrada.save('pillow_filtrada.png')