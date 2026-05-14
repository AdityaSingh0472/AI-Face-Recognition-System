# AI Face Recognition System

An advanced AI-based Face Recognition System that performs real-time face detection, emotion analysis, event-based attendance tracking (IN/OUT), and security monitoring with email alerts.

---

# Features

## Face Recognition
- Real-time face detection using camera
- Accurate face recognition using trained dataset
- Single-face validation to avoid multiple face confusion

## Emotion Detection
- Emotion analysis using DeepFace
- Smile-based interaction system

## Smart Attendance System (Event-Based)
- Continuous camera monitoring
- Event-based attendance system:
  - First detection of the day → **IN**
  - Next detection → **OUT**
- Automatic attendance logging with timestamp
- Cooldown mechanism to prevent duplicate entries

## Voice Interaction
- “Welcome [Name]” on entry
- “Goodbye [Name]” on exit
- “Please smile” guidance for attendance

## Unknown Person Detection & Email Alerts
- Detects unknown persons in real time
- Captures multiple images of unknown person
- Sends automatic email alerts with attachments

## Face Validation & Accuracy Improvements
- Blur detection to ignore unclear faces
- Face size filtering to ignore small/partial faces
- Stability check using multiple frames before detection
- Improved recognition accuracy and reduced false detection

## System Configuration Checker
Checks:
- RAM
- CPU
- GPU
- Operating System
- Camera availability

Displays warning if system requirements are not met.

## EXE Deployment
- Fully converted into executable (.exe)
- No Python installation required
- Stable ONEDIR deployment using PyInstaller

---

# Major Improvements Over Previous Version

| Feature | Previous Version ❌ | Updated Version ✅ |
|----------|--------------------|--------------------|
| Attendance System | Basic attendance logging | Event-based IN/OUT attendance |
| Emotion Detection | Basic / unused | Integrated smile-based interaction |
| Unknown Detection | Basic detection only | Image capture + email alerts |
| Accuracy | More false detection | Blur + size + stability validation |
| User Experience | Basic | Interactive voice-enabled system |
| Camera Handling | Basic | Continuous monitoring |
| Deployment | Unstable EXE | Stable executable deployment |

---

# Technologies Used

- Python
- OpenCV
- face_recognition
- DeepFace
- SQLite
- Pyttsx3 (Text-to-Speech)
- PyInstaller

---

# Project Structure

```plaintext
AI-Face-Recognition-System/
│
├── dataset/
├── model.pkl
├── database.db
├── attendance.csv
├── face_recognition_live.py
├── capture_faces.py
├── train_model.py
├── utils.py
├── system_check_module.py
└── README.md
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/AdityaSingh0472/AI-Face-Recognition-System.git
```

## 2. Navigate to Project Folder

```bash
cd AI-Face-Recognition-System
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

Run the project:

```bash
python face_recognition_live.py
```

---

# System Workflow

1. System performs configuration check
2. Camera starts automatically
3. Face is detected and recognized
4. Emotion is analyzed using DeepFace
5. Attendance is marked as IN or OUT
6. Voice feedback is provided
7. Unknown person detection triggers:
   - Image capture
   - Email alert system

---

# Output

- Real-time face recognition
- Emotion display
- Attendance tracking (IN/OUT)
- Voice interaction
- CSV attendance logs
- Unknown person email alerts

---

# Future Enhancements

- Web-based Admin Panel
- Cloud Database Integration
- Mobile Application
- Multi-Camera Support
- Advanced Analytics Dashboard
- Body Movement Verification

---

# Author

**Aditya Singh**

---

# Note

This project was initially developed as a basic face recognition system and later enhanced with advanced features, improved accuracy, event-based attendance handling, and real-world usability as part of an internship project.