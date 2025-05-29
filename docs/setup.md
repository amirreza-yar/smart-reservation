# Setup Guide

## System Requirements

- Python 3.8 or higher
- OpenCV 4.10.0 or higher
- dlib 19.24.6 or higher
- WebSocket libraries
- Django (for web integration)

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/amirreza-yar/smart-reservation.git
   cd smart-reservation/backend
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   Create a `.env` file in the root directory:
   ```
   FACE_DB_PATH=path/to/face_db.p
   WEBSOCKET_PORT=8765
   DEBUG=True
   ```

5. **Initialize Face Database**
   ```bash
   python test.py
   ```

## Configuration

### Face Detection Settings

The face detection system can be configured in `__face_detector/config.py`:

```python
FACE_DETECTION_CONFIDENCE = 0.6
FACE_RECOGNITION_TOLERANCE = 0.6
MAX_FACE_DISTANCE = 0.6
```

### WebSocket Settings

WebSocket server settings can be configured in `__websocket_server/config.py`:

```python
HOST = "localhost"
PORT = 8765
MAX_CONNECTIONS = 100
```

## Testing

Run the test suite:
```bash
pytest
```

## Troubleshooting

### Common Issues

1. **dlib Installation Fails**
   - Ensure you have CMake installed
   - Install Visual Studio Build Tools (Windows)
   - Install build-essential (Linux)

2. **OpenCV Issues**
   - Ensure you have the correct version installed
   - Check system dependencies

3. **WebSocket Connection Issues**
   - Check firewall settings
   - Verify port availability
   - Check network configuration

## Support

For additional support:
- Open an issue on [GitHub](https://github.com/amirreza-yar/smart-reservation/issues)
- Contact via [Email](mailto:yar.amirreza@gmail.com)
- Reach out on [Telegram](https://t.me/Amirrz_yar)
- Connect on [LinkedIn](https://www.linkedin.com/in/amirreza-yarahmadi/) 