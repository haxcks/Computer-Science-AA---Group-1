<div align="center">

# 🏫 Dorm Curfew Tracker

[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](#-dorm-curfew-tracker)
[![Platform](https://img.shields.io/badge/Platform-Terminal-lightgrey?style=for-the-badge&logo=zsh)](#-dorm-curfew-tracker)
[![License](https://img.shields.io/github/license/haxcks/Computer-Science-AA---Group-1?style=for-the-badge)](https://github.com/haxcks/Computer-Science-AA---Group-1/blob/main/LICENSE)

> A Python-based dormitory monitoring and notification system designed to automate student check-ins, enforce curfew policies, and improve accountability.

</div>

---

## 📚 Table of Contents
- [Final Paper](#-final-paper)
- [Overview](#-overview)
- [Objectives](#-objectives)
- [Features](#-features)
- [Tech Stack](#%EF%B8%8F-tech-stack)
- [Project Structure](#-project-structure)
- [Sample Output](#%EF%B8%8F-sample-output)
- [Installation & Usage](#%EF%B8%8F-installation--usage)
- [System Architecture](#-system-architecture)
- [Authors](#-authors)

---

## 📝 Final Paper 
- [Final Paper](https://github.com/haxcks/Computer-Science-AA---Group-1/blob/main/CSAA_FinalPaper.pdf)
---

## 📖 Overview

The **Dorm Curfew Tracker** replaces traditional dorm logbooks with a **real-time automated system**. It records student activity, detects curfew violations, and minimizes human error while improving communication between dorm managers, students, and guardians.

---

## 🎯 Objectives

* Track student check-in/check-out activity
* Implement secure role-based authentication
* Detect and log curfew violations
* Provide a management dashboard

---

## ✨ Features

### 🔐 Core Features

* Role-based login (**Student / Manager**)
* Secure authentication using **SHA-256 hashing**
* Real-time check-in/check-out tracking
* Automatic curfew violation detection
* JSON-based persistent storage
* Manager dashboard (CRUD operations)
* Student interface (profile, history, violations)

---

### ⚡ Additional Features

Click to expand

* 🌍 Timezone-aware tracking (`zoneinfo`)
* 🧱 Atomic file handling (`os`, `pathlib`)
* 📜 PEP 8 compliant structure

---

## 🛠️ Tech Stack

| Component      | Technology           |
| -------------- | -------------------- |
| Language       | Python 3.9+          |
| Database       | JSON (Local Storage) |
| Authentication | hashlib (SHA-256)    |
| Time Handling  | datetime + zoneinfo  |
| File Handling  | os, pathlib          |

---

## 📂 Project Structure

```
DormCurfewTracker/
│── main.py
│── manager.py
│── student.py
│
├── API/
│   ├── TimeAPI.py
│   ├── time.timeapi
│
├── Helpers/
│   ├── db.py 
│   ├── HashHelper.py
│
├── DataBase/
│   ├── students.json
│   ├── managers.json
│   ├── history.json
│   ├── violations.json
│
```

---

## 🖥️ Sample Output

```
----- INTERFACE -----
        [1.] Student
        [2.] Manager
        [3.] Exit
1
Student ID: 14-2024-01
Passkey: 12345
Login successful

----- Student Dashboard -----
1 : Check-in
2 : Check-out
3 : View Student Profile
4 : View Student Violations
5 : Logout

Choice: 3 

---- Profile ----
Name: Jhustin Jane C. Alialy
Room: 210
Status: IN
```

---

## ⚙️ Installation & Usage

```bash
# Clone repository
git clone https://github.com/haxcks/Computer-Science-AA---Group-1.git

# Navigate into project
cd Computer-Science-AA---Group-1/src

# Run program
python main.py
```

---

## 🧠 System Architecture

### Modules

* **Time API**

  * Handles timezone-aware time tracking

* **Main**

  * Entry point with role selection

* **Manager System**

  * Admin controls (add/remove students/managers, view data)

* **Student System**

  * Check-in/out and profile management

* **Database**

  * JSON-based persistent storage

---

## 👥 Authors

* **Jakob Pabico**
* **Jhustin Alialy**
* **Jemdrich Galido**
* **Ae-shin Barrete**
* **Liam Gonzales**

---

