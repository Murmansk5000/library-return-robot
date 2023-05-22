#include<Servo.h>
Servo myservo;



void setup() {
myservo.attach(A0);
  
Serial.begin(9600);
}



void loop() {
  // put your main code here, to run repeatedly:


myservo.write(0);
delay(1000);
delay(1000);

}
