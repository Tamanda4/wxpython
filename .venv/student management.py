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

        btn_frame = tk.Frame(form_frame)
        btn_frame.grid(row=4, column=0, columnspan=2, pady=10)

        tk.Button(btn_frame, text="Add", command=self.add_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Update", command=self.update_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete", command=self.delete_student).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_form).pack(side="left", padx=5)

        search_frame = tk.Frame(self.root)
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="Search:").pack(side="left")
        self.search_entry = tk.Entry(search_frame)
        self.search_entry.pack(side="left", padx=5, fill="x", expand=True)
        tk.Button(search_frame, text="Search", command=self.search_students).pack(side="left", padx=5)
        tk.Button(search_frame, text="Show All", command=self.view_students).pack(side="left", padx=5)

        tree_frame = tk.Frame(self.root)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Course", "Grade"), show="headings")
        for col in ("ID", "Name", "Course", "Grade"):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")
            scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
            self.tree.configure(yscrollcommand=scrollbar.set)

            self.tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            self.tree.bind("<ButtonRelease-1>", self.load_selected_student)


    def validate_inputs(self):
        if not self.id_entry.get().isdigit():
            messagebox.showerror("Error", "ID must be a number!")
            return False
        if not self.name_entry.get().strip():
            messagebox.showerror("Error", "Name is required!")
            return False
        if not self.course_entry.get().strip():
            messagebox.showerror("Error", "Course is required!")
            return False
        return True


    def add_student(self):
        if not self.validate_inputs():
            return

        try:
            self.cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                                (int(self.id_entry.get()),
                                 self.name_entry.get().strip(),
                                 self.course_entry.get().strip(),
                                 self.grade_entry.get().strip() or None))
            self.conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            self.view_students()
            self.clear_form()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Student ID already exists!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error adding student: {str(e)}")


    def update_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "No student selected!")
            return

        if not self.validate_inputs():
            return

        try:
            self.cursor.execute(
                (self.name_entry.get().strip(),
                 self.course_entry.get().strip(),
                 self.grade_entry.get().strip() or None,
                 int(self.id_entry.get())))
            self.conn.commit()
            messagebox.showinfo("Success", "Student updated successfully!")
            self.view_students()
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error updating student: {str(e)}")


    def search_students(self):
        """Search for students based on the search query"""
        query = self.search_entry.get().strip()
        if not query:
            self.view_students()
            return

        try:
            self.tree.delete(*self.tree.get_children())
            self.cursor.execute("""
                SELECT * FROM students 
                WHERE CAST(id AS TEXT) LIKE ? OR name LIKE ? OR course LIKE ?
            """, (f"%{query}%", f"%{query}%", f"%{query}%"))
            for row in self.cursor.fetchall():
                self.tree.insert("", "end", values=row)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error searching students: {str(e)}")



    def delete_student(self):
        selected = self.tree.focus()
        if not selected:
            messagebox.showerror("Error", "No student selected!")
            return

        student_id = self.tree.item(selected)["values"][0]

        if messagebox.askyesno("Confirm", "Are you sure you want to delete this student?"):
            try:
                self.cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
                self.conn.commit()
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.view_students()
                self.clear_form()
            except sqlite3.Error as e:
                messagebox.showerror("Database Error", f"Error deleting student: {str(e)}")




    def view_students(self):
        try:
            self.tree.delete(*self.tree.get_children())
            self.cursor.execute("SELECT * FROM students ORDER BY id")
            for row in self.cursor.fetchall():
                self.tree.insert("", "end", values=row)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error loading students: {str(e)}")

    def load_selected_student(self, event):
        selected = self.tree.focus()
        if selected:
            student = self.tree.item(selected)["values"]
            self.clear_form()
            self.id_entry.insert(0, student[0])
            self.name_entry.insert(0, student[1])
            self.course_entry.insert(0, student[2])
            self.grade_entry.insert(0, student[3] if student[3] else "")

    def clear_form(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)


    def __del__(self):
        if hasattr(self, 'conn'):
            self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()










