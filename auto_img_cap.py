#captures one image per hour
import time
import picamera
import RPi.GPIO as GPIO

switch = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(switch, GPIO.OUT, initial = GPIO.LOW)


NO_OF_DAYS = 1

FRAMES_PER_HOUR = 10

FRAMES = FRAMES_PER_HOUR * 24 * NO_OF_DAYS

def capture_frame(frame):

    with picamera.PiCamera() as cam:
        GPIO.output(switch, GPIO.HIGH)
        time.sleep(2)

        cam.capture('/home/pi/Desktop/pictures/frame%03d.jpg' % frame)
        time.sleep(2)
        GPIO.output(switch, GPIO.LOW)
 

for frame in range(FRAMES):

    start = time.time()

    capture_frame(frame)

    time.sleep(int(60* 60 / FRAMES_PER_HOUR) - (time.time() - start)

)