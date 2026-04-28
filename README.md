# AI Face Recognition System

An advanced AI-based Face Recognition System that performs real-time face detection, emotion analysis, event-based attendance tracking (IN/OUT), and security monitoring with email alerts.

---

##  Features

###  Face Recognition
- Real-time face detection using camera
- Accurate face recognition using trained dataset (face_recognition)

###  Emotion Detection
- Emotion analysis using DeepFace
- Used for smart interaction (e.g., smile-based attendance)

###  Smart Attendance System (Event-Based)
- Continuous system (camera does not shut down)
- Event-based attendance:
  - First detection of the day → **IN (Entry)**
  - Next detection → **OUT (Exit)**
- Prevents duplicate entries using cooldown mechanism
- Stores attendance in CSV file with timestamp

###  Voice Interaction
- “Welcome [Name]” on entry
- “Goodbye [Name]” on exit
- “Please smile” guidance for attendance

###  Unknown Person Detection & Alert
- Detects unknown faces
- Captures multiple images
- Sends email alert with attached images

###  Face Validation (Accuracy Improvements)
- Face size filtering (ignores small/partial faces)
- Blur detection (rejects unclear frames)
- Stability check (multiple frames required before detection)
- Single-face enforcement (prevents multiple face confusion)

###  System Configuration Checker
- Checks system compatibility:
  - RAM
  - CPU
  - GPU
  - OS
  - Camera availability
- Displays warnings if requirements are not met

###  EXE Deployment
- Converted to executable (.exe)
- No need for Python installation
- Stable ONEDIR deployment

---

##  Major Improvements Over Previous Version

| Feature                    | Previous Version                   | Updated Version                            |
|----------------------------|------------------------------------|----------------------------------------------|
| Attendance System          | Basic logging                      | Event-based IN/OUT tracking                  |
| Camera Handling            | Basic                              | Continuous + optimized                       |
| Emotion Detection          | Basic / not used                   | Integrated with attendance                   |
| Unknown Detection          | Not reliable                       | Image capture + email alerts                 |
| Accuracy                   | Low                                | Blur + size + stability filters              |
| User Interaction           | Basic                              | Voice-enabled system                         |
| Deployment                 | Not stable                         | Fully working EXE                            |

---

##  Technologies Used

- Python  
- OpenCV  
- face_recognition  
- DeepFace  
- SQLite  
- Pyttsx3 (Text-to-Speech)  
- PyInstaller  

---

##  Project Structure

```
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
```

---

##  Installation

### 1. Clone the repository
```
git clone https://github.com/AdityaSingh0472/AI-Face-Recognition-System.git
```

### 2. Navigate to project folder
```
cd AI-Face-Recognition-System
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

##  Usage

Run the system:

```
python face_recognition_live.py
```

###  System Workflow

- System performs configuration check  
- Camera starts for real-time detection  
- Face is detected and recognized  
- Emotion is analyzed  
- Attendance is marked (IN/OUT based on event)  
- Voice feedback is given  
- Unknown person → images captured + email alert  

---

##  Output

- Face bounding box  
- Recognized name  
- Emotion display  
- Voice interaction  
- Attendance CSV log  
- Email alerts for unknown person  

---

##  Future Enhancements

- Web-based Admin Panel  
- Cloud database integration  
- Mobile application  
- Multi-camera support  
- Advanced analytics  

---

##  Author

Aditya Singh  

---

## Note

This project was initially developed as a basic system and later enhanced with advanced features, improved accuracy, and real-world usability as part of an internship project.