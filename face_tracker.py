import cv2
import numpy as np
import serial


# Function to detect faces using OpenCV's built-in face cascade classifier
def detect_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    return faces


cap = cv2.VideoCapture(1)
ws, hs = 1000, 1000
cap.set(cv2.CAP_PROP_FRAME_WIDTH, ws)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

set = serial.Serial("/dev/cu.usbserial-140", 9600, timeout=0.5)
servoPos = [90, 90]

while True:
    success, img = cap.read()
    faces = detect_faces(img)

    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        fx, fy = x + w // 2, y + h // 2
        pos = [fx, fy]
        servoX = np.interp(fx, [0, ws], [0, 180])
        servoY = np.interp(fy, [0, hs], [0, 180])
        servoX = np.clip(servoX, 0, 180)
        servoY = np.clip(servoY, 0, 180)
        servoPos[0] = servoX
        servoPos[1] = servoY
        cv2.line(img, (0, fy), (img.shape[1], fy), (0, 0, 0), 2)  # x line
        cv2.line(img, (fx, 0), (fx, img.shape[0]), (0, 0, 0), 2)  # y line
    else:
        cv2.putText(
            img, "NO TARGET", (100, 400), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3
        )
    cv2.putText(
        img,
        f"Servo X: {int(servoPos[0])} deg",
        (50, 50),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 0, 0),
        2,
    )
    cv2.putText(
        img,
        f"Servo Y: {int(servoPos[1])} deg",
        (50, 100),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 0, 0),
        2,
    )

    set.write(f"X{servoPos[0]}Y{servoPos[1]}\n".encode())
    cv2.imshow("Image", img)
    cv2.waitKey(1)
