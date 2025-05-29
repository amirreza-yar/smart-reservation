import face_recognition
from sklearn import svm
import pickle
from collections import Counter
import os

class FaceDetectionModel:
    def __init__(self, db_file_name:str, db_recreate=False):
        self.db_file_name = db_file_name
        self.db_recreate = db_recreate
        self.enrolled_faces = None
        self.classifier_model = None

        self._load_db_file()

    def _load_db_file(self):
        try:
            if self.db_recreate:
                print("Recreating the db file...")
                if os.path.exists(self.db_file_name):
                    os.remove(self.db_file_name)

                enrolled_faces = {}
                pickle.dump(enrolled_faces, open("face_db.p", "wb"))

            enrolled_faces = pickle.load(open("face_db.p", "rb"))
            print("'face_db.p' file loaded")
        except:
            print("Unable to load faces from 'face_db.p', creating new 'face_db.p'...")
            enrolled_faces = {}
            pickle.dump(enrolled_faces, open("face_db.p", "wb"))
            print("New 'face_db.p' created")

            enrolled_faces = pickle.load(open("face_db.p", "rb"))

            self.enrolled_faces = enrolled_faces

        if enrolled_faces:
            self.train_svm()

        else:
            print("No enrolled face. Waiting for enroll...")

    def _update_db_file(self):
        try:
            print("Updating 'face_db.p'...")
            pickle.dump(self.enrolled_faces, open("face_db.p", "wb"))
            print("'face_db.p' updated successfully")
        except:
            print("Errors accured while updating 'face_db.p', try again")

    def enroll_new_face(self, person_images, person_name):
        print(f"Creating encodings for {person_name}")
        person_encodings = []
        unused_images = 0

        for person_img in person_images:
            # face = face_recognition.load_image_file("data/for_enroll/" + person + "/" + person_img)
            face_bounding_boxes = face_recognition.face_locations(person_img)

            #If training image contains exactly one face
            if len(face_bounding_boxes) == 1:
                face_enc = face_recognition.face_encodings(person_img)[0]
                person_encodings.append(face_enc)
            else:
                unused_images += 1

        if unused_images:
            print(f"Encodings created, wan't able to use {unused_images} images")

        self.enrolled_faces[person_name] = person_encodings
        self._update_db_file()

        self.train_svm()

    def train_svm(self):
        if self.classifier_model:
            print("Retraining SVM classifier...")
        else:
            print("Training SVM classifier...")
        encodings = []
        names = []

        if not self.enrolled_faces:
            print("No enrolled faces!")
            return

        for name, enc_list in self.enrolled_faces.items():
            for enc in enc_list:
                encodings.append(enc)
                names.append(name)  

        clf = svm.SVC(gamma='scale')
        clf.fit(encodings,names)

        self.classifier_model = clf

        print("SVM classifier trained successfully")

    def detect_faces(self, img_list):
        print("Starting face detection...")

        if not self.classifier_model:
            print("No classifier!")
            return

        labels_list = []

        for img in img_list:
            # Find all the faces in the test image using the default HOG-based model
            face_locations = face_recognition.face_locations(img)
            no = len(face_locations)

            if no != 1:
                continue

            img_enc = face_recognition.face_encodings(img)[0]
            label = self.classifier_model.predict([img_enc])

            labels_list.append(*label)

        if len(labels_list) == 0:
            print("Face detection failed! Try again")
            return

        label_counts = Counter(labels_list)
        most_common_label, count = label_counts.most_common(1)[0]

        confidence = count / len(labels_list)
        print(f"Face detection finished! Most common label: {most_common_label}, confidence: {confidence:.2f}")

        return most_common_label, confidence