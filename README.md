# 🛡️ SmartShield – IoT Security Monitoring System

A Flask-based IoT Security Monitoring System that helps manage connected devices, monitor security events, and classify potential threats through rule-based detection.

---

## 📌 Project Overview

SmartShield is a web-based IoT security application developed to simplify the monitoring of connected IoT devices. The system enables users to register devices, record security logs, detect suspicious activities, and monitor threats through a centralized dashboard.

This project demonstrates backend development, database management, and full-stack web application development using Python and Flask.

---

## ✨ Features

- 🔹 Register and manage IoT devices
- 🔹 Record device activity logs
- 🔹 Monitor detected threats
- 🔹 Rule-based threat classification
- 🔹 Interactive dashboard
- 🔹 SQLite database integration
- 🔹 Responsive web interface

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### Frontend
- HTML
- CSS

### Database
- SQLite
  
### Development Tools
- VS Code
- Git
- GitHub
  ---

# 📂 Project Structure

```
SmartShield-IoT/
│
├── app.py                 # Flask application
├── smart.db               # SQLite database
├── requirements.txt       # Project dependencies
├── index.html             # Frontend UI
├── static/
│   ├── css/
│   └── images/
└── README.md
```

---

# 🗄 Database Design

The project uses **SQLite** as its database.

### Tables

### 📌 Devices
Stores information about registered IoT devices.

| Column | Description |
|---------|-------------|
| id | Device ID |
| name | Device Name |
| type | Device Type |
| location | Device Location |
| status | Active / Inactive |

---

### 📌 Logs
Stores device activity logs.

| Column | Description |
|---------|-------------|
| id | Log ID |
| device_id | Connected Device |
| activity | Security Event |

---

### 📌 Threats
Stores detected threats with severity.

| Column | Description |
|---------|-------------|
| id | Threat ID |
| device_id | Connected Device |
| activity | Threat Activity |
| severity | Medium / High / Critical |

---

# ⚙️ How to Run the Project

### Clone the repository

```bash
git clone https://github.com/Likith301206/smartshield-iot-security-system.git
```

### Navigate to the project

```bash
cd smartshield-iot-security-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Flask application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```
---

# 📸 Project Screenshots

## 🏠 Dashboard

![Dashboard](assets/images/dashboard.png)

---

## ➕ Add Device

![Add Device](assets/images/add-device.png)

---

## 📝 Add Security Log

![Add Log](assets/images/add-log.png)

---

## 📱 Device Management

![View Devices](assets/images/view-devices.png)

---

## 🚨 Threat Monitoring

![View Threats](assets/images/view-threats.png)
# 🚀 Future Enhancements

The following features can be implemented in future versions:

- 🤖 AI-powered threat detection using Machine Learning
- 🔐 User Authentication & Role-Based Access
- ☁️ Cloud Database Integration
- 📧 Email Alerts for Critical Threats
- 📊 Interactive Analytics Dashboard
- 📱 Mobile-Friendly Responsive Interface
- 🌐 Live IoT Device API Integration

---

# 📚 Learning Outcomes

This project helped me gain practical experience in:

- Python Programming
- Flask Web Framework
- SQLite Database Management
- CRUD Operations
- Backend Development
- Frontend Development
- Database Design
- Git & GitHub
- Problem Solving

---

# 👨‍💻 Author

## Likith S

Computer Science Engineering Student

### Connect with me

- 💼 LinkedIn: https://www.linkedin.com/in/likith-s-798b66383/
- 💻 GitHub: https://github.com/Likith301206

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
