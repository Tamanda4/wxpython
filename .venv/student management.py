import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")


        self.conn = sqlite3.connect("student_database.db")
        self.cursor = self.conn.cursor()
        self.create_table()


        self.create_widgets()
        self.view_students()

    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    course TEXT NOT NULL,
                    grade TEXT
                )
            ''')
            self.conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error creating table: {str(e)}")
    def create_widgets(self):
        form_frame = tk.LabelFrame(self.root, text="Student Form", padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(form_frame, text="ID*").grid(row=0, column=0, sticky="w")
        self.id_entry = tk.Entry(form_frame)
        self.id_entry.grid(row=0, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(form_frame, text="Name*").grid(row=1, column=0, sticky="w")
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(form_frame, text="Course*").grid(row=2, column=0, sticky="w")
        self.course_entry = tk.Entry(form_frame)
        self.course_entry.grid(row=2, column=1, pady=5, padx=5, sticky="ew")

        tk.Label(form_frame, text="Grade").grid(row=3, column=0, sticky="w")
        self.grade_entry = tk.Entry(form_frame)
        self.grade_entry.grid(row=3, column=1, pady=5, padx=5, sticky="ew")

