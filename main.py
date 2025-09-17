import cv2
import pickle
import pandas as pd
import os
from utils import mark_attendance

CONFIDENCE_THRESHOLD = 70

trainer_dir = "trainer"
employees_file = "employees.csv"

def run_attendance():
    if not os.path.exists(employees_file):
        print("employees.csv not found.")
        return

    df = pd.read_csv(employees_file)
    if df.empty:
        print("employees.csv is empty. Please add employees first.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(os.path.join(trainer_dir, "lbph_model.yml"))

    with open(os.path.join(trainer_dir, "labels.pkl"), "rb") as f:
        label_ids = pickle.load(f)
    id_labels = {v: k for k, v in label_ids.items()}

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)

            if conf < CONFIDENCE_THRESHOLD:
                name = id_labels[id_]
                emp = df[df['Name'] == name].iloc[0]
                jobid, role, dept = emp['JobID'], emp['Role'], emp['Department']

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
                text = f"{name} | {jobid} | {role} | {dept}"
                cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
                mark_attendance(name, jobid, role, dept)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
                cv2.putText(frame, "Unknown", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_attendance()
