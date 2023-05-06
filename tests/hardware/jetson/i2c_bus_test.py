import board 
import digitalio
import busio
print("hello world")
pin = digitalio.DigitalInOut(board.D4)
print("D4 io ok")

i2c = busio.I2C(board.SCL,board.SDA)
print("I2C1 ok")
i2c = busio.I2C(board.SCL_0,board.SDA_0)
print("I2C2 ok")
print("done")