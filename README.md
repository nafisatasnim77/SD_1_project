SD_1_project – To-Do List Application

The SD_1_project is a desktop-based To-Do List Application developed using Python. Its objective is to offer a clear and intuitive interface for task management, allowing users to add, update, delete, and save tasks. Data is stored in a JSON file, ensuring tasks persist even after closing the app.


Objectives


Provide an easy-to-use GUI for daily task tracking

Ensure task data persists between sessions via JSON storage

Demonstrate key programming concepts—GUI development, file I/O, and data serialization


Technologies Used


Python 3.x — Core language for scripting

Tkinter — Standard GUI library included with Python

JSON — Structured, human-readable storage format

OS module — For file path operations and filesystem management


🚀 Installation & Setup

Clone the repository:

git clone https://github.com/nafisatasnim77/SD_1_project.git

cd SD_1_project


Run the application:

python "To_DO LIst 1.py"


📌 Features


✅ Add Tasks – Add new tasks to your to-do list

✏️ Update/Edit Tasks – Modify existing tasks

❌ Delete Tasks – Remove tasks from the list

💾 Persistent Storage – Tasks are saved in a JSON file, so they remain after restarting the app

🎨 Graphical User Interface (GUI) – Built with Tkinter for a simple and intuitive interface


📂 Project Structure


SD_1_project/

├── To_DO LIst 1.py     # Main application script

├── tasks.json          # JSON file for storing tasks

├── README.md           # Project documentation


📖 Usage


1.Launch the app using the command above.

2.Use the interface buttons to:

   Add → Type a new task and add it to the list
   
   Update → Edit a selected task
   
   Delete → Remove a selected task
   
   Save → Automatically saves tasks into tasks.json
   
   

🔮 Future Improvements


Potential enhancements that could make the app more powerful:

📅 Add Deadlines – Assign due dates to tasks

⭐ Task Priority – Mark tasks as High/Medium/Low priority

🔔 Reminders/Notifications – Notify users of upcoming tasks

🔍 Search & Filter – Easily find tasks by keyword or status

☁️ Cloud Sync – Store tasks online for access across devices

📱 Mobile Version – Extend the project to Android/iOS


Challenges Faced


Managing real-time updates in the task list via Tkinter

Ensuring consistency of tasks.json when adding, editing, or removing items

Handling file create/read exceptions when the JSON file doesn't exist


🎯 Application Scope


This project is ideal for:

1. Beginners learning Python GUI programming

2. Understanding file handling with JSON
   
3. small-scale personal task management
   

📜 License


This project is developed for educational purposes. You may freely use or modify it for learning and non-commercial use.


👩‍💻 Author


Nafisa Tasnim

email: nafisatasnim189@gmail.com

GitHub: https://github.com/nafisatasnim77

✨ A simple project to organize your daily tasks efficiently!
