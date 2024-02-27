import cv2
import os
import base64
import json

number_mapping = {
	"front" : "1", "right" : "2",
	"back" : "3", "left" : "4"
}

name_mapping = {
	"front" : "img1", "right" : "img2",
	"back" : "img3", "left" : "img4"
}


def get_cam(cam_pos):
    cam_id = number_mapping[cam_pos]
    return "/dev/v4l/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1."+cam_id+":1.0-video-index0"

def test_func():
    print(name_mapping["back"])

def check_and_clear_path():
    if not os.path.exists('captures'):
        os.makedirs('captures')
    dir = os.path.join('captures')
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))

def start_capture(cam_positions):

    check_and_clear_path()
    for cam_pos in cam_positions:

        #vid = cv2.VideoCapture(get_cam(cam_pos))
        vid = cv2.VideoCapture(get_cam(cam_pos))

        frame_count = 0
        while(frame_count <= 14):
            ret, frame = vid.read()
            #cv2.imshow('frame', frame)
            frame_count += 1

            '''if cv2.waitKey(1) & 0xFF == ord('q'):
                break'''
        img_name = name_mapping[cam_pos]
        #frame = cv2.resize(frame, (1920,1080), interpolation = cv2.INTER_LINEAR)
        cv2.imwrite(os.path.join('captures', img_name+'.jpg'), frame)
        vid.release()


def load_base64_image(cam_positions):
    start_capture(cam_positions)
    image_names = []
    for cam_pos in cam_positions:
        image_names.append(name_mapping[cam_pos])
    temp_dict = {}
    for image_name in image_names:
        image_path = os.path.join('captures', image_name+'.jpg')
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        temp_dict[image_name] = encoded_string.decode('utf-8')

    with open('input_json.json', 'w') as input_json:
        input_json.write(json.dumps(temp_dict))
    return temp_dict

######
if __name__ == "__main__":
    start_capture(["left", "back"])
