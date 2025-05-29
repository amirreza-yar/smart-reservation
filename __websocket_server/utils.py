import numpy as np
import cv2

def img_buf_to_array(img_data):
    np_arr = np.frombuffer(img_data, np.uint8)
                
    # Decode the numpy array to an image using OpenCV
    image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if image is not None:
        return image
    
    return None