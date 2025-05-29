from __face_detector.api import FaceDetectionModel
from __face_detector.utils import load_images_from_dir

face_model = FaceDetectionModel('face_db.p')
yar_imgs = load_images_from_dir('.data/for_enroll/yar/')
face_model.enroll_new_face(yar_imgs, "yar")

# yar_imgs = load_images_from_dir('.data/for_enroll/amin/')
# face_model.enroll_new_face(yar_imgs, "amin")