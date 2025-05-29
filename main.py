from __websocket_server.api import WebSocketServer
from __face_detector.api import FaceDetectionModel

fc_model = FaceDetectionModel('face_db.p')

def on_command_callback(command, data):
    fc_model.enroll_new_face(data, "amirreza")

if __name__ == "__main__":

    ws_server = WebSocketServer(on_command_callback=on_command_callback)
    ws_server.start_server()