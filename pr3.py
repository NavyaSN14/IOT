import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

led1=15


gpio.setup(led1,gpio.OUT,initial=0)

fp=open("sample.txt")
for line in fp:
	print(line)
	ontime=line
	gpio.output(led1,True)
	
time.sleep(2)
gpio.output(led1,False)

try:
	while(True):
		time.sleep(3)
except KeyboardInterrupt:
	gpio.cleanup()

