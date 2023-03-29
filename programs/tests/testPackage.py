import time
from datetime import datetime
from picamera2 import Picamera2, Preview

picam2 = Picamera2()

camera_config = picam2.create_preview_configuration() # fast
# camera_config = picam2.create_still_configuration()   # 26 seconds
# camera_config = picam2.create_video_configuration()   # slow

picam2.configure(camera_config)
# picam2.set_controls({"AfMode": 1, "AfTrigger": 0, "LensPosition": 425})


tstart1 = datetime.now()
picam2.start()
tend1 = datetime.now()
print()
print("Time for start() command:")
print(tend1 - tstart1)
print()

tstart = datetime.now()
picam2.capture_file("preview.jpg")
tend = datetime.now()

print()
print("Time for capture_file() command:")
print(tend - tstart)
print()


