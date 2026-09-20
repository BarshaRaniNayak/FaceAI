from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

app = FastAPI()


# Load OpenCV face detection model
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


@app.get("/")
def home():
    return {
        "success": True,
        "message": "Face Finder AI server is running"
    }


@app.post("/detect")
async def detect_face(file: UploadFile = File(...)):

    # Read uploaded image
    image_data = await file.read()

    # Convert image bytes to NumPy array
    image_array = np.frombuffer(image_data, np.uint8)

    # Convert NumPy array to OpenCV image
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

    # Check if image was read successfully
    if image is None:
        return {
            "success": False,
            "message": "Could not read image"
        }

    # Get original image dimensions
    image_height, image_width = image.shape[:2]

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    detected_faces = []

    # Process every detected face
    for index, (x, y, width, height) in enumerate(faces):

        # Convert pixel coordinates to percentage coordinates
        x_percent = (x / image_width) * 100
        y_percent = (y / image_height) * 100
        width_percent = (width / image_width) * 100
        height_percent = (height / image_height) * 100

        detected_faces.append({
            "id": index + 1,
            "x": x_percent,
            "y": y_percent,
            "width": width_percent,
            "height": height_percent
        })

    print("Image size:", image_width, "x", image_height)
    print("Faces detected:", len(detected_faces))

    return {
        "success": True,
        "message": f"Detected {len(detected_faces)} face(s)",
        "faces": detected_faces
    }
