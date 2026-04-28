import cv2
import os
import time
from deepface import DeepFace
import pyttsx3
import face_recognition

engine = pyttsx3.init()

name = input("Enter Name: ")
path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)

count = 0
TARGET_IMAGES = 5
last_capture_time = 0

reference_encoding = None

# NEW: no face timer
no_face_start_time = time.time()
NO_FACE_TIMEOUT = 30

while True:
    ret, frame = cam.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)

    cv2.putText(frame, "Instruction: Smile 😊", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)

    cv2.putText(frame, f"Captured: {count}/{TARGET_IMAGES}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # NO FACE HANDLING
    if len(encodings) == 0:
        cv2.putText(frame, "No face detected...", (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        if time.time() - no_face_start_time > NO_FACE_TIMEOUT:
            print("No face detected. Closing camera...")

            engine.say("No face detected, closing camera")
            engine.runAndWait()
            break
    else:
        no_face_start_time = time.time()

    # SET REFERENCE FACE
    if reference_encoding is None and len(encodings) > 0:
        reference_encoding = encodings[0]
        print("Reference face locked ✅")

    # FACE MATCH CHECK
    same_person = False
    if reference_encoding is not None and len(encodings) > 0:
        distance = face_recognition.face_distance([reference_encoding], encodings[0])[0]

        if distance < 0.5:
            same_person = True

    # DIFFERENT PERSON DETECTED → HARD STOP
    if reference_encoding is not None and not same_person and len(encodings) > 0:
        cv2.putText(frame, "Different person detected!", (20, 160),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        print("❌ Different person detected. Restart required.")

        engine.say("Different person detected. Please restart.")
        engine.runAndWait()

        time.sleep(2)
        break  

    # EMOTION DETECTION
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
    except:
        emotion = "N/A"

    cv2.putText(frame, f"Emotion: {emotion}", (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    current_time = time.time()

    # CAPTURE ONLY SAME PERSON
    if same_person and emotion == "happy" and (current_time - last_capture_time > 2):
        cv2.imwrite(f"{path}/{count}.jpg", frame)
        print("Smile detected 😄 → Captured")

        count += 1
        last_capture_time = current_time

    cv2.imshow("Smile Capture System", frame)

    if count >= TARGET_IMAGES:
        print("All images captured ✅")

        engine.say("Thank you")
        engine.runAndWait()
        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()