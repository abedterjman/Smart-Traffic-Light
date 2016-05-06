import RPi.GPIO as GPIO
import time


#right Triger =10
#right Echo =8

#middle trigger =18
#middle Echo =16


#left triger =40
#left Echo =38



GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Right Ultra
GPIO.setup(10,GPIO.OUT)
GPIO.setup(8,GPIO.IN)

#Middle Ultra
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

#Left Ultra
GPIO.setup(40,GPIO.OUT)
GPIO.setup(38,GPIO.IN)


GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(37,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.output(37,False)
GPIO.output(35,False)
GPIO.output(33,False)
GPIO.output(31,False)
GPIO.output(29,False)
GPIO.output(23,False)


def blink(pin):
   GPIO.output(pin,GPIO.HIGH)
   time.sleep(1)
   GPIO.output(pin,GPIO.LOW)
   time.sleep(1)

signalOff=0
    
while True: 
    
    
    

    #Right Ultra sonic
    GPIO.output(10,False)
    time.sleep(0.009)
    GPIO.output(10,True)
    time.sleep(0.009)
    GPIO.output(10,False)
    while GPIO.input(8)==0:
     signalOff=time.time()
    while GPIO.input(8)==1:
     signalOn=time.time()
    
    timePassed=signalOn-signalOff
    distance1=timePassed*17000
   
    print distance1," right cm"

    #Middle Ultra sonic
    GPIO.output(18,False)
    time.sleep(0.009)
    GPIO.output(18,True)
    time.sleep(0.009)
    GPIO.output(18,False)
    while GPIO.input(16)==0:
     signalOff=time.time()
    while GPIO.input(16)==1:
     signalOn=time.time()
    
    timePassed=signalOn-signalOff
    distance2=timePassed*17000
   
    print distance2," Middle cm"

   #Left Ultra sonic
    GPIO.output(40,False)
    time.sleep(0.009)
    GPIO.output(40,True)
    time.sleep(0.009)
    GPIO.output(40,False)
    while GPIO.input(38)==0:
        signalOff=time.time()
    while GPIO.input(38)==1:
        signalOn=time.time()

    timePassed=signalOn-signalOff
    distance3=timePassed*17000

    print distance3," Left cm"
    time.sleep(0.009) 
   
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.output(37,GPIO.LOW) 
    GPIO.output(33,GPIO.HIGH)
    GPIO.output(31,GPIO.HIGH) 
    GPIO.output(23,GPIO.LOW)
    if distance3 <10 and distance2>10 and distance1>10 :
       
         GPIO.output(33,GPIO.LOW)
         blink(35)
         GPIO.output(37,GPIO.HIGH) 
         GPIO.output(31,GPIO.LOW)
         GPIO.output(23,GPIO.HIGH)
         time.sleep(8) 
         GPIO.output(23,GPIO.LOW)
         blink(29)
         GPIO.output(31,GPIO.HIGH) 
         GPIO.output(37,GPIO.LOW)
         time.sleep(0.7)
         GPIO.output(33,GPIO.HIGH)
         time.sleep(8)
         print "highway warning "
    else :
        print"safe"
    
  

    if distance3 <10 and distance2<10  :
       
         GPIO.output(33,GPIO.LOW)
         blink(35)
         GPIO.output(37,GPIO.HIGH) 
         GPIO.output(31,GPIO.LOW)
         GPIO.output(23,GPIO.HIGH)
         time.sleep(8) 
         GPIO.output(23,GPIO.LOW)
         blink(29)
         GPIO.output(31,GPIO.HIGH) 
         
         GPIO.output(37,GPIO.LOW)
         time.sleep(0.7)
         GPIO.output(33,GPIO.HIGH)
         time.sleep(8)
         print "highway warning "
    else :
        print"safe"
    if distance3 <10 and distance1<10  :
       
         GPIO.output(33,GPIO.LOW)
         blink(35)
         GPIO.output(37,GPIO.HIGH) 
         GPIO.output(31,GPIO.LOW)
         GPIO.output(23,GPIO.HIGH)
         time.sleep(8) 
         GPIO.output(23,GPIO.LOW)
         blink(29)
         GPIO.output(31,GPIO.HIGH) 
         
         GPIO.output(37,GPIO.LOW)
         time.sleep(0.7)
         GPIO.output(33,GPIO.HIGH)
         time.sleep(8)
         print "highway warning "
    else :
        print"safe"
GPIO.cleanup()


