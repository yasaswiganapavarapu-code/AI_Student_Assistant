import streamlit as st
import sqlite3
from datetime import date


# -----------------------------
# DATABASE
# -----------------------------

def get_connection():
    return sqlite3.connect("tasks.db")


def create_table():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            priority TEXT NOT NULL,
            deadline TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def add_task(task, priority, deadline):
    conn = get_connection()

    conn.execute(
        """
        INSERT INTO tasks (task, priority, deadline)
        VALUES (?, ?, ?)
        """,
        (task, priority, str(deadline))
    )

    conn.commit()
    conn.close()


def get_tasks():
    conn = get_connection()

    tasks = conn.execute(
        """
        SELECT id, task, priority, deadline, completed
        FROM tasks
        ORDER BY deadline
        """
    ).fetchall()

    conn.close()

    return tasks


def update_task_status(task_id, completed):
    conn = get_connection()

    conn.execute(
        """
        UPDATE tasks
        SET completed = ?
        WHERE id = ?
        """,
        (int(completed), task_id)
    )

    conn.commit()
    conn.close()


# Create database table
create_table()


# -----------------------------
# APP
# -----------------------------

st.set_page_config(
    page_title="AI Student Productivity Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Student Productivity Assistant")
st.write("Organize your studies smarter! 🤖")


# -----------------------------
# ADD TASK
# -----------------------------

st.subheader("📝 Add a New Task")

task = st.text_input("Enter your task")

priority = st.selectbox(
    "Select priority",
    ["🔴 High", "🟡 Medium", "🟢 Low"]
)

deadline = st.date_input(
    "Select deadline",
    min_value=date.today()
)

if st.button("Add Task"):

    if task.strip():

        add_task(task.strip(), priority, deadline)

        st.success("Task saved successfully! 💾")
        st.rerun()

    else:
        st.warning("Please enter a task.")


# -----------------------------
# GET TASKS
# -----------------------------

tasks = get_tasks()


# -----------------------------
# SMART PLANNER
# -----------------------------

st.subheader("🤖 Smart Planner")

if tasks:

    priority_value = {
        "🔴 High": 1,
        "🟡 Medium": 2,
        "🟢 Low": 3
    }

    incomplete_tasks = [
        task for task in tasks
        if task[4] == 0
    ]

    sorted_tasks = sorted(
        incomplete_tasks,
        key=lambda x: (
            priority_value[x[2]],
            x[3]
        )
    )

    if sorted_tasks:

        st.write("### ⭐ Suggested order")

        for index, item in enumerate(sorted_tasks):

            st.write(
                f"**{index + 1}. {item[1]}**  \n"
                f"{item[2]} | 📅 {item[3]}"
            )

    else:
        st.success("🎉 All your tasks are completed!")


# -----------------------------
# YOUR TASKS
# -----------------------------

st.subheader("📋 Your Tasks")

if tasks:

    for item in tasks:

        task_id = item[0]
        task_name = item[1]
        priority = item[2]
        deadline = item[3]
        completed = bool(item[4])

        new_status = st.checkbox(
            f"{task_name} | {priority} | 📅 {deadline}",
            value=completed,
            key=f"task_{task_id}"
        )

        if new_status != completed:
            update_task_status(task_id, new_status)
            st.rerun()

else:

    st.info("No tasks added yet.")