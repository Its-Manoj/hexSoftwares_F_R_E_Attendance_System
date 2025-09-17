import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if not filepath:
        return

    df = pd.read_csv(filepath) if filepath.endswith(".csv") else pd.read_excel(filepath)

    for col in tree.get_children():
        tree.delete(col)

    tree["columns"] = list(df.columns)
    tree["show"] = "headings"

    for col in df.columns:
        tree.heading(col, text=col)

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

root = tk.Tk()
root.title("Attendance Dashboard")
root.geometry("800x500")


btn = tk.Button(root, text="Open Attendance File", command=load_file)
btn.pack(pady=10)

tree = ttk.Treeview(root)
tree.pack(expand=True, fill="both")

root.mainloop()
