import cv2
import face_recognition
import pickle
from utils import get_user, mark_entry_exit, send_alert
from deepface import DeepFace
import pyttsx3
import time

engine = pyttsx3.init()

# Load trained model
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

known_faces = data["encodings"]
known_names = data["names"]

video = cv2.VideoCapture(0)

# ===== ATTENDANCE SETTINGS =====
attendance_marked = {}
ATTENDANCE_DELAY = 10

smile_count = 0
SMILE_REQUIRED_FRAMES = 3

# ===== UNKNOWN DETECTION SETTINGS =====
unknown_frame_count = 0
REQUIRED_FRAMES = 5
capture_count = 0
max_images = 5
unknown_images = []
email_sent = False

# ===== FILTER SETTINGS =====
MIN_FACE_SIZE = 80


def is_blurry(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var() < 50


while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    # Avoid multiple face confusion
    if len(face_encodings) > 1:
        cv2.putText(frame, "Multiple faces detected!", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == 27:
            break
        continue

    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):

        # ===== FACE SIZE FILTER =====
        if (right - left) < MIN_FACE_SIZE or (bottom - top) < MIN_FACE_SIZE:
            continue

        face_crop = frame[top:bottom, left:right]

        # ===== BLUR FILTER =====
        if is_blurry(face_crop):
            continue

        # ===== FACE RECOGNITION =====
        face_distances = face_recognition.face_distance(known_faces, encoding)

        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()
            if face_distances[best_match_index] < 0.45:
                name = known_names[best_match_index]
            else:
                name = "Unknown"
        else:
            name = "Unknown"

        # ===== EMOTION DETECTION =====
        try:
            result = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        except:
            emotion = "N/A"

        current_time = time.time()

        # ================= KNOWN PERSON =================
        if name != "Unknown":

            # Reset unknown tracking
            unknown_frame_count = 0
            capture_count = 0
            unknown_images = []
            email_sent = False

            user = get_user(name)
            person_name = user[1] if user else name

            if name not in attendance_marked:
                attendance_marked[name] = 0

            # Smile detection
            if emotion == "happy":
                smile_count += 1
            else:
                smile_count = 0

            # ===== EVENT-BASED ATTENDANCE =====
            if smile_count >= SMILE_REQUIRED_FRAMES:
                if current_time - attendance_marked[name] > ATTENDANCE_DELAY:

                    status = mark_entry_exit(name)

                    if status == "IN":
                        engine.say(f"Welcome {person_name}")
                    else:
                        engine.say(f"Goodbye {person_name}")

                    engine.runAndWait()

                    attendance_marked[name] = current_time
                    smile_count = 0

            else:
                cv2.putText(frame, "Please smile 😊", (20, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        # ================= UNKNOWN PERSON =================
        else:
            unknown_frame_count += 1

            # Stability check
            if unknown_frame_count < REQUIRED_FRAMES:
                continue

            # Capture images
            if capture_count < max_images:
                img_path = f"unknown_{capture_count}.jpg"
                cv2.imwrite(img_path, frame)
                unknown_images.append(img_path)
                capture_count += 1
                print("Capturing unknown:", capture_count)

            # Send email alert
            if capture_count >= max_images and not email_sent:
                send_alert(unknown_images)

                engine.say("Unknown person detected")
                engine.runAndWait()

                email_sent = True

        # ===== UI =====
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, f"{name} ({emotion})", (left, top - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()