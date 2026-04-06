# AI Face Recognition System

An AI-based Face Recognition System that performs real-time face detection and recognition, detects emotions using DeepFace, automatically marks attendance in a CSV file, and sends email alerts.

---

## Features

* Real-time Face Detection
* Face Recognition
* Emotion Detection using DeepFace
* Automatic Attendance Tracking (CSV)
* Email Notification System

---

## Technologies Used

* Python
* OpenCV
* NumPy
* DeepFace
* Machine Learning

---

## Project Structure

```
AI-Face-Recognition-System/
│
├── dataset/                # Stored face images
├── trainer/                # Trained model files
├── attendance.csv          # Attendance data
├── main.py                 # Main program file
├── face_recognition.py     # Recognition logic
├── emotion_detection.py    # Emotion detection logic
└── README.md
├── database.db             # Stores user data
```

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

Run the main file:

```
python main.py
```

* System will start camera
* Detect and recognize faces
* Track attendance automatically
* Send email alerts

---

## Output

* Face detection with bounding box
* Name recognition
* Emotion display
* Attendance stored in CSV file

---

## Future Improvements

* Web-based dashboard
* Database integration
* Mobile app support
* Improved accuracy using deep learning models

---

## Author

Aditya Singh

---

## Note

This project is developed for learning and internship purposes.
