import numpy as np
import PIL.Image
import os

def load_image(img_dir):
    try:
        im = PIL.Image.open(img_dir)
        im = im.convert("RGB")
        return np.array(im)
    except:
        print(f"Can't load {img_dir}")

def load_images_from_dir(img_dir):
    img_list = []
    img_list_dir = os.listdir(img_dir)

    for img in img_list_dir:
        try:
            im = PIL.Image.open(img_dir + img)
            im = im.convert("RGB")
            img_list.append(np.array(im))
        except:
            print(f"Can't load {img_dir + img}")
            continue
    
    if img_list:
        print(f"{len(img_list)} images loaded successfully")
        return img_list
    else:
        print("Images list is empty! Nothing to return")
