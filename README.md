
# raspberry-pi-assistive-device

  
## Getting started
This repository contains the code that runs on the Raspberry Pi of the Multi-Camera Blind assistive device.

  

To get started, place the directory `start_main` anywhere on the local storage of the Raspberry Pi.

  

The program `my_server.py` contains the code that starts the execution of the assistive functionalities by setting up Bluetooth connectivity for the Mobile Application to connect.

  

The Raspberry Pi should be connected with Four cameras to its 4 USB slots for this software to work correctly.

  ## Vehicle Detection

This package also contains an object detection model (Google's SSDLite with Mobilenet v2 model.) for detecting vehicles in real-time. For general object detection purpose, this software requests the cloud server to detect objects and label them.

  

The Raspberry Pi must also be connected to a Buzzer at GPIO pin 17 so that when the vehicles are detected from the front camera, the buzzer makes a sound.

  ## Facial Recognition

Facial detection is done using `face-recognition` package of python which can be installed through `pip` [(face-recognition package)](https://github.com/ageitgey/face_recognition)

## General Features
All other features such as depth perception, OCR, image/scene description, object identification etc run on the cloud and the software performs an API call to the cloud server with the images to perform those assistive functions.
  
  ## Auto Start at Boot

The Raspberry Pi can be set up to auto-start this software at boot time by putting the python run command for `my_server.py` in `/etc/init.d` if you are using Raspbian OS. Whenever the OS boots up, the program will prompt a buzzer sound to make us aware that the device is ready to be connected through bluetooth.