from picamera import PiCamera
from time import sleep
from picamera import Color 
import datetime as dt

camera = PiCamera()
#camera.rotation = 180
count = 701
camera.resolution = (1280, 960)  # 0.3MP
imagelist = ['none','watercolor','sketch', 
            'cartoon', 'negative', 'emboss', 
            'oilpaint', 'solarize', 'colorpoint']
camera.stop_preview()
camera.start_preview()
for effect in imagelist:
    camera.image_effect = effect
    camera.annotate_background = Color('black')
    camera.annotate_text_size = 75
    datetimestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text = datetimestamp + '\n' + "Effect: %s" % effect
    camera.capture('/home/pi/Desktop/Camera/' + str(count) +" " + effect +'.jpg')
    count = count + 1
    sleep(2)
camera.stop_preview()

#for effect in camera.IMAGE_EFFECTS:
#camera.start_preview()
#camera.image_effect = 'negative'
#sleep(5)
#camera.capture('/home/pi/Desktop/negative.jpg')
#camera.stop_preview()
