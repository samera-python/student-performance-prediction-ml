 # 🎓 Student Performance Prediction System

> **TL;DR:** Predict students’ Pass/Fail and grades using a Machine Learning model.  
> Works as both a **Tkinter desktop GUI** and a **Django web app**.

A **Machine Learning–based application** that predicts a student's academic performance using attendance, exam scores, and study hours.  
The system predicts both **Pass/Fail** status and **grades**, and comes with **two interfaces**:  
- 🖥️ **Tkinter desktop GUI**  
- 🌐 **Django web app**

---

## ✨ Features

- 🧠 Trained ML model for academic performance prediction  
- 🖥️ User-friendly **Tkinter GUI**  
- 🌐 Interactive **Django web interface**  
- 📊 Predicts **Pass/Fail** and **Grades**  
- 📁 Clean and organized project structure  

---

## 🛠️ Technologies Used

- Python  
- Scikit-learn  
- Joblib  
- Django  
- Tkinter  

---

## 📂 Project Structure

ai_student_system/
├── student_gui.py # Tkinter GUI
├── train_model.py # Script to train ML model
├── student_model.pkl # Trained ML model
├── manage.py # Django project entry
├── requirements.txt # Python dependencies
├── README.md # Project documentation


---

## ▶ How to Run

### 🖥️ GUI Version

1. Install dependencies:

```bash
pip install -r requirements.txt
Run the Tkinter GUI:

python student_gui.py
🌐 Web Version
Install dependencies:

pip install -r requirements.txt
Run Django server:

python manage.py runserver
Open your browser at:
http://127.0.0.1:8000/

📸 Screenshots (Optional)
### Django Web App
![Web Screenshot](assets/web_screenshot.png)

### Tkinter GUI
![GUI Screenshot](assets/gui_screenshot.png)

🚀 Future Improvements
🔐 Add user authentication for the web app

🧠 Support more advanced ML models

☁️ Deploy web app online using Heroku or other cloud platforms

📄 Generate performance reports in PDF

Author:
Samera Haque
CSE Student | Machine Learning Enthusiast

