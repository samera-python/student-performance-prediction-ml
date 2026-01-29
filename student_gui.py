import tkinter as tk
from tkinter import messagebox
import joblib
import os

# ------------------- Load Model -------------------
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'student_model.pkl')

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Model loaded successfully!")
except Exception as e:
    print("❌ Failed to load model:", e)
    model = None

# ------------------- Grading Function -------------------
def get_grade(total_score):
    """
    Maps numeric total_score to grade, grade point, and remarks.
    """
    if 80 <= total_score <= 100:
        return "A+", 4.00, "Outstanding"
    elif 75 <= total_score <= 79:
        return "A", 3.75, "Excellent"
    elif 70 <= total_score <= 74:
        return "A−", 3.50, "Very Good"
    elif 65 <= total_score <= 69:
        return "B+", 3.25, "Good"
    elif 60 <= total_score <= 64:
        return "B", 3.00, "Satisfactory"
    elif 55 <= total_score <= 59:
        return "B−", 2.75, "Above Average"
    elif 50 <= total_score <= 54:
        return "C+", 2.50, "Average"
    elif 45 <= total_score <= 49:
        return "C", 2.25, "Below Average"
    elif 40 <= total_score <= 44:
        return "D", 2.00, "Pass"
    else:
        return "F", 0.00, "Fail"

# ------------------- Prediction Function -------------------
def predict():
    if not model:
        messagebox.showerror("Error", "Model not loaded!")
        return

    try:
        # Read input values
        name = entry_name.get()
        attendance = float(entry_attendance.get())
        midterm = float(entry_midterm.get())
        final = float(entry_final.get())
        study_hours = float(entry_study_hours.get())

        # Validation
        if not (0 <= attendance <= 100):
            raise ValueError("Attendance must be 0-100")
        if not (0 <= midterm <= 25):
            raise ValueError("Midterm score must be 0-25")
        if not (0 <= final <= 40):
            raise ValueError("Final score must be 0-40")
        if study_hours < 0:
            raise ValueError("Study hours cannot be negative")

        # Prediction
        features = [[attendance, midterm, final, study_hours]]
        numeric_score = model.predict(features)[0]

        # Convert numeric_score to grade
        grade, grade_point, remarks = get_grade(numeric_score)

        show_custom_popup("Prediction Result",
                          f"Name: {name}\n"
                          f"Total Score: {numeric_score}\n"
                          f"Grade: {grade}\n"
                          f"Grade Point: {grade_point}\n"
                          f"Remarks: {remarks}")

    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

# ------------------- Big Popup -------------------
def show_custom_popup(title, text):
    popup = tk.Toplevel(root)
    popup.title(title)
    popup.geometry("600x400")  # Large popup
    popup.resizable(False, False)
    popup.config(bg="#f5f5f5")  # Light background

    frame = tk.Frame(popup, bg="#f5f5f5")
    frame.pack(expand=True, fill="both")

    label = tk.Label(frame, text=text, font=("Arial", 28, "bold"),
                     fg="black", bg="#f5f5f5", justify="center")
    label.pack(expand=True)

    tk.Button(popup, text="OK", command=popup.destroy,
              font=("Arial", 20), bg="gray", fg="white").pack(pady=20)

# ------------------- Main Window -------------------
root = tk.Tk()
root.title("Student Prediction System")
root.geometry("800x600")  # Large main window
root.resizable(False, False)
root.config(bg="#f5f5f5")  # Light background

# Title
tk.Label(root, text="Student Prediction Form",
         font=("Arial", 32, "bold"), fg="black", bg="#f5f5f5").pack(pady=20)

# Input Frame
frame_inputs = tk.Frame(root, bg="#f5f5f5")
frame_inputs.pack(pady=20)

# Helper function to add label + entry
def add_field(frame, text, row):
    tk.Label(frame, text=text, font=("Arial", 24), fg="black", bg="#f5f5f5").grid(row=row, column=0, padx=10, pady=10, sticky="w")
    entry = tk.Entry(frame, font=("Arial", 20), width=10)
    entry.grid(row=row, column=1, padx=10, pady=10)
    return entry

# Create fields
entry_name = add_field(frame_inputs, "Name", 0)
entry_attendance = add_field(frame_inputs, "Attendance (%)", 1)
entry_midterm = add_field(frame_inputs, "Midterm Score (0-25)", 2)
entry_final = add_field(frame_inputs, "Final Score (0-40)", 3)
entry_study_hours = add_field(frame_inputs, "Study Hours", 4)

# Predict Button
tk.Button(root, text="Predict", command=predict,
          font=("Arial", 28, "bold"), bg="#4CAF50", fg="white").pack(pady=30)

root.mainloop()
