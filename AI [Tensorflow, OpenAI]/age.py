import cv2
import face_recognition

def detect_age(image_path):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find all face landmarks in the image
    face_landmarks = face_recognition.face_landmarks(image)

    # Check if a face is detected
    if not face_landmarks:
        print("No face detected.")
        return

    # Extract facial features for age estimation
    facial_features = face_landmarks[0]
    left_eye = facial_features['left_eye']
    right_eye = facial_features['right_eye']

    # Calculate the distance between the eyes
    eye_distance = cv2.norm(left_eye[0], right_eye[-1])

    # Load the age model
    age_model = cv2.face.AGE_MODEL
    age_net = cv2.dnn.readNet(age_model)

    # Prepare the input image for age prediction
    blob = cv2.dnn.blobFromImage(image, size=(256, 256), ddepth=cv2.CV_8U)
    age_net.setInput(blob)

    # Perform forward pass and get the age prediction
    age_preds = age_net.forward()

    # Get the predicted age
    predicted_age = int(age_preds[0].argmax())

    print(f"Predicted Age: {predicted_age}")

# Test the age detector with an example image
image_path = 'path/to/your/image.jpg'
detect_age(image_path)
