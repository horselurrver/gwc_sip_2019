#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(13);
  servoRight.attach(12);
  servoLeft.writeMicroseconds(1500); // establish shaft angle
  servoRight.writeMicroseconds(1500);
  // 2000 => clockwise, 1000 => counterclockwise
  // 1500 => standstill
}

void loop() {
  // put your main code here, to run repeatedly:

  // Move wheels forward, then stop
//  servoLeft.writeMicroseconds(1300);
//  servoRight.writeMicroseconds(1700);
//  delay(1000);
//
//  servoLeft.writeMicroseconds(1500);
//  servoRight.writeMicroseconds(1500);
//  delay(1000);
//
//  // Move wheels backward, then stop
//  servoLeft.writeMicroseconds(1700);
//  servoRight.writeMicroseconds(1300);
//  delay(1000);
//
//  servoLeft.writeMicroseconds(1500);
//  servoRight.writeMicroseconds(1500);
//  delay(1000);


  servoLeft.writeMicroseconds(1490);
  servoRight.writeMicroseconds(1490);
  delay(1000);
}
