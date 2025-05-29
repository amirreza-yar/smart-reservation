import json
import websockets
import asyncio

from .utils import img_buf_to_array
from .logger import log

class WebSocketServer:
    def __init__(self, server_ip="0.0.0.0", server_port=8000, on_command_callback=None):
        self.server_ip = server_ip
        self.server_port = server_port

        self.on_command_callback = on_command_callback

    def start_server(self):
        start_server = websockets.serve(self.handler, "0.0.0.0", 8000)
        log("Starting websocket server...", "INFO", "WEBSOCKET SERVER", "start_server")
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def handler(self, websocket, path):
        log("Connection established", "INFO", "WEBSOCKET SERVER", "handler")

        try:
            while True:
                # Receive data (could be JSON text or binary)
                data = await websocket.recv()

                if isinstance(data, bytes):  # If binary, treat it as image data
                    log(f"Received unexpected {len(data)} bytes of binary data without command", "ERROR", "WEBSOCKET SERVER")
                    continue
                else:  # If text, treat it as a command or request
                    try:
                        message = json.loads(data)
                        command = message.get("command")

                        if command == "ENROLL_FACE" or command == "DETECT_FACE":
                            frames = message.get("frames", 1)
                            log(f"Processing ENROLL_FACE command, expecting {frames} frames...", "INFO", "WEBSOCKET SERVER", command)

                            # Receive frames and handle possible network errors
                            all_frames = await self.receive_image_frames(websocket, frames)
                            if all_frames:
                                log(f"All frames recieved", "INFO", "WEBSOCKET SERVER", command)
                                await websocket.send(f"All frames received successfully, start {'enrolling' if command == 'ENROLL_FACE' else 'detecting'}...")
                            else:
                                log(f"Problem in getting frames", "ERROR", "WEBSOCKET SERVER", "ENROLL_FACE")
                                await websocket.send("Error: Not all frames were received, try again")

                            # Notify the main thread through the callback
                            if self.on_command_callback:
                                log(f"Sending frames to callback", "INFO", "WEBSOCKET SERVER", "ENROLL_FACE")
                                self.on_command_callback(command, all_frames)

                        elif command == "REQUEST_STATUS":
                            log("Processing status request", "INFO", "WEBSOCKET SERVER", command)
                            await websocket.send("Status: OK")
                        
                        elif command == "SHUTDOWN":
                            log("Shutting down server...", "WARNING", "WEBSOCKET SERVER", command)
                            await websocket.send("Server shutting down")
                            break

                        # Add more command handlers as needed
                        
                    except json.JSONDecodeError:
                        log(f"Received non-JSON text data: {data}", "WARNING", "WEBSOCKET SERVER", "handler")
        except websockets.exceptions.ConnectionClosed:
            log("Connection closed", "WARNING", "WEBSOCKET SERVER", "handler")

    async def receive_image_frames(self, websocket, frames):
        received_frames = 0
        data_frames = []
        while received_frames < frames:
            try:
                data = await websocket.recv()
                if isinstance(data, bytes):
                    data_frames.append(img_buf_to_array(data))
                    received_frames += 1
                    log(f"Frame {received_frames}/{frames} received", "INFO", "WEBSOCKET SERVER", "receive_image_frames")
                else:
                    log("Unexpected non-binary data received", "WARNING", "WEBSOCKET SERVER", "receive_image_frames")
            except websockets.exceptions.ConnectionClosed:
                log("Connection closed before all frames were received", "WARNING", "WEBSOCKET SERVER", "receive_image_frames")
                break
        return data_frames