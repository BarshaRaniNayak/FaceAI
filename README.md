# 🤖 Face Finder AI

> An AI-powered web application that detects human faces in uploaded images and highlights them with bounding boxes.

![Face Finder AI](https://img.shields.io/badge/Face%20Finder-AI-6366f1?style=for-the-badge)
![React](https://img.shields.io/badge/Frontend-React-61DAFB?style=for-the-badge\&logo=react\&logoColor=black)
![Node.js](https://img.shields.io/badge/Backend-Node.js-339933?style=for-the-badge\&logo=node.js\&logoColor=white)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge\&logo=fastapi\&logoColor=white)
![OpenCV](https://img.shields.io/badge/AI-OpenCV-5C3EE8?style=for-the-badge\&logo=opencv\&logoColor=white)

---

## ✨ Overview

**Face Finder AI** is a full-stack computer vision project that allows users to upload an image and automatically detect human faces.

The application follows a simple AI pipeline:

```text
User
 ↓
React Frontend
 ↓
Node.js / Express
 ↓
FastAPI
 ↓
OpenCV Face Detection
 ↓
Face Coordinates
 ↓
React
 ↓
🟩 Bounding Boxes
```

The project was built to understand how a frontend application can communicate with multiple backend services and a computer-vision model.

---

## 🚀 Features

* 🖼️ Upload images directly from the browser
* 👁️ Automatic human face detection
* 👥 Detect multiple faces in one image
* 📦 Bounding boxes around detected faces
* ⚡ React-based interactive interface
* 🟢 Node.js API layer
* 🐍 FastAPI AI service
* 🤖 OpenCV Haar Cascade face detection
* 🔄 Frontend → Node → FastAPI communication
* 📊 Returns face coordinates through JSON
* 📱 Responsive interface

---

## 🛠️ Tech Stack

### Frontend

* HTML
* CSS
* JavaScript
* React
* Vite

### Backend

* Node.js
* Express.js
* Multer
* Axios
* FormData
* CORS

### AI / Computer Vision

* Python
* FastAPI
* OpenCV
* NumPy
* Haar Cascade Classifier

---

## 📁 Project Structure

```text
face-finder/
│
├── public/
│
├── src/
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
│
├── server/
│   ├── src/
│   │   └── app.js
│   └── package.json
│
├── fastapi/
│   ├── main.py
│   ├── requirements.txt
│   └── venv/
│
├── index.html
├── package.json
├── package-lock.json
└── README.md
```

> `venv/` should **not** be pushed to GitHub. Add it to `.gitignore`.

---

# 🔄 How It Works

## 1. Select Image

The user selects an image through the React interface.

```javascript
const file = event.target.files[0];
```

The selected image is previewed using `FileReader`.

---

## 2. Send Image to Node.js

React creates a `FormData` object:

```javascript
const formData = new FormData();

formData.append("image", selectedImage);
```

The image is then sent to:

```text
POST /api/detect
```

---

## 3. Node.js Receives the Image

Express uses **Multer** to receive the uploaded file.

```javascript
app.post(
  "/api/detect",
  upload.single("image"),
  async (req, res) => {
    // image received
  }
);
```

Node temporarily keeps the image in memory.

---

## 4. Node Sends Image to FastAPI

Node forwards the image to the Python AI service:

```text
Node.js
   ↓
FastAPI
```

FastAPI endpoint:

```text
POST /detect
```

---

## 5. FastAPI Processes the Image

The image is converted into an OpenCV image:

```python
image_array = np.frombuffer(image_data, np.uint8)

image = cv2.imdecode(
    image_array,
    cv2.IMREAD_COLOR
)
```

The image is then converted to grayscale:

```python
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)
```

---

## 6. Face Detection

OpenCV's Haar Cascade classifier detects faces:

```python
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
```

The model returns coordinates such as:

```text
x
y
width
height
```

---

## 7. Convert Coordinates

OpenCV provides coordinates in pixels.

The application converts them into percentages so React can position the bounding boxes responsively.

Example:

```text
Pixel coordinates

x = 300
y = 150
width = 200
height = 250
```

become:

```text
Percentage coordinates

x = 30%
y = 18%
width = 20%
height = 31%
```

---

## 8. Return JSON

FastAPI returns:

```json
{
  "success": true,
  "message": "Detected 2 face(s)",
  "faces": [
    {
      "id": 1,
      "x": 30,
      "y": 18,
      "width": 20,
      "height": 31
    },
    {
      "id": 2,
      "x": 65,
      "y": 20,
      "width": 18,
      "height": 29
    }
  ]
}
```

---

## 9. React Draws Bounding Boxes

React receives the coordinates and dynamically creates the boxes:

```jsx
<div
  className="face-box"
  style={{
    left: `${face.x}%`,
    top: `${face.y}%`,
    width: `${face.width}%`,
    height: `${face.height}%`
  }}
/>
```

Result:

```text
       ┌──────────┐        ┌──────────┐
       │    👤    │        │    👤    │
       │          │        │          │
       └──────────┘        └──────────┘
```

---

# ⚙️ Local Setup

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd face-finder
```

---

# 🎨 Frontend Setup

Install dependencies:

```bash
npm install
```

Start React:

```bash
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

# 🟢 Node.js Setup

Go to the server directory:

```bash
cd server
```

Install dependencies:

```bash
npm install
```

Start the server:

```bash
node src/app.js
```

Node API:

```text
http://localhost:5000
```

---

# 🐍 FastAPI Setup

Go to:

```bash
cd fastapi
```

Create virtual environment:

```bash
python -m venv venv
```

### Windows

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn main:app --reload --port 8000
```

FastAPI:

```text
http://127.0.0.1:8000
```

---

# 📦 requirements.txt

```txt
fastapi
uvicorn
python-multipart
opencv-python
numpy
```

---

# 🔌 API Endpoints

## Node.js

### Health Check

```http
GET /
```

Response:

```json
{
  "success": true,
  "message": "Face Finder backend is running"
}
```

### Face Detection

```http
POST /api/detect
```

Request:

```text
multipart/form-data
image=<image-file>
```

---

## FastAPI

### Health Check

```http
GET /
```

Response:

```json
{
  "success": true,
  "message": "Face Finder AI server is running"
}
```

### Detection

```http
POST /detect
```

Request:

```text
multipart/form-data
file=<image-file>
```

---

# 🔐 Environment Variables

For local development, the API URLs can be written directly.

For production, use environment variables instead.

Example:

```env
VITE_API_URL=https://your-node-api.example.com
```

Node:

```env
FASTAPI_URL=https://your-fastapi-api.example.com
```

Never commit:

```text
.env
```

to GitHub.

---

# 🚀 Deployment Architecture

Production architecture:

```text
                    🌐 Internet
                         │
                         ▼
                  React Frontend
                         │
                         │ HTTPS
                         ▼
                 Node / Express API
                         │
                         │ HTTPS
                         ▼
                   FastAPI Service
                         │
                         ▼
                  OpenCV Detection
                         │
                         ▼
                  Face Coordinates
                         │
                         ▼
                  React Bounding Box
```

---

# 🧪 Example Result

Input:

```text
📷 Image containing multiple people
```

Processing:

```text
React
 ↓
Node
 ↓
FastAPI
 ↓
OpenCV
```

Output:

```text
👤 Face 1 detected
👤 Face 2 detected
```

The application displays bounding boxes around the detected faces.

---

# ⚠️ Limitations

This project currently uses an OpenCV Haar Cascade classifier.

Therefore:

* Detection depends on image quality.
* Very small faces may not be detected.
* Side-facing faces may be missed.
* Poor lighting can reduce detection accuracy.
* False detections are possible.
* It is not intended to identify who a person is.

This project performs **face detection**, not facial recognition.

---

# 🔮 Future Improvements

Possible future versions could include:

* 🎯 More advanced face detection models
* 📷 Webcam/live camera detection
* ⚡ Real-time face detection
* 📊 Confidence scores
* 👤 Face counting
* 🖼️ Drag-and-drop uploads
* 📱 Better mobile UI
* 🧠 Deep-learning-based detection
* 📈 Detection history
* ☁️ Cloud deployment
* 🔒 Better file validation
* 🧪 Automated API testing

---

# 🧠 What I Learned

Building Face Finder AI helped me understand:

* React state management
* React event handling
* File uploads
* FileReader API
* FormData
* REST APIs
* HTTP requests
* Express.js
* Multer
* Axios
* FastAPI
* Python virtual environments
* OpenCV
* NumPy
* Image processing
* Face detection
* Coordinate systems
* Frontend/backend communication
* Microservice-style architecture

---

# 👨‍💻 Author

**Durga Prasad Mishra**

BCA Student
Interested in:

* AI/ML
* Full-Stack Development
* Backend Development
* Computer Vision
* Building practical AI applications

---

# ⭐ Project Goal

The goal of Face Finder AI is to build a simple but complete computer-vision application while learning how modern web applications connect:

```text
Frontend
   +
Backend
   +
Python API
   +
Computer Vision
   =
AI Web Application 🚀
```

---

## 📜 License

This project is created for learning and educational purposes.
