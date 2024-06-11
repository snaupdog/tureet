# Face Tracking and Locking System with Servo Control
This project implements a face tracking and locking system using OpenCV for face detection and an Arduino for controlling servo motors. The system consists of three main components: Arduino code for servo control, a Python script for face tracking, and a manual control interface using Tkinter.

## Components and Their Functions
1. Arduino Code (Servo Control)
The Arduino code manages two servos (servoX and servoY) that adjust their positions based on received commands. It listens for commands via the serial port and updates the servo positions accordingly.

2. Python Script (Face Tracking)
The Python script uses OpenCV to capture video from the webcam, detect faces, and calculate the position of the detected face. It then maps these positions to servo angles and sends the commands to the Arduino via serial communication.

3. Manual Control Interface (Tkinter)
This Python script provides a graphical user interface (GUI) using Tkinter, allowing manual control of the servo positions with mouse movements. It maps the mouse coordinates to servo angles and sends the commands to the Arduino via serial communication.

## System Workflow
### Face Tracking
  - The camera captures video frames.
  - The Python script detects faces in the frames and calculates the position of the face.
  - It maps the face position to corresponding servo angles and sends the commands to the Arduino.

### Servo Control
  - The Arduino receives commands via serial communication.
  - It updates the servo positions to point towards the detected face.

## Manual Control
- The Tkinter GUI allows manual control of the servo positions using mouse movements.
- It maps mouse coordinates to servo angles and sends the commands to the Arduino.

## Installation and Usage

### Prerequisites
  - Arduino IDE
  - Python 3.x
  - OpenCV (cv2 module)
  - Tkinter (usually included with Python installations)
  - Numpy
  - Serial library (pyserial)

### Arduino Setup
  - Connect the servo motors to the Arduino (servoX to pin 10, servoY to pin 9).
  - Upload the Arduino code to the Arduino board.

### Python Setup
  - Install the necessary Python libraries:
    *pip install opencv-python numpy pyserial*
  - Ensure your webcam is properly connected.

### Running the Face Tracking Script
  - Run the face tracking Python script:
    *python facetracker.py*
  - The camera feed should open, and the servos will start tracking any detected faces.

### Running the Manual Control Interface
  - Run the manual control Python script:
    *python manual.py*
  - A Tkinter window will open, allowing you to control the servos with your mouse.

## Note
  - Ensure the correct serial port is specified in the Python scripts (e.g., /dev/cu.usbserial-140 or /dev/cu.usbserial-110).
  - Adjust the servo mapping ranges as needed to fit your specific setup and servo motor capabilities.
This project demonstrates a practical application of computer vision and robotics by integrating software and hardware to achieve a face tracking and locking system.

