import RPi.GPIO as GPIO
import os

color = os.environ['COLOR']

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.IN,GPIO.PUD_UP)

ledPin1 = 20  #define led pin1
ledPin2 = 21  #define led pin2
GPIO.setup(ledPin1,GPIO.OUT)
GPIO.setup(ledPin2,GPIO.OUT)
GPIO.output(ledPin1,GPIO.LOW)
GPIO.output(ledPin2,GPIO.LOW)

if color == "RED":
   GPIO.output(ledPin1,GPIO.HIGH)  #turn on led1
   GPIO.output(ledPin2,GPIO.LOW)  #turn off led2
#GREEN LED
else:
   GPIO.output(ledPin2,GPIO.HIGH)  #turn on led2
   GPIO.output(ledPin1,GPIO.LOW)  #turn off led1


except KeyboardInterrupt:
    GPIO.cleanup()
