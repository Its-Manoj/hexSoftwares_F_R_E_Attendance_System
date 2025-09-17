import os
import pandas as pd
from datetime import datetime

def mark_attendance(name, jobid, role, dept, attendance_dir="attendance"):
    os.makedirs(attendance_dir, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    csv_path = os.path.join(attendance_dir, f"attendance_{date_str}.csv")
    xlsx_path = os.path.join(attendance_dir, f"attendance_{date_str}.xlsx")

    time_now = datetime.now().strftime("%H:%M:%S")

    # Load existing data
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
    else:
        df = pd.DataFrame(columns=["Name", "JobID", "Role", "Department", "Time", "Date"])

    # Check if already marked
    if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
        new_row = {"Name": name, "JobID": jobid, "Role": role, "Department": dept,
                   "Time": time_now, "Date": date_str}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

        df.to_csv(csv_path, index=False)
        df.to_excel(xlsx_path, index=False)
        print(f"Attendance marked for {name}")
    else:
        print(f"{name} already marked today.")
