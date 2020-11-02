
import requests
import json
import threading

class LIFXController():
    
    def __init__(self, token):
        self.headers = {
                    "Authorization": "Bearer %s" % token,
                }
            
        
    def getAllLights(self):
        return requests.get(
            'https://api.lifx.com/v1/lights/all', headers=self.headers)
    
    # toggles power of passed in label and state
    def togglePower(self, label, state):
        
        payload = {
            "power": state,
        }
        # debug methods
        print("Label togglePower: "+label)
        print("Label state togglePower: "+state)
        return requests.put(
            'https://api.lifx.com/v1/lights/label:'+label+'/state', data=payload, headers=self.headers)

    def changeBrightness(self, label, brightness):
        
        payload = {
            "brightness": brightness,
        }
        # debug methods
        #print("Label Changebrightness: "+label)
        #print("Brightness Level : "+ brightness)
        return requests.put(
            'https://api.lifx.com/v1/lights/label:'+label+'/state', data=payload, headers=self.headers)

    def changeColor(self, label, color):
        
        payload = {
            "color": color,
        }
        # debug methods
        #print("Label Changebrightness: "+label)
        #print("Brightness Level : "+ brightness)
        return requests.put(
            'https://api.lifx.com/v1/lights/label:'+label+'/state', data=payload, headers=self.headers)

   
    # returns a list of light IDs

    


class APIThread(threading.Thread):
    #START OF THREADING METHODS
    pass
    

