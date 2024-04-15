#include <Servo.h>

Servo servoX;
Servo servoY;

void setup() {
  Serial.begin(9600);
  servoX.attach(10); // Attach servo X to pin 9
  servoY.attach(9); // Attach servo Y to pin 10
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    int posX = command.indexOf('X');
    int posY = command.indexOf('Y');
    if (posX >= 0 && posY >= 0) {
      int angleX = command.substring(posX + 1, posY).toInt();
      int angleY = command.substring(posY + 1).toInt();
      servoX.write(angleX);
      servoY.write(angleY);
    }
  }
}
