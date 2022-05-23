from os import listdir
from os.path import isfile, join
from PIL import Image

mypath = '/Users/mohammedarham/Downloads/draven/' #draven here was the name of my folder containing all the images
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for img_file_path in onlyfiles: 
    frame_1 = Image.open(f'{mypath}{img_file_path}')
    rotated = frame_1.rotate(90) #anticlockwise
    rotated.save(f'{mypath}{img_file_path}')
    

