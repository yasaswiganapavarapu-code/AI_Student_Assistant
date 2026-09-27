# 🎓 AI Student Productivity Assistant

A simple and practical productivity web application built with Python and Streamlit to help students organize and prioritize their academic tasks.

## ✨ Features

- 📝 Add academic tasks
- ⭐ Set task priority
- 📅 Set deadlines
- ✅ Mark tasks as completed
- 🤖 Smart Planner suggests a task order
- 💾 SQLite database for permanent task storage
- 🌐 Simple and interactive web interface

## 🛠️ Technologies Used

- Python
- Streamlit
- SQLite
- SQL
- Git & GitHub

## 🧠 How It Works

The application allows students to enter a task along with its priority and deadline.

The Smart Planner organizes incomplete tasks based on:

1. Priority
2. Deadline

Tasks are stored in a local SQLite database so they remain available when the application is restarted.

## 📂 Project Structure

```text
AI_Student_Assistant/
│
├── app.py
├── requirements.txt
├── .gitignore
└── tasks.db