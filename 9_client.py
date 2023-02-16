import socket
import RPi.GPIO as GPIO
import time

Buzzer=36
HOST='192.168.14.51'
PORT=4005

GPIO.setmode(GPIO.BOARD)
#GPIO.setWarings(False)
GPIO.setup(Buzzer,GPIO.OUT)

try:
	 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
		 s.connect((HOST, PORT))
		 while True:
			 data=s.recv(1024).decode('utf-8')
			 print(data)
			 if(str(data)=='Alert'):
				 print("Alert!Gas leakage detected")
				 GPIO.output(Buzzer,True)
				 time.sleep(3)
				 GPIO.output(Buzzer,False)
			 time.sleep(3)
except KeyboardInterrupt:
	s.close()
	GPIO.cleanup()			   
