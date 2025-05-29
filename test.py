"""
Test module for the face detection system.

This module provides functionality to test the face detection and enrollment features
of the system. It demonstrates how to load images from a directory and enroll them
into the face detection model.

Author: [Your Name]
Date: [Current Date]
"""

from __face_detector.api import FaceDetectionModel
from __face_detector.utils import load_images_from_dir

# Initialize the face detection model with the pre-trained database
face_model = FaceDetectionModel('face_db.p')

# Load and enroll images for the user "yar"
yar_imgs = load_images_from_dir('.data/for_enroll/yar/')
face_model.enroll_new_face(yar_imgs, "yar")

# Example of enrolling another user (commented out)
# yar_imgs = load_images_from_dir('.data/for_enroll/amin/')
# face_model.enroll_new_face(yar_imgs, "amin")