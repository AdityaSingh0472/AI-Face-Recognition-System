# AI Face Recognition System

An advanced AI-based Face Recognition System that performs real-time face detection, emotion analysis, automated attendance tracking (Entry/Exit), and security monitoring with email alerts. The system is fully deployed as an executable (.exe) application for real-world use.
---

## Features

### Face Recognition System
- Real-time face detection using camera
- Accurate face matching with trained dataset

### Emotion Detection
- Detects user emotions using DeepFace
- Enables smart interaction based on emotion

### Smart Attendance System
- Entry (IN) and Exit (OUT) tracking
- Stores attendance in CSV file

### Voice Interaction
- “Welcome [Name]” on entry
- “Goodbye [Name]” on exit
- “Please smile” guidance

### Unknown Person Alert System
- Captures images of unknown person
- Sends email alerts with attachments

### System Configuration Checker
- Checks:
  - RAM
  - CPU
  - GPU
  - OS
  - Camera availability
- Shows warning if system requirements are not met

### Auto Camera Control
- Camera closes automatically after attendance
- Optimized performance

### EXE Deployment (Major Update 🔥)
- Project converted into executable (.exe)
- No need for Python installation
- Stable ONEDIR deployment
- Previous EXE errors fixed

---

## 🆕 Major Improvements Over Previous Version

| Feature                     | Previous Version ❌                     | Updated Version ✅                          |
|---------------------------|----------------------------------------|---------------------------------------------|
| Attendance System          | Basic attendance only                  | Entry (IN) & Exit (OUT) tracking implemented |
| Voice Interaction          | Not available                          | Smart voice feedback (Welcome/Goodbye)       |
| System Configuration Check | Not available                          | Hardware validation (CPU, RAM, Camera, etc.) |
| EXE Deployment             | Unstable / Not working properly        | Fully stable and functional (.exe supported) |
| Camera Handling            | Continuous running                     | Auto start & auto stop optimized             |
| User Experience            | Basic and non-interactive              | Interactive, user-friendly system            |

🛠 Technologies Used

- Python
- OpenCV
- face_recognition
- DeepFace
- SQLite
- Pyttsx3 (Text-to-Speech)
- PyInstaller (for EXE deployment)

---

## 📁 Project Structure

AI-Face-Recognition-System/
│
├── dataset/
├── model.pkl
├── database.db
├── face_recognition_live.py
├── system_check_module.py
├── utils.py
├── train_model.py
└── README.md

---

## Installation

1. Clone the repository:

```
git clone https://github.com/AdityaSingh0472/AI-Face-Recognition-System.git
```

2. Navigate to project folder:

```
cd AI-Face-Recognition-System
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

🔹 Run via Python

```
python face_recognition_live.py
```

- The system initializes and performs a system configuration check  
- The camera starts automatically for real-time face detection  
- Faces are detected and recognized using the trained model  
- Emotion is analyzed to enable smart interaction  
- Attendance is automatically marked as Entry (IN) or Exit (OUT)  
- Voice feedback is provided (Welcome / Goodbye / Please smile)  
- If an unknown person is detected, images are captured and an email alert is sent  
- The camera automatically closes after completing the process  

---

## Output

Face detection with bounding box
Name recognition
Emotion display
Voice feedback
Attendance tracking
Email alerts for unknown person

---


## Future Enhancements
Web-based dashboard
Cloud database integration
Mobile application
Multi-camera support
Advanced analytics

---



## Author

Aditya Singh

---

## Note

👨‍💻 Author

Aditya Singh

📌 Note

This project was initially developed as a basic system and later enhanced with advanced features, improved performance, and full deployment support as part of an internship project.
