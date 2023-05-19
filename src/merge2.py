import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C
import cv2
import pyzbar.pyzbar as pyzbar
import serial
send = 'S'  # 发送给arduino的数据
Port = "/dev/ttyACM0"  # 串口
baudRate = 9600 # 波特率
ser = serial.Serial(Port, baudRate, timeout=1)

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
    #这个index有大用，留着给机械臂传参数
    carShelf[index] = "/"
    
    size = size - 1
    print("book {} is removed from {}".format(bookCode, index))
    print(carShelf)
    
    if size == 0:
        print("All books returned !")
        print("Please add new books!")
        
        



def decodeDisplay(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        # 提取条形码的边界框的位置
        # 画出图像中条形码的边界框
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
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
    global carShelf
    global size
    if barcodeData in carShelf:
        # 底盘停车
        carStop()

        # 机械臂放书
        returnBook()

        # 删除数据
        rmvBook(barcodeData)
        
    else:
        print("QR code doesn't match")

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

if __name__ == "__main__":
    # 创建大小为 5 的列表来存储 bookCode
    carShelf = ["/","/","/","/","/"]
    size = 0    

    i2c = busio.I2C(board.SCL, board.SDA) # 创建 I2C 对象
    pn532 = PN532_I2C(i2c, debug=False)   # 使用 I2C 接口连接 PN532
    ic, ver, rev, support = pn532.get_firmware_version() # 初始化 PN532
    print(f"Found PN532 with firmware version: {ver}.{rev}")

    pn532.SAM_configuration() # 配置 PN532 以便在 Mifare 卡片上读取数据
    print("Waiting for RFID/NFC card...")
    
    try:
        while(1):
            
           
            while (size!= 5):
                # 尝试读取 ID 卡信息
                uid = pn532.read_passive_target(timeout=0.5)

                # 如果找到卡片，将 UID 转换为字符串 bookCode
                if uid is not None:
                    bookCode = ''.join([hex(i)[2:] for i in uid])

                    # 检查是否重复读取到相同的 bookCode
                    if bookCode in carShelf:
                        print("Book already on the car shelf!")
                    else:
                        putBook(bookCode)
                        print("Current car shelf:", carShelf)
                time.sleep(0.2)
            pn532.SAM_configuration()
            camera = cv2.VideoCapture(0)
            while(size!= 0):
                    # 等待一段时间再进行下一次读取，避免频繁读取导致程序无响应
                # 读取当前帧
                    ret, frame = camera.read()
                    # 转为灰度图像
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    im=decodeDisplay(gray)
                    
                    cv2.waitKey(5)
                    cv2.imshow("camera", im)
            camera.release()
            cv2.destroyAllWindows()
    except KeyboardInterrupt:
        print("Program stopped by user")
