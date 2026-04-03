# Weapon Detection System

A Python-based weapon detection application with a client-side PyQt GUI. The project uses OpenCV for camera capture and PyQt5 for the login, settings, and live detection interfaces.

## Features

- PyQt5 desktop GUI with multiple windows:
  - Login screen
  - Settings screen
  - Live detection window
- Live webcam capture with OpenCV
- QThread-based video feed updates for smooth UI performance
- Modular design with separate UI and logic components

## Technology Stack

- Python 3.x
- PyQt5
- OpenCV (`opencv-python-headless`)
- NumPy
- Requests

## Project Structure

- `Client Side/`
  - `main.py` - Application entry point
  - `login_window.py` - Login window implementation
  - `settings_window.py` - Settings screen and detection control
  - `detection_window.py` - Live detection GUI window
  - `detection.py` - Background video capture thread
  - `UI/` - Qt Designer `.ui` files for the application windows
- `client_side/` - Existing Pipenv environment configuration
  - `Pipfile`
  - `Pipfile.lock`
- `venv/` - Local virtual environment created for this project
- `.gitignore` - Git ignore rules for Python projects

## Prerequisites

- Python 3.8 or newer
- `python3` and `pip` installed
- macOS or Linux recommended for desktop GUI support

## Setup

1. Open a terminal at the project root:
   ```bash
   cd "/Volumes/Nimal Singh/Weapon-Detection-System"
   ```
2. Activate the local virtual environment:
   ```bash
   source venv/bin/activate
   ```
3. Install required packages in the active environment:
   ```bash
   pip install requests numpy opencv-python-headless pyqt5
   ```

## Running the Application

With the virtual environment activated, run:

```bash
cd "Client Side"
python3 main.py
```

## Notes

- The application currently uses a basic login screen and transitions to the settings window.
- The detection window captures webcam frames and displays them using a QThread to keep the UI responsive.
- If `PyQt5` is not found, ensure the virtual environment is active and the package is installed inside it.

## Git Ignore

The repository includes a `.gitignore` file to exclude virtual environments, compiled files, OS artifacts, and other temporary project files.
