# API Documentation

## Face Detection API

### FaceDetectionModel

The main class for face detection and recognition operations.

```python
from __face_detector.api import FaceDetectionModel

# Initialize the model
model = FaceDetectionModel('path_to_face_db.p')
```

#### Methods

##### enroll_new_face(images, identifier)
Enrolls a new face into the system.

- **Parameters:**
  - `images`: List of images containing the face
  - `identifier`: String identifier for the face
- **Returns:** None
- **Raises:** ValueError if images are invalid

##### recognize_face(image)
Recognizes a face in the given image.

- **Parameters:**
  - `image`: Image to process
- **Returns:** String identifier of the recognized face
- **Raises:** ValueError if no face is detected

## WebSocket API

### WebSocketServer

Handles real-time communication with clients.

```python
from __websocket_server.api import WebSocketServer

# Initialize the server
server = WebSocketServer(callback=your_callback_function)
```

#### Methods

##### start_server()
Starts the WebSocket server.

- **Parameters:** None
- **Returns:** None
- **Raises:** RuntimeError if server fails to start

##### stop_server()
Stops the WebSocket server.

- **Parameters:** None
- **Returns:** None
- **Raises:** RuntimeError if server fails to stop 