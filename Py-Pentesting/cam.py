
import requests
import logging
import sys
from time import sleep

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

#Wait for IP camera to connect. Will not exit until this works
while(True):
    try:
        url = 'http://10.4.1.19/mjpg/video.mjpg' # IP Address of the Camera
        stream = requests.get(url, stream=True)
        bytes = b''
        print('Connected to IP Camera')
        break
    except:
        sleep(0.5)
        print('No cam yet')
        pass
    

while(True):

    # When nothing is seen there is a divide by zero error, so this skips over those frames
    try:
        # Takes frames from the camera that we can use
        bytes+=stream.raw.read(16384)
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a!=-1 and b!=-1:
            jpg = bytes[a:b+2]
            bytes= **bytes
            frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
            img = framee
