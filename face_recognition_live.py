import cv2
import face_recognition
import pickle
from utils import get_user, mark_entry_exit, send_alert
from deepface import DeepFace
import pyttsx3
from system_check_module import run_system_check
import time
import sys
import os


# RESOURCE PATH

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# RUN SYSTEM CHECK

run_system_check()

engine = pyttsx3.init()


# LOAD MODEL 

with open(resource_path("model.pkl"), "rb") as f:
    data = pickle.load(f)

known_faces = data["encodings"]
known_names = data["names"]

print("Loaded faces:", len(known_faces))  # debug

video = cv2.VideoCapture(0)


# UNKNOWN SYSTEM
unknown_images = []
capture_count = 0
max_images = 5
email_sent = False

# ENTRY / EXIT TRACKING

last_action = {}


# DELAY CONTROL
last_spoken_time = 0
SPEAK_DELAY = 3


# EXIT CONTROL

exit_program = False

while True:
    ret, frame = video.read()
    if not ret:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):

        face_distances = face_recognition.face_distance(known_faces, encoding)

        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()

            if face_distances[best_match_index] < 0.45:
                name = known_names[best_match_index]
            else:
                name = "Unknown"
        else:
            name = "Unknown"

        
        # EMOTION DETECTION
        
        face_crop = frame[top:bottom, left:right]

        try:
            result = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        except:
            emotion = "N/A"

        mask_status = "Mask/Neutral" if emotion == "neutral" else "No Mask"

        current_time = time.time()

        
        # KNOWN PERSON
        
        if name != "Unknown":
            email_sent = False
            capture_count = 0
            unknown_images = []

            user = get_user(name)

            if user:
                display_name = f"{user[1]} (Age: {user[2]})"
                person_name = user[1]
            else:
                display_name = name
                person_name = name

            if name not in last_action:
                last_action[name] = "OUT"

            # ENTRY
            if last_action[name] == "OUT" and emotion == "happy":
                if current_time - last_spoken_time > SPEAK_DELAY:
                    engine.say(f"Welcome {person_name}")
                    engine.runAndWait()
                    time.sleep(1)

                    mark_entry_exit(name)
                    last_action[name] = "IN"
                    last_spoken_time = current_time

                    exit_program = True
                    break

            # EXIT
            elif last_action[name] == "IN" and emotion == "happy":
                if current_time - last_spoken_time > SPEAK_DELAY:
                    engine.say(f"Goodbye {person_name}")
                    engine.runAndWait()
                    time.sleep(1)

                    mark_entry_exit(name)
                    last_action[name] = "OUT"
                    last_spoken_time = current_time

                    exit_program = True
                    break

            # NOT SMILING
            elif emotion != "happy":
                if current_time - last_spoken_time > SPEAK_DELAY:
                    engine.say("Please smile")
                    engine.runAndWait()
                    last_spoken_time = current_time

        
        # UNKNOWN PERSON
        
        else:
            display_name = "Unknown"

            if capture_count < max_images:
                image_path = f"unknown_{capture_count}.jpg"
                cv2.imwrite(image_path, frame)

                unknown_images.append(image_path)
                capture_count += 1

                print("Capturing:", capture_count)

            if capture_count >= max_images and not email_sent:
                if current_time - last_spoken_time > SPEAK_DELAY:
                    send_alert(unknown_images)
                    engine.say("Unknown person detected")
                    engine.runAndWait()

                    email_sent = True
                    last_spoken_time = current_time

                    capture_count = 0
                    unknown_images = []

        
        # UI DISPLAY
        
        text = f"{display_name} ({emotion}) [{mask_status}]"
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, text, (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    if exit_program:
        break

    cv2.putText(frame, "Smart AI Surveillance System", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()