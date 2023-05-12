int incomedate = 0;

int lf1 = 2;
int lf2 = 4;
int LeftF = 3;

void setup() {
  pinMode(lf1, OUTPUT);
  pinMode(lf2, OUTPUT);
  pinMode(LeftF, OUTPUT);
  
  Serial.begin(9600); //设置串口波特率9600
}

void loop() {
  //arduino正常寻线
  Serial.println("Following line...")
  delay(1);
  
  while (Serial.available() > 0)//串口接收到数据
  {
    incomedate = Serial.read();//获取串口接收到的数据
    if (incomedate == '1')
    {
      //若接收到1则执行
      pinMode(13, OUTPUT);
      digitalWrite(13, HIGH); //亮灯    
      Serial.println("Car Stop for 5 sec"); //向树莓派发送信息
      delay(5000)
    }
    delay(5);
  }
}

void run(char incomedate, int offect) {
  velocity = 70;
  
  Serial.print(velocity);
  Serial.print("\n");
  if (incomedate == 'F') {
    //Forward
    digitalWrite(lf1, HIGH);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);

    //sRightB serial message back
    //Serial.println("ok");

  } else if (incomedate == 'S') {
    //Stop
    digitalWrite(lf1, LOW);
    digitalWrite(lf2, LOW);
    analogWrite(LeftF, velocity);
  }
}
