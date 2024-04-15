import cv2
import time
import serial


def bitch():
    print("bitchass")


def face():

    face_cascade = cv2.CascadeClassifier("assets/haarcascade_frontalface_default.xml")
    cap = cv2.VideoCapture(1)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    # ArduinoSerial = serial.Serial("/dev/cu.usbserial-10", 9600, timeout=0.5)
    out = cv2.VideoWriter("assets/face detection4.avi", fourcc, 20.0, (600, 600))
    time.sleep(1)

    while cap.isOpened():
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 6)

        for x, y, w, h in faces:
            string = "X{0:d}Y{1:d}".format((x + w // 2), (y + h // 2))
            print(string)
            # ArduinoSerial.write(string.encode("utf-8"))
            cv2.circle(frame, (x + w // 2, y + h // 2), 2, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        out.write(frame)
        cv2.imshow("img", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    face()
