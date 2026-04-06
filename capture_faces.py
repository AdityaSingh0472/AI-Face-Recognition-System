import cv2
import os
import time
from deepface import DeepFace
import pyttsx3

engine = pyttsx3.init()

name = input("Enter Name: ")
path = f"dataset/{name}"
os.makedirs(path, exist_ok=True)

cam = cv2.VideoCapture(0)

count = 0
TARGET_IMAGES = 5  

last_capture_time = 0

while True:
    ret, frame = cam.read()

    cv2.putText(frame, "Instruction: Smile 😊", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)

    cv2.putText(frame, f"Captured: {count}/{TARGET_IMAGES}", (20,80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)

    #Emotion Detection
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emotion = result[0]['dominant_emotion']
    except:
        emotion = "N/A"

    #Show Emotion
    cv2.putText(frame, f"Emotion: {emotion}", (20,120),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

    current_time = time.time()

    #Capture only when smiling
    if emotion == "happy" and (current_time - last_capture_time > 2):

        cv2.imwrite(f"{path}/{count}.jpg", frame)
        print("Smile detected 😄 → Captured")

        count += 1
        last_capture_time = current_time

    cv2.imshow("Smile Capture System", frame)

    #Stop after 5 images
    if count >= TARGET_IMAGES:
        print("All images captured ✅")

        #Voice: Thank you
        engine.say("Thank you")
        engine.runAndWait()

        break

    if cv2.waitKey(1) == 27:
        break

cam.release()
cv2.destroyAllWindows()