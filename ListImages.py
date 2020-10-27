import os
from datetime import datetime
from PIL import Image
import csv
import exif
import datetime as dt

rootdir = "/home/pi/picamera/output"  #Python/Photo Directory"    #My Photos"
filelist = list()
pathfilelist = list()
fileDetails_dict = dict()
imageDetails_dict = dict()
exifDetails_dict = dict()
processedDateTime = datetime.now()  #the Date and Time when script was run

def main():
    processStartTime = datetime.now()
    print(processStartTime)
    try:
        print("main method starting....")
        getFilepaths()
    except IOError as ioe:
        print("IO Error in Main method")
    finally:
        print("main() finally block executed")
        processEndTime = datetime.now()
        print(processStartTime)
        print(processEndTime)
        print(processEndTime - processStartTime)

def getFilepaths():
    try:
        print("For Loop going to all filepaths...")
        for subdir, dirs, files in os.walk(rootdir):
            for filename in files:
                if not (filename.endswith('.DS_Store') or filename.endswith('.picasa.ini')):
                    print(filename)                                   #see filename
                    filesize = os.path.getsize(subdir+'/'+filename)
                    print(filesize)                                   #see file save in bytes
                    pathfilelist.append(os.path.join(subdir, filename))
                    filepath = os.path.join(subdir, filename)
                    print(filepath)

                    fileDetails_dict.update({
                    'Filename':filename,
                    'File Size':filesize,
                    'File Path':filepath,
                    'Processed DateTime':str(processedDateTime)
                    })
                    print(fileDetails_dict)
                    getImageDetails(filepath)
                    fileDetails_dict.update(imageDetails_dict)
                    dict3 = fileDetails_dict.copy()
                    #filelist.append(dict3)

                    getExifDetails(filepath)
                    dict3.update(exifDetails_dict)
                    dict5 = dict3.copy()
                    filelist.append(dict5)

                    #A Flat file (.csv) of the complete file list dictionary
                    with open('filelistdict.csv', 'w', newline='') as myfile:
                        wr = csv.writer(myfile, lineterminator='\n',quoting=csv.QUOTE_ALL)
                        wr.writerow(filelist)
                    #List of Dictionaries to .csv file
                    #csv_columns = ['ID','Filename','Bytes','Create DateTime','Base64','Base64 Length']   #Needs to match Dictionary Keys
                    csv_columns = list(filelist[0].keys())     #Returns Dictionary Keys as a List
                    dict_data = filelist
                    csv_file = "FilelistDict2DataFrame.csv"
                    try:
                        with open(csv_file, 'w') as csvfile:
                            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                            writer.writeheader()
                            for data in dict_data:
                                writer.writerow(data)
                    except IOError:
                        print("I/O error")

    except IOError as ioe:
        print("IO Error when going to for loop")
        pass
    finally:
        print("getFilepaths() finally block")
        pass

def getImageDetails(filepath):
    imageDetails_dict.update({
        'Image Format': None,
        'Image Mode': None,
        'Image Size': None,
        'Image Width': None,
        'Image Height': None,
        'Megapixels': None
            })
    print("getImageDetails() None Dictionary Values\n", imageDetails_dict)
    try:
        image = Image.open(filepath)
        print(image.size)
        imageDetails_dict.update({
            'Image Format': image.format,
            'Image Mode': image.mode,
            'Image Size': image.size,
            'Image Width': image.size[0],
            'Image Height': image.size[1],
            'Megapixels': round(image.size[0] * image.size[1] / 1000000, 1)
        })
        image.close()

    except IOError as ioe:
        print(filepath," -> not an image")

    finally:
        print("getImageDetails() finally block")
        print("imageDetails_dict:\n",imageDetails_dict)
        return imageDetails_dict

def getExifDetails(filepath):
    exifDetails_dict.update({
        'Image DateTime': None,
        'Device Make': None,
        'Device Model': None,
        'Shutter Speed': None,
        'Focal Length (mm)': None,
        'Aperture (f/_)': None,
        'ISO': None
            })
    #print("getExifDetails() None Dictionary Values\n", exifDetails_dict)
    try:
        image = Image.open(filepath)
        EXIF_data = image._getexif()
        print(EXIF_data.get(272))
        print(EXIF_data.get(36867))
        #imagedatetime = str(EXIF_data.get(36867))
        #imagedatetime = datetime.datetime.strptime(imagedatetime, '%Y:%m:%d %H:%M:%S')
        #print(imagedatetime)
        exifDetails_dict.update({
            'Image DateTime': str(dt.datetime.strptime(EXIF_data.get(36867), '%Y:%m:%d %H:%M:%S')),
                #{'Image DateTime': '2019:07:05 16:35:01',
                #{'Image DateTime': datetime.datetime(2020, 9, 12, 19, 45, 13),
                #{'Image DateTime': '2020-09-23 11:06:12',
            'Device Make': EXIF_data.get(271),
            'Device Model': EXIF_data.get(272),
            'Shutter Speed': EXIF_data.get(33434)[0] / EXIF_data.get(33434)[1],
            'Focal Length (mm)': EXIF_data.get(37386)[0] / EXIF_data.get(37386)[1],
            'Aperture (f/_)': EXIF_data.get(33437)[0] / EXIF_data.get(33437)[1],
            'ISO': EXIF_data.get(34855)
        })
        image.close()

    except IOError as ioe:
        print(filepath," -> does not have exif data")

    finally:
        print("getExifDetails() finally block")
        print("exifDetails_dict:\n",exifDetails_dict)
        return exifDetails_dict




main()




print("*** Python Script Testing Output ***")
print("fileDetails_dict")
print(fileDetails_dict)
print("imageDetails_dict")
print(imageDetails_dict)
#print("update fileDetails_dict w/ imageDetails_dict")
#fileDetails_dict.update(imageDetails_dict)
#print(fileDetails_dict)

'''
{'Filename': 'IMG_20200923_110612.jpg',
'File Size': 4538120,
'File Path': '/Users/joeat/Documents/Python/Photo Directory/Pixel 3/IMG_20200923_110612.jpg',
'Processed DateTime': '2020-10-25 10:24:51.379181',
'Image Format': 'JPEG',
'Image Mode': 'RGB',
'Image Size': (4032, 3024),
'Image Width': 4032,
'Image Height': 3024,
'Megapixels': 12.2}

{'Filename': 'IMG_3894.jpg',
'File Size': 1823961,
'File Path': '/Users/joeat/Documents/Python/Photo Directory/IMG_3894.jpg',
'Processed DateTime': '2020-10-26 10:03:43.515500',
'Image Format': 'JPEG',
'Image Mode': 'RGB',
'Image Size': (4032, 3024),
'Image Width': 4032,
'Image Height': 3024,
'Megapixels': 12.2,
'Image DateTime': '2020-10-12 18:13:08',
'Device Make': 'Apple',
'Device Model': 'iPhone XS',
'Shutter Speed': 0.002421307506053269,
'Focal Length (mm)': 4.25,
'Aperture (f/_)': 1.8,
'ISO': 25}

'''

print("\n *** Get file list length ***")
print(str(len(filelist)) + " = the # of files in list")
print("\n *** Here is the first object in file list ***")
print(filelist[0])
print("\n *** Here is the last object in file list ***")
print(filelist[len(filelist)-1])
#print(filelist[1])
#print(filelist)

print("\n *** imageDetails_dict ***")
print(imageDetails_dict)

print("\n *** exifDetails_dict ***")
print(exifDetails_dict)

print("\n *** Python Script Runtime ***")
print(str(len(filelist)) + " = the # of files processed")
print("Start Time: ",processedDateTime)
processEndTime = datetime.now()
print("End Time: ",processEndTime)
print("Duration: ",processEndTime - processedDateTime)
print("Duration (in seconds): ", (processEndTime - processedDateTime).total_seconds())
