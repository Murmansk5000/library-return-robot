import serial

Port = "/dev/ttyACM0"  # 串口
baudRate = 115200  # 波特率
ser = serial.Serial(Port, baudRate, timeout=1)


    
send = 'S'  # 发送给arduino的数据
ser.write(send.encode())
         

ser.close()
