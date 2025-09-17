import cv2
import os
import numpy as np
import pickle

dataset_dir = "dataset"
trainer_dir = "trainer"
os.makedirs(trainer_dir, exist_ok=True)

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    faces = []
    labels = []
    label_ids = {}
    current_id = 0

    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):

                path = os.path.join(root, file)
                label = os.path.basename(root)

                if label not in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
                faces.append(img)
                labels.append(id_)

    recognizer.train(faces, np.array(labels))
    recognizer.save(os.path.join(trainer_dir, "lbph_model.yml"))

    with open(os.path.join(trainer_dir, "labels.pkl"), "wb") as f:
        pickle.dump(label_ids, f)

    print("Training completed.")

if __name__ == "__main__":
    train()
