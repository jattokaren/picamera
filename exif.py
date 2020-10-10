import os
import exif
from PIL import Image
from PIL.ExifTags import TAGS

rootdir = "/home/pi/picamera/output"
filelist = list()
pathfilelist = list()

def main():
	try:
		for subdir, dirs, files in os.walk(rootdir):
			for filename in files:
				if not filename.endswith('.py'):
					#filelist.append(filename)
					print(filename)
					filesize = os.path.getsize(subdir+'/'+filename)
					print(filesize)
					pathfilelist.append(os.path.join(subdir, filename))
					filepath =  os.path.join(subdir, filename)
					print(filepath)
					EXIF_data = exif_model(filepath)
					filelist.append({
					'Filename':filename, 
					'File Size':filesize,
					'Image DateTime': EXIF_data.get(36867),
					'Device Make':EXIF_data.get(271),
					'Device Model':EXIF_data.get(272),
					'Image Width':EXIF_data.get(40962),
					'Image Height':EXIF_data.get(40963),
					'Megapixels':round(EXIF_data.get(40962) * EXIF_data.get(40963) / 1000000,1),
					'Shutter Speed':EXIF_data.get(33434),
					'Focal Length (mm)':EXIF_data.get(37386),
					'Aperture (f/_)':EXIF_data.get(33437),
					'ISO':EXIF_data.get(34855)					
					})
					
						
	except IOError as ioe:
		print(ioe)
		
def exif_model(filepath):
	try:
		image = Image.open(filepath)
		EXIF_data = image._getexif()
		#print('Make = ' + EXIF_data.get(271))		#Make
		#print('Model = ' + EXIF_data.get(272))		#Model
		#print('Image DateTime = ' + EXIF_data.get(36867))		#Image Date Time Original
		#print('Image Width = ' + str(EXIF_data.get(40962)))		#Image Width
		#print('Image Height = ' + str(EXIF_data.get(40963)))		#Image Height
		#print(EXIF_data.get(33434))		#Exposure Time
		#print(EXIF_data.get(37386))		#Focal Length
		#print(EXIF_data.get(34855))		#ISO
		#print(EXIF_data.get(33437))		#Aperture
		image.close()
		
		return EXIF_data
	except IOError as ioe:
		raise
		
main()


print('*** Get file list length ***')
print(str(len(filelist)) + " = the # of files in list")
print("*** Here are the last 2 objects in file list ***")
print(filelist[:2])

print('*** Get path/file list length ***')
print(len(pathfilelist))
print("*** This is the 6th object in the path/file list ***")
print("pathfilelist[5]: " + pathfilelist[5])
