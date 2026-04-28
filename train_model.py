import face_recognition
import os
import pickle

known_faces = []
known_names = []

dataset_path = "dataset"

print("Training started...\n")

for name in os.listdir(dataset_path):
    folder = os.path.join(dataset_path, name)

    if not os.path.isdir(folder):
        continue

    print(f"Processing: {name}")

    for img in os.listdir(folder):
        path = os.path.join(folder, img)

        try:
            image = face_recognition.load_image_file(path)
            encodings = face_recognition.face_encodings(image)

            
            if len(encodings) != 1:
                print(f"Skipped (invalid face): {img}")
                continue

            encoding = encodings[0]

            
            duplicate = False
            for existing in known_faces:
                distance = face_recognition.face_distance([existing], encoding)[0]
                if distance < 0.4:
                    duplicate = True
                    break

            if duplicate:
                print(f"Skipped (duplicate): {img}")
                continue

            # Add clean data
            known_faces.append(encoding)
            known_names.append(name)

            print(f"Added: {img}")

        except Exception as e:
            print(f"Error processing {img}: {e}")


# SAVE MODEL
data = {
    "encodings": known_faces,
    "names": known_names
}

with open("model.pkl", "wb") as f:
    pickle.dump(data, f)

print("\nModel trained successfully ✅")
print(f"Total faces stored: {len(known_faces)}")