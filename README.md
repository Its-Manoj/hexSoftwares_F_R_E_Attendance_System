# F_R_E_Attendance_System_V2

## Steps to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Add employees in `employees.csv`:
   ```csv
   Name,JobID,Role,Department
   manoj_kumar,101,Software Engineer,IT
   ```

3. Capture images:
   ```bash
   python capture_images.py
   ```

4. Train recognizer:
   ```bash
   python train.py
   ```

5. Run attendance system:
   ```bash
   python main.py
   ```

6. Attendance logs are saved in `attendance/` (CSV + Excel).
7. View logs using dashboard:
   ```bash
   python dashboard.py
   ```
