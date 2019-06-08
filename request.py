import requests
import json

def statusRetrieval(url, cat1, cat2, index):
    return json.loads(requests.get('http://' + url + '/rr_status?type=1').text)[cat1][cat2][index]

def sendGcode(url,gcode):
    return requests.get('http://' + url + '/rr_gcode?gcode='+gcode)

def altstatusRetrival(url):
    return json.dumps(requests.get('http://' + url + '/rr_status?type=3').text)

url = '10.1.10.3'
coordx = statusRetrieval(url, 'coords','xyz', 0)
coordy = statusRetrieval(url, 'coords','xyz', 1)
coordz = statusRetrieval(url, 'coords','xyz', 2)
tempbed = statusRetrieval(url, 'temps','current', 0)
tempext = statusRetrieval(url, 'temps','current', 1)


print('The Toolhead is at: (',coordx,', ',coordy,', ',coordz,')')
print('The Extruder is ',tempext,'°C')
print('The Bed is ',tempbed,'°C')
sendGcode(url,'G10 P0 S0')
print(altstatusRetrival(url))
