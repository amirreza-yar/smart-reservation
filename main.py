"""
Main entry point for the Smart Reservation Project backend.

This module initializes and coordinates the face detection system and WebSocket server
for real-time communication. It handles the integration between face detection
capabilities and client communication through WebSocket.

Author: [Your Name]
Date: [Current Date]
"""

from __websocket_server.api import WebSocketServer
from __face_detector.api import FaceDetectionModel

# Initialize the face detection model with the pre-trained database
fc_model = FaceDetectionModel('face_db.p')

def on_command_callback(command, data):
    """
    Callback function to handle incoming WebSocket commands.
    
    Args:
        command (str): The command received from the client
        data: The data associated with the command
    
    Currently handles face enrollment by storing new face data with the identifier "amirreza"
    """
    fc_model.enroll_new_face(data, "amirreza")

if __name__ == "__main__":
    # Initialize and start the WebSocket server with the command callback
    ws_server = WebSocketServer(on_command_callback=on_command_callback)
    ws_server.start_server()