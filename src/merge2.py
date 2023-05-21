#  coding:utf8
import time
from pymycobot import MyCobotSocket, Coord
import cv2
import pyzbar.pyzbar as pyzbar
import serial
send = 'S'  # 发送给arduino的数据
Port = "/dev/ttyACM0"  # 串口
baudRate = 9600 # 波特率
ser = serial.Serial(Port, baudRate, timeout=1)
def pick(location):
    # 初始位置
    mc.send_angles([-90, -80, -20, 0, 50, 0], 20)
    time.sleep(5)
    mc.set_gripper_state(0, 50)
    time.sleep(2)

    if location == 1:
        print("Picking book 1")
        # 第一个取书前位姿
        mc.send_angles([-5, 0, -70, -95.36, 62.49, 37], 55)
        time.sleep(4)
        # 第一个取书位姿
        mc.send_angles([-5, 0, -70, -68, 100, 33], 25)
        time.sleep(3)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([31.37, 9.4, -72, -119.7, 100, 35], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([34.8, 10.01, -71.8, -160, 48.86, 38.58], 40)
        time.sleep(3)
        mc.send_angles([34.54, -5, -71.8, -160, 9.31, 41.48], 40)
        time.sleep(2)
    elif location == 2:
        print("Picking book 2")
        # 第二个取书前位姿
        mc.send_angles([-118.3, -30, -22, 60.2, 32, -40], 20)
        time.sleep(5)
        # 第二个取书位姿
        mc.send_angles([-121.9, -33, -13.09, 36, 69.78, -23.64], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(3)
        # 夹书后撤
        mc.send_angles([-96.06, -58.97, -12.74, 8.96, 75.05, -3.07], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-96.06, -64.77, -12.74, 23.2, 12.65, -19.68], 40)
        time.sleep(4)
    elif location == 3:
        print("Picking book 3")
        # 第三个取书前位姿
        mc.send_angles([0, -43.59, -21.7, -103.88, 56.68, 26.36], 20)
        time.sleep(5)
        # # 第三个取书位姿
        mc.send_angles([0, -43.59, -21.7, -85.6, 99.4, 24.52], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-80, -50, -35, -15, 86.83, 0], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-80, -50, -35, -15, 10, 0], 40)
        time.sleep(4)
    elif location == 4:
        print("Picking book 4")
        # 第四个取书前位姿
        mc.send_angles([5, -57, -25, -88.85, 45, 0], 20)
        time.sleep(5)
        # # 第四个取书位姿
        mc.send_angles([5, -57, -25, -90, 88, 0], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-29.97, -60, -25, -59.5, 90, -0.17], 40)
        time.sleep(3)
        # 抬高
        mc.send_angles([-29.53, -50, -35, -61.43, 0, 0.7], 40)
        time.sleep(4)
    elif location == 5:
        print("Picking book 5")
        # 第五个取书前位姿
        mc.send_angles([0, -65, -63, -45, 59.76, -58.18], 40)
        time.sleep(5)
        # 第五个取书位姿
        mc.send_angles([0, -63.19, -45, -88.59, 88.68, -30], 20)
        time.sleep(4)
        # 夹书
        mc.set_gripper_value(60, 20)
        time.sleep(2)
        # 夹书后撤
        mc.send_angles([-23.46, -55, -65.91, -68, 99.58, -43], 20)
        time.sleep(4)
        # 抬高
        mc.send_angles([-22.85, -66.62, -60, -2.19, 49.65, -68.37], 40)
        time.sleep(4)
    else:
        print("Book location is wrong!")

    # 抬高后操作
    mc.send_angles([0, -20, -50, 0, -5, 0], 40)
    time.sleep(3)
    mc.send_angles([0, -55, -10, 0, 65, 0], 20)
    time.sleep(4)
    mc.send_angles([0, 45, -20, -1.31, -55, 0], 40)
    time.sleep(4)
    mc.set_gripper_state(0, 50)
    time.sleep(2)
    mc.send_angles([0, -80, -20, 0, 50, 0], 40)
    time.sleep(3)



def putBook(bookCode):
	global size # 告诉python用的是同一个size
	i=0	
	while i<5:
		if carShelf[i] == "/":
			carShelf[i] = bookCode
			size = size + 1
			print("book {} is put in {}".format(bookCode, i))
			return
		else:
			i=i+1
	
	# 如果五个位置都放了书（字典没有"_"位置）
	print("Stop it and the damn car shelf is already full.") 
	

def rmvBook(bookCode):
    global size # 告诉python用的是同一个size	
    index = carShelf.index(bookCode)

    carShelf[index] = "/"
    pick(index+1)
    size = size - 1
    print("book {} is removed from {}".format(bookCode, index))
    print(carShelf)
    
    if size == 0:
        print("All books returned !")
        camera.release()
        cv2.destroyAllWindows()

		
		
def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        # 条形码数据为字节对象，所以如果我们想在输出图像上
        # 画出来，就需要先将它转换成字符串
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
 
        # 绘出图像上条形码的数据和条形码类型
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    .5, (0, 0, 125), 2)
 
        # 向终端打印条形码数据和条形码类型
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
        
        cmpQR(barcodeData)
    return image
 
# arduino 通信
def carStop():
    print("car stop")
    ser.write(send.encode())
# raspbarry Pi 通信
def returnBook():
    print("Robot arm puts book from car shelf")
   
    
    
def cmpQR(barcodeData):
    global size
    global carShelf
    print(barcodeData)
    if barcodeData in carShelf:
        # 底盘停车
        carStop()

        # 机械臂放书
        returnBook()

        # 删除数据
        rmvBook(barcodeData)
        
    else:
        print("QR code doesn't match")
    
    
    
    
def detect():
 
    camera = cv2.VideoCapture(0)
 
    while True:
        # 读取当前帧
        ret, frame = camera.read()
        # 转为灰度图像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        im=decodeDisplay(gray)
 
        #cv2.waitKey(5)
        #cv2.imshow("camera", im)
 
    camera.release()
    cv2.destroyAllWindows()
 


if __name__ == "__main__":
    size = 5
    mc = MyCobotSocket("10.142.223.177", 9000)

    # 树莓派版本需要输入connect函数，默认值为("/dev/ttyAMA0","1000000")
    mc.connect("/dev/ttyAMA0", "1000000")
    print("Arm has been connected!")
    carShelf = []
    f = open('list.txt')
    for line in f:
         carShelf.append(line.strip())
    print(carShelf)
    f.close()

detect()









