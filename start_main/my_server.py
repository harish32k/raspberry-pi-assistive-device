import os
os.chdir('/home/pi/Desktop/start_main')
import bluetooth
import json
from capturer import start_capture, load_base64_image, name_mapping
from facial_req import face_detect
from car_caps import get_snap
from make_model_request import call_model, call_grief
from buzzer_test import make_sound

from thread_test import thread

server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_socket.bind(("",port))
server_socket.listen(1)
img_dir = 'captures'

my_thread = None

def start_face(cam_positions = ["left", "right"]):
	start_capture(cam_positions)
	faces = []
	outputs = {}
	for cam_pos in cam_positions:
		img_name = name_mapping[cam_pos]
		file_name = os.path.join(img_dir, img_name+'.jpg')
		detections = face_detect(file_name)
		faces.append(detections)
		outputs[cam_pos] = detections
	print(cam_positions)
	print(faces)
	print(outputs)
	
	with open('input_json.json', 'w') as input_json:
		input_json.write(json.dumps(outputs))
		
def vehicle_start():
	my_thread = thread("cap_thread", 1000)
	my_thread.start()
	return my_thread
	
def vehicle_stop(my_thread):
	my_thread.runvar[0] = False


while 1:

	print("Waiting for connect request: ")
	make_sound()
	client_socket,address = server_socket.accept()
	make_sound()
	print ("Accepted connection from ",address)
	while 1:
		try:
			data = client_socket.recv(1024)
			data = data.decode("utf-8")
			print(data)
			if data:
				queries = data.split()
				task = queries[0]
				uid = queries[1]
				positions = queries[2:]
				print(task, uid, positions)
				#print(queries, task, positions)
				print ("Received: %s" % str(data))
				if (task == "face"):
					#get_snap()
					start_face(positions)
					call_model(uid, task)
				elif task in ["object", "caption", "ocr", "depth", "obj_depth"]:
					start_capture(positions)
					load_base64_image(positions)
					call_model(uid, task)
				elif task == "grief":
					coords = positions
					positions = ["front", "right", "back", "left"]
					start_capture(positions)
					load_base64_image(positions)
					call_grief(uid, coords)
					#call_model(uid, task)
				elif task == "vehicle_start":
					my_thread = vehicle_start()
					'''import time
					time.sleep(30)
					vehicle_stop(my_thread)'''
				elif task == "vehicle_stop":
					vehicle_stop(my_thread)
				if (data == "q"):
					print ("Quit")
					break
				print("done")
		except Exception as e:
			make_sound(4)
			#raise e
			print(str(e) + ", continuing") 
			break
client_socket.close()
server_socket.close()

