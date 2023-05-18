int Trig = A2;
int Echo = A3;
float distance;
//获取超声波往返时间函数，发送到接收
int times() {
  int time1;
  int time2;
  while (digitalRead(Echo) == LOW);//等待高电平信号，
  time1 = micros();//高电平信号触发，记录当前时间
  while (digitalRead(Echo) == HIGH);//等待底电平信号
  time2 = micros();//低电平信号触发，记录当前时间
  Serial.println("函数调用");
  return (time2 - time1);//返回时间差即引脚高电平所持续的时间
}
void setup() {
  Serial.begin(115200);
  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);
}
void loop() {
  //发送一个10us的脉冲
  digitalWrite(Trig, LOW);
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(Trig, LOW);
  //获取时间
  //program_one
  int Time1 = times();
  //program_two
  int Time2 = pulseIn(Echo, HIGH); //获取超声波返回时长，单位us = 10^-6s
  //计算距离
  distance =  Time1 / 58; //单位厘米 distance = Time1*340*100/1000000/2;
  Serial.print(distance);
  Serial.println("cm");
  delay(1000);
}
