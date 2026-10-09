Flask Cookies & Sessions Demo Project

A clean and interactive web application built with Python and Flask to demonstrate state management, client-side cookies, server-side session handling, and protected routes.

🌟 Key Features

Cookie Management:

Set Cookie: Store client-side data dynamically in browser cookies.

Read Cookie: Retrieve and display cookies stored on the browser.

Delete Cookie: Clear cookies safely.

Session Management:

User Authentication: Demo login using Flask session handling.

Protected Dashboard: Restrict access to authenticated users only.

Session Status & Info: Live status indicator showing Active or Inactive status.

Logout: Clears active sessions securely.

🛠️ Project Structure

cookies_session_mini_project/
├── app.py                     # Main Flask Application Code
├── static/
│   └── style.css              # Custom Styling & Responsive Layout
└── templates/
    ├── base.html              # Base Layout Template
    ├── index.html             # Home Page (Cookies & Session Demo)
    ├── login.html             # Login Form Page
    ├── dashboard.html         # User Dashboard (Protected Route)
    └── session_info.html     # Active Session Information View



🚀 How to Run the Project Locally

1. Clone the Repository

git clone https://github.com/aaryan6397/cookies_Vs_session_mini_project.git
cd cookies_Vs_session_mini_project



2. Set Up Virtual Environment (Optional but Recommended)

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate



3. Install Dependencies

pip install flask



4. Run the Application

python app.py



Open your browser and navigate to:

http://127.0.0.1:5000/



🔑 Demo Login Credentials

Email: aaryan@gmail.com

Password: Vashu

💻 Tech Stack

Backend: Python, Flask

Frontend: HTML5, CSS3, Jinja2 Templating Engine

📄 License

This project is open-source and free to use for learning purposes.