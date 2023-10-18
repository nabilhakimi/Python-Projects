from PIL import Image, ImageEnhance, ImageFilter
import os

source_directory = './Images_Sources'
edited_directory = '/Edited_Images'
valid_image = []
valid_image_format = [".jpg", ".gif", ".png", ".tga"]

for images in os.listdir(source_directory):
    ext = os.path.splitext(images)[1]
    if ext.lower() not in valid_image_format:
        continue
    image = Image.open(f"{source_directory}/{images}")
    valid_image.append(image)

    edit = image.filter(ImageFilter.SHARPEN)
    clean_name = os.path.splitext(images)[0]
    edit.save(f'.{edited_directory}/{clean_name}_edited.jpg')
    edit.show()
