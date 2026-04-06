import face_recognition
import os
import pickle

known_faces = []
known_names = []

for name in os.listdir("dataset"):
    folder = os.path.join("dataset", name)

    for img in os.listdir(folder):
        path = os.path.join(folder, img)

        image = face_recognition.load_image_file(path)
        enc = face_recognition.face_encodings(image)

        if enc:
            known_faces.append(enc[0])
            known_names.append(name)

data = {"encodings": known_faces, "names": known_names}

with open("model.pkl", "wb") as f:
    pickle.dump(data, f)

print("Model Trained ✅")