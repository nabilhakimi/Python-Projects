from PIL import Image, ImageEnhance, ImageFilter
import os

source_directory = './Images_Sources'
edited_directory = '/Edited_Images'

for images in os.listdir(source_directory):
    image = Image.open(f"{source_directory}/{images}")

    edit = image.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(images)[0]
    edit.save(f'.{edited_directory}/{clean_name}_edited.jpg')
    edit.show()
