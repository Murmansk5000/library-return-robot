import time
import board
import busio
from digitalio import DigitalInOut
from adafruit_pn532.i2c import PN532_I2C

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
        while (size<5):
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
                
            # 等待一段时间再进行下一次读取，避免频繁读取导致程序无响应
            time.sleep(0.2)
            if(size == 5):
                    file_handle = open('barcode.txt',mode = 'w')
                    file_handle.writelines([carShelf[0],'\n',carShelf[1],'\n',carShelf[2],'\n',carShelf[3],'\n',carShelf[4]])
                    file_handle.close()
    
    except KeyboardInterrupt:
        print("Program stopped by user")
