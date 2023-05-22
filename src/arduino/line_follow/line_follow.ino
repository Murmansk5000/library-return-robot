
#include <Wire.h>
#include "gw_grayscale_sensor.h"

#define GW_GRAY_GPIO_CLK A5
#define GW_GRAY_GPIO_DAT A4

/* 读取8 bit的传感器数据 */
static uint8_t gw_gray_serial_read(){
  uint8_t ret = 0;
  for (int i = 0; i < 8; ++i) {
    ret <<= 1;
    digitalWrite(GW_GRAY_GPIO_CLK, 0);
    ret |= digitalRead(GW_GRAY_GPIO_DAT);
    digitalWrite(GW_GRAY_GPIO_CLK, 1);
  }
  return ret;
}


int single[8] = {0, 0, 0, 0, 0, 0, 0, 0};
int sub[4] = {0, 0, 0, 0};
//int weight[4] = {10, 5, 2, 1};
int weight[4] = {120, 110, 100, 90};
int sum = 0;
int comp = 0;
char inf = '0';

int lf1 = 2;
int lf2 = 4;
int LeftF = 3;

int lb1 = 5;
int lb2 = 7;
int LeftB = 6;

int rf1 = 8;
int rf2 = 10;
int RightF = 9;


int rb1 = 12;
int rb2 = 13;
int RightB = 11;

int Trig = A2;
int Echo = A3;
float distance = 80;

int avg = 80;
int velocity = 0;
int offect = 0;
int half = 0;

int times() {
  int time1;
  int time2;
  while (digitalRead(Echo) == LOW);//等待高电平信号，
  time1 = micros();//高电平信号触发，记录当前时间
  while (digitalRead(Echo) == HIGH);//等待底电平信号
  time2 = micros();//低电平信号触发，记录当前时间
  //Serial.println("函数调用");
  return (time2 - time1);//返回时间差即引脚高电平所持续的时间
}

void setup() {
  pinMode(lf1, OUTPUT);
  pinMode(lf2, OUTPUT);
  pinMode(LeftF, OUTPUT);

  pinMode(rf1, OUTPUT);
  pinMode(rf2, OUTPUT);
  pinMode(RightF, OUTPUT);

  pinMode(lb1, OUTPUT);
  pinMode(lb2, OUTPUT);
  pinMode(LeftB, OUTPUT);

  pinMode(rb1, OUTPUT);
  pinMode(rb2, OUTPUT);
  pinMode(RightB, OUTPUT);

  pinMode(Trig, OUTPUT);
  pinMode(Echo, INPUT);

  pinMode(GW_GRAY_GPIO_CLK, OUTPUT);
  pinMode(GW_GRAY_GPIO_DAT, INPUT_PULLUP);

  digitalWrite(GW_GRAY_GPIO_CLK, 0);


  // 初始化串口
  Serial.begin(9600);
}



void loop() {
  uint8_t sensor_status = 0;
  uint8_t sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8;
  // 循环 直到PING成功  // 读取传感器串行输出
  sensor_status = gw_gray_serial_read();

    // 把读取到的传感器数据打印到公屏上

  digitalWrite(Trig, LOW);
  delayMicroseconds(0.1);
  digitalWrite(Trig, HIGH);
  delayMicroseconds(0.1);
  digitalWrite(Trig, LOW);
  int Time1 = times();
  //int Time2 = pulseIn(Echo, HIGH); //获取超声波返回时长，单位us = 10^-6s
  distance =  Time1 / 58; //单位厘米 distance = Time1*340*100/1000000/2;

  SEP_ALL_BIT8(sensor_status, sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8);

    //Serial.print("传感器数字数据:");
    for (int i = 1; i <= 8; ++i) {  //探头从1开始,不是0
      single[8-i] = (GET_NTH_BIT(sensor_status, i));
      //Serial.print(" ");
      //Serial.print(GET_NTH_BIT(recv_value, i));
      //Serial.print(single[i-1]);
    }
    //Serial.print("\n");

    sum = 0;
    for (int i = 0; i < 4; i++) {
      sub[i] = single[i] - single[7 - i];
      sum += sub[i] * weight[i];
    }

    comp = 0;

    if (0 - comp <= sum && sum <= comp) {
      inf = 'F';
    } else if (sum > comp) {
      inf = 'l';
    } else if (sum < 0 - comp) {
      inf = 'r';
    }

    if (sub[0] > 0 
    || sub[1] > 0
    )
      inf = 'L';
    if (sub[0] < 0 
    || sub[1] < 0
    )
      inf = 'R';
    //Serial.print(distance);

    if (distance < 40) inf = 'S';
    if (Serial.read() == 'S')
    {
     inf = 'S';
     run(inf,0);
     delay(42000);
    }
    sum = abs(sum);

    run(inf, sum);

}

void run(char incomedate, int offect) {
  velocity = avg + offect;
  if (velocity > 255) velocity = 255;
  if (velocity < 0)velocity = 0;
  Serial.print(incomedate);
  Serial.print(velocity);
  Serial.print("\n");
  if (incomedate == 'F') {
    //Forward
    digitalWrite(lf1, HIGH);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(rf1, HIGH);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(lb1, HIGH);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rb1, HIGH);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
    delay(1);

  } else if (incomedate == 'S') {
    //Stop
    digitalWrite(lf1, LOW);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(rf1, LOW);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(lb1, LOW);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rb1, LOW);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
    delay(1000);

  }
  else if (incomedate == 'B') {
    //Back

    digitalWrite(lf1, LOW);
    digitalWrite(lf2, HIGH);
    analogWrite(LeftF, velocity);

    digitalWrite(rf1, LOW);
    digitalWrite(rf2, HIGH);
    analogWrite(RightF, velocity);

    digitalWrite(lb1, LOW);
    digitalWrite(lb2, HIGH);
    analogWrite(LeftB, velocity);

    digitalWrite(rb1, LOW);
    digitalWrite(rb2, HIGH);
    analogWrite(RightB, velocity);
    delay(20);

  }

  if (incomedate == 'L') {
    if (velocity > 200) velocity = 200;
    //if (velocity < 100) velocity = 100;
    digitalWrite(lf1, LOW);
    digitalWrite(lf2, HIGH);
    analogWrite(LeftF, velocity);

    digitalWrite(lb1, LOW);
    digitalWrite(lb2, HIGH);
    analogWrite(LeftB, velocity);

    digitalWrite(rf1, HIGH);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(rb1, HIGH);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
    delay(20);



  } else if (incomedate == 'R') {
    if (velocity > 200) velocity = 200;
    //if (velocity < 100) velocity = 100;
    digitalWrite(lf1, HIGH);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(lb1, HIGH);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rf1, LOW);
    digitalWrite(rf2, HIGH);
    analogWrite(RightF, velocity);

    digitalWrite(rb1, LOW);
    digitalWrite(rb2, HIGH);
    analogWrite(RightB, velocity);
    delay(20);

  }

  else if (incomedate == 'r') {
    //if (velocity > 200) velocity = 200;
    if (velocity < 150) velocity = 150;
    digitalWrite(lf1, HIGH);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(lb1, HIGH);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rf1, LOW);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(rb1, LOW);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
    delay(10);

  }
  else if (incomedate == 'l') {
    //if (velocity > 200) velocity = 200;
    if (velocity < 150) velocity = 150;
    digitalWrite(lf1, LOW);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(lb1, LOW);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rf1, HIGH);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(rb1, HIGH);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
    delay(10);


  } else if (incomedate == 'T') {
    digitalWrite(lf1, HIGH);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    digitalWrite(lb1, HIGH);
    digitalWrite(lb2, LOW);
    analogWrite(LeftB, velocity);

    digitalWrite(rf1, LOW);
    digitalWrite(rf2, LOW);
    analogWrite(RightF, velocity);

    digitalWrite(rb1, LOW);
    digitalWrite(rb2, LOW);
    analogWrite(RightB, velocity);
  }
}
