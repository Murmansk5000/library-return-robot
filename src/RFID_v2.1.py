import sys
import time
import subprocess

xe = subprocess.run("nfc-list", stdout=subprocess.PIPE)

raw = xe.stdout.decode("gbk")
lines = raw.split("\n")
goodLine = lines[5]
bookCode = goodLine[21:40].replace(" ","")

print(bookCode)
#print(xe.stdout.decode("gbk"))
#print(xe.returncode)
