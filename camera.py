from picamera import PiCamera
from time import sleep
from picamera import Color 
import datetime as dt

camera = PiCamera()
#camera.rotation = 180

camera.resolution = (2560, 1920)  # 0.3MP
# 22 Total Image Effects
imageEffectlist = ['none','watercolor','sketch', 
            'cartoon', 'negative', 'emboss', 
            'oilpaint', 'solarize', 'colorpoint'] # 9 Image Effects
#camera.stop_preview()
camera.start_preview()
for effect in imageEffectlist:
    camera.image_effect = effect
    camera.annotate_background = Color('black')
    camera.annotate_text_size = 75
    datetimestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.annotate_text = datetimestamp + '\n' + "Effect: %s" % effect
    camera.capture('/home/pi/picamera/output/' + datetimestamp + " " + effect +'.jpg')

    sleep(2)
camera.stop_preview()


