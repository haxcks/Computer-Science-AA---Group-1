# 💻 Dorm Curfew Tracker - Technical Documentation

## Project Overview
The Dorm Curfew Tracker is a console-based program that monitors student check-ins and check-outs in dormitories. It is designed for PSHS dorms and helps dorm managers track attendance in real time.

## Project Structure
```
dorm-curfew-tracker/
│
├── README.md
├── src/
│ ├── main.py # Program entry point and UI
│ └── database.py # Handles student attendance data
└── docs/
└── technical_doc.md
```

## Dependencies
- Python 3.9+
- Standard libraries: `datetime`

## Code Overview
- **main.py**  
  - Handles program flow
  - Manages login for students and dorm managers
  - Records check-in/check-out times
- **TimeAPI.py**
  - Uses ZoneInfo and Datetime to get the time

## How the System Works
1. A user (student or dorm manager) logs in.
2. The system records the local time using the Python `datetime` library.
3. Student check-ins and check-outs are stored in the database.
4. Dorm managers can view real-time attendance and export records.

## Notes / Limitations
- The dashboard and automated time API features are **not fully implemented yet**.
- Only console-based; no GUI or web interface yet.
- Current implementation does not synchronize with fingerprint scanners.
