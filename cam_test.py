#11/07/2023

from picamera import PiCamera
import time
from time import sleep
import datetime
import os
import RPi.GPIO as GPIO

switch = 21

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(switch, GPIO.OUT, initial = GPIO.LOW)

#This code is for IR light control. Light is on while GPIO is high
camera = PiCamera()
#preview to see the IR light(for debug purpose, feel free to delete)





camera.start_preview()
GPIO.output(switch, GPIO.HIGH)
time.sleep(50)

GPIO.output(switch, GPIO.LOW)
camera.stop_preview()

    


#the below code is still buggy, fix it if you have time~~

picT = 600
uploadT = 60
temp = 1

# PJ Nov. 2 2023 commented the following code for testing camera feature

#while (1):
    #if temp == uploadT:
    #    print("uploading")
    #    os.system('rclone copy /home/pi/Desktop/pics "gdrive: WaggleNet"')
        
    #temp -= picT
    #if temp <= 0:
    #    temp = uploadT
    #    print("updating")
    
    #time.sleep(picT-7)
    #camera.start_preview()
    #time.sleep(5)
        
    #id = datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S")
    #filename = "/home/pi/Desktop/pics/"+id+".jpg"
    
    #GPIO.output(switch, GPIO.HIGH)
    #time.sleep(1)
    #camera.capture(filename)
    #time.sleep(1)
    #GPIO.output(switch, GPIO.LOW)
    #print("captured")
    #camera.stop_preview()


 
