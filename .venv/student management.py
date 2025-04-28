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