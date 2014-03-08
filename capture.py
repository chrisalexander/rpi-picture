#/usr/bin/env python3

import picamera

with picamera.PiCamera() as camera:
	camera.resolution = (1024, 768)
	camera.capture("test.jpg")
