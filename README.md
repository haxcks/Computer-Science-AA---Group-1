# 🏫 Dorm Curfew Tracker

![Python](https://img.shields.io/badge/Language-Python-blue)
![Status](https://img.shields.io/badge/Status-Active-success)
![Platform](https://img.shields.io/badge/Platform-Console-lightgrey)

> A console-based system designed to monitor dormitory curfew compliance in **PSHS dormitories**.

---

## 📚 Table of Contents
- [Project Description](#-project-description)
- [Objectives](#-objectives)
- [Features](#%EF%B8%8F-features)
- [Program Requirements](#-program-requirements)
- [How to Run the Program](#%EF%B8%8F-how-to-run-the-program)
- [Sample Output](#%EF%B8%8F-sample-output)
- [Authors](#-authors)

---

## 📖 Project Description

This project is a **dormitory curfew monitoring system** designed for **PSHS CALABARZON dormitories**.

The system allows students to:

- ✔ Check in / check out digitally  
- ✔ Record exact attendance time  
- ✔ Determine whether a student is **on time or late**

Dorm managers can monitor dorm attendance and reduce manual tracking.

---

## 🎯 Objectives

| Objective | Description |
|-----------|-------------|
| 1 | Create a digital system for recording dorm curfew attendance |
| 2 | Allow students to easily check in and check out |
| 3 | Automatically determine whether a student is late or on time |

---

## ⚙️ Features

### Core Features

| Feature | Status |
|--------|--------|
| Student login using ID and passkey | ✅ Implemented |
| Automatic time logging using local time API | ⏳ Not yet implemented |
| Real-time dashboard for dorm managers | ⏳ Not yet implemented |
| Late / On-time detection | ✅ Implemented |
| Student attendance database | 🚧 Work in Progress |

---

### Additional Features

| Feature | Status |
|--------|--------|
| Export attendance records for reports | ⏳ Not yet implemented |
| Account management for dorm managers | ⏳ Not yet implemented |
| Real-time updates to dorm staff | ⏳ Not yet implemented |

---

## 💻 Program Requirements

### Programming Language
- `Python 3.9+`

### Tools / Libraries
- `datetime`

---

## ▶️ How to Run the Program

### 1️⃣ Clone the repository

```bash
git clone https://github.com/haxcks/Computer-Science-AA---Group-1.git
```
### 2️⃣ Open the project folder
```bash
cd Computer-Science-AA---Group-1
```
### 3️⃣ Run the program
```bash
python -m src.main
```
## 🖥️ Sample Output

```
----- DORMITORY SYSTEM -----
1 : Student
2 : Manager
3 : Exit
Choice: 1
Student ID: 14-2024-007
Passkey: 1234
Login successful

----- Student Dashboard -----
1 : Check-in
2 : Check-out
3 : View Student Profile
4 : View Student Violations
5 : Logout

Choice: 5
Logging Out...
```

## 👥 Authors
| Name       | Contribution                  |
|------------|-------------------------------|
| Jakob Pabico  | Local API and Main Program |
| Jhustin Alialy   | Main Program |
| Jemdrich Galido  | Main Program |
| Liam Gonzales    | Student Attendance Database  |
| Ae-shin Barrete  |  Check-in/out System   |
* *Main Program referrs to every feature that is not coded already by other members.
