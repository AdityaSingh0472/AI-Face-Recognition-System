import cv2
import face_recognition
import pickle
from utils import get_user, mark_entry_exit, send_alert
from deepface import DeepFace
import pyttsx3

engine = pyttsx3.init()

#Load model
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

known_faces = data["encodings"]
known_names = data["names"]

video = cv2.VideoCapture(0)

#Unknown system
unknown_images = []
capture_count = 0
max_images = 5
email_sent = False

#Voice control
welcomed = False

while True:
    ret, frame = video.read()

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb)
    face_encodings = face_recognition.face_encodings(rgb, face_locations)

    for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):

        #Accurate Face Match
        face_distances = face_recognition.face_distance(known_faces, encoding)

        if len(face_distances) > 0:
            best_match_index = face_distances.argmin()

            if face_distances[best_match_index] < 0.45:
                name = known_names[best_match_index]
            else:
                name = "Unknown"
        else:
            name = "Unknown"

        #Emotion Detection
        face_crop = frame[top:bottom, left:right]

        try:
            result = DeepFace.analyze(face_crop, actions=['emotion'], enforce_detection=False)
            emotion = result[0]['dominant_emotion']
        except:
            emotion = "N/A"

        #Mask Detection (basic logic)
        if emotion == "neutral":
            mask_status = "Mask/Neutral"
        else:
            mask_status = "No Mask"

        

        if name != "Unknown":
            email_sent = False
            capture_count = 0
            unknown_images = []

            user = get_user(name)

            if user:
                display_name = f"{user[1]} (Age: {user[2]})"
            else:
                display_name = name

            #Voice Logic
            if emotion == "happy" and not welcomed:
                engine.say("Access granted")
                engine.runAndWait()

                mark_entry_exit(name)
                welcomed = True

            elif emotion != "happy":
                engine.say("Please smile")
                engine.runAndWait()
                welcomed = False

        else:
            display_name = "Unknown"

            #Capture 5 images
            if capture_count < max_images:
                image_path = f"unknown_{capture_count}.jpg"
                cv2.imwrite(image_path, frame)

                unknown_images.append(image_path)
                capture_count += 1

            #Send email once
            if capture_count == max_images and not email_sent:
                send_alert(unknown_images)
                engine.say("Unknown person detected")
                engine.runAndWait()

                email_sent = True

            welcomed = False

        #UI Text
        text = f"{display_name} ({emotion}) [{mask_status}]"

        color = (0,255,0) if name != "Unknown" else (0,0,255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 3)

        cv2.putText(frame, text, (left, top-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.putText(frame, "Smart AI Surveillance System", (20,40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()