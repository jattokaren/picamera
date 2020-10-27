from PIL import Image
from PIL.ExifTags import TAGS

ImageFileName = "/home/pi/picamera/output/2020-10-09 10:41:08 sketch.jpg"

image = Image.open(ImageFileName)

dataExifDictionary = image._getexif()

print(dataExifDictionary)

#An example Dictionary of Image EXIF data
exampleDictionary = {256: 1280, 257: 960, 37378: (20000, 10000), 
	36867: '2020:10:01 14:55:00', 36868: '2020:10:01 14:55:00', 
	37381: (20000, 10000), 36864: b'0220', 37121: b'\x01\x02\x03\x00', 
	37385: 0, 37386: (30390, 10000), 40962: 1280, 
	271: 'RaspberryPi', 272: 'RP_imx219', 
	531: 1, 282: (72, 1), 283: (72, 1), 33434: (10785, 1000000), 
	40965: 906, 34850: 3, 40961: 1, 34855: 50, 296: 2, 41987: 0, 
	37383: 2, 33437: (20000, 10000), 306: '2020:10:01 14:55:00', 
	37377: (6534830, 1000000), 40960: b'0100', 40963: 960, 
	41986: 0, 34665: 192, 37379: (272, 100), 
	37500: b'ev=-1 mlux=-1 exp=10785 ag=256 focus=255 gain_r=1.347 gain_b=2.316 greenness=0 ccm=6096,-1964,-30,-1274,5632,-258,264,-3794,7632,0,0,0 md=0 tg=272 272 oth=0 0 b=0 f=272 272 fi=0 ISP Build Date: Aug 15 2019, 12:08:19 VC_BUILD_ID_VERSION: 0e6daa5106dd4164474616408e0dc24f997ffcf3 (clean) VC_BUILD_ID_USER: dom VC_BUILD_ID_BRANCH: master '
	}

#Exif keys of interest
myKeysOfInterest = [272,36867,40962,40963,37386,34855,33434,33437]

#Iterates thru the Dictionary and only gives my keys of interest
myExifDictionary = { each_key: dataExifDictionary[each_key] for each_key in myKeysOfInterest }

#Prints both Keys & Values in my Dictionary
print(myExifDictionary)

#Prints only Dictionary Keys
print(myExifDictionary.keys())

#Prints only Dictionary Values
print(myExifDictionary.values())
