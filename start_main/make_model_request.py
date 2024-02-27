from buzzer_test import make_sound

import json
import requests



api_url = "https://central-api-g4ie3zivpa-uw.a.run.app/"

endpoints = {"object" : "object-detect", "caption" : "captioning",
            "ocr" : "read-text", "depth" : "depth-estimate", 
            "obj_depth" : "object-and-depth", "grief" : "grief-signaling",
            "face" : "face-detect"}
#payload = {'key': 'value'}

def call_model(uid, task):
    payload = {}
    with open("input_json.json", 'r') as json_file:
        payload = json.loads(json_file.read())
    payload["uid"] = uid
    url = api_url + endpoints[task]
    try:
        make_sound()
        r = requests.post(url, json=payload)
        print(r.status_code)
        status = str(r.status_code)
        if status in ["404", "403", "400", "500"] :
            raise Exception
        make_sound()
    except:
        make_sound(3)
        
def call_grief(uid, coords):
    payload = {}
    with open("input_json.json", 'r') as json_file:
        payload = json.loads(json_file.read())
    payload["uid"] = uid
    payload["lat"] = coords[0]
    payload["lon"] = coords[1]
    
    url = api_url + endpoints["grief"]
    try:
        make_sound()
        r = requests.post(url, json=payload)
        print(r.status_code)
        status = str(r.status_code)
        if status in ["404", "403", "400", "500"] :
            raise Exception
        make_sound()
    except:
        make_sound(3)
    
