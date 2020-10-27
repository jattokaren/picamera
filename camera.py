from picamera import PiCamera   # Importing the library for camera module
from time import sleep          # Importing sleep from time library to add delay in program
from picamera import Color      # Importing for text annotation color background
import datetime as dt           # Importing for a date timestamp for filename

camera = PiCamera()
#camera.rotation = 180

camera.start_preview()
sleep(5)                        #Warm up camera and exposure for video recording
datetimestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# Record Video Python Code
camera.start_recording('/home/pi/picamera/output/video ' + datetimestamp + '.h264') 
sleep(10)                       #Duration 11 seconds @ 2.1MP  1920 × 1080 21.1 MB
camera.stop_recording()  

camera.resolution = (2560, 1920)  # 0.3MP
# 22 Total Image Effects
imageEffectlist = ['none','watercolor','sketch', 
            'cartoon', 'negative', 'emboss', 
            'oilpaint', 'solarize', 'colorpoint'] # 9 Image Effects
          
for effect in imageEffectlist:
    camera.image_effect = effect
    camera.annotate_background = Color('black')
    camera.annotate_text_size = 75
    datetimestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text = datetimestamp + '\n' + "Effect: %s" % effect
    camera.capture('/home/pi/picamera/output/' + datetimestamp + " " + effect +'.jpg')

    sleep(2)

camera.stop_preview()
