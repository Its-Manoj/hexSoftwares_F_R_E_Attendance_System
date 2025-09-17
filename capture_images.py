import cv2
import os
import pandas as pd

NUM_IMAGES_PER_PERSON = 10

dataset_dir = "dataset"
employees_file = "employees.csv"

def capture_images():
    if not os.path.exists(employees_file):
        print("employees.csv not found.")
        return

    name = input("Enter employee name (use underscores instead of spaces): ").strip()
    df = pd.read_csv(employees_file)

    if name not in df['Name'].values:
        print("Employee not found in employees.csv. Please add them first.")
        return

    person_dir = os.path.join(dataset_dir, name)
    os.makedirs(person_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing Images", frame)

        if count < NUM_IMAGES_PER_PERSON:
            img_path = os.path.join(person_dir, f"{name}_{count}.jpg")
            cv2.imwrite(img_path, gray)
            count += 1
            print(f"Captured {count}/{NUM_IMAGES_PER_PERSON}")

        if cv2.waitKey(1) & 0xFF == ord('q') or count >= NUM_IMAGES_PER_PERSON:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images()
