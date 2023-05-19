#  coding:utf8
 
import cv2
import pyzbar.pyzbar as pyzbar

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

# raspbarry Pi 通信
def returnBook():
    print("Robot arm puts book from car shelf")
    
    
def cmpQR(barcodeData):
    global carShelf
    if barcodeData in carShelf:
        # 底盘停车
        carStop()

        # 机械臂放书
        returnBook()

        # 删除数据
        rmvBook(barcodeData)
	size = size -1
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
 
        cv2.waitKey(5)
        cv2.imshow("camera", im)
 
    camera.release()
    cv2.destroyAllWindows()
 


if __name__ == "__main__":
    books = [167432, 104588, 193805, 183079, 185725, 134863, 120876, 130956, 176397, 109673]
    carShelf = ["167432","104588","193805","183079","185725"]
    size = 5
    detect()









