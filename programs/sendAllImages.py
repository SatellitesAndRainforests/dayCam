import requests
import glob

url = 'http://10.3.141.128:8080/captures/image-from-client'

for filepath in glob.iglob('/home/pi/dayCam/images/*.jpg'):
    files = {'image': open( filepath, 'rb')}
    requests.post(url, files=files)

