import requests
import json
import certifi
import urllib3
from pprint import pprint
from getpass import getpass

urllib3.disable_warnings() 

#Data collection
u = input ('Input username: ')
p = getpass(prompt='Input password: ')
url = input('Input Hostname or IP address: ')
protocol = 'https://'
 

x="0"
attempts=0


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def auth():
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  uri = '/api/fdm/v6/fdm/token'
  token_url = protocol+url+uri

  payload = {
        'grant_type' : 'password',
        'username' : u,
        'password': p
        }

  response = requests.post(token_url, data=payload, verify=False)
  
  #ONlY USE "verify=False" in a lab setting!

#Error Checking
  if response.status_code == 400:
    raise Exception("Error Received: {}".format(response.content))
  else:
    access_token = response.json()['access_token']
    return access_token


token = auth()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def deploy():
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  uri = '/api/fdm/v6/operational/deploy'
  deploy = protocol+url+uri

  headers = headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization":"Bearer {}".format(token)
  }

  payload = {
  "statusMessage": "string",
  "cliErrorMessage": "string",
  "state": "QUEUED",
  "queuedTime": 0,
  "startTime": 0,
  "endTime": 0,
  "statusMessages": [
    "string"
    ],
  "id": "string",
  "name": "string",
  "modifiedObjects": {},
  "forceRefreshDeploymentData": False,
  "type": "deploymentstatus"
  }

  data = json.dumps(payload)

  response = requests.get(deploy, headers=headers, data=data,verify=False)
  if response.status_code == 200:
    print(response.status_code)
    status = response.json()['items'][0]['statusMessage']
    return status
  else:
    print(response.status_code)
    pass
    
status = deploy()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def deploy2():
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  uri = '/api/fdm/v6/operational/deploy'
  deploy = protocol+url+uri

  headers = headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization":"Bearer {}".format(token)
  }

  payload = {
  "statusMessage": "string",
  "cliErrorMessage": "string",
  "state": "QUEUED",
  "queuedTime": 0,
  "startTime": 0,
  "endTime": 0,
  "statusMessages": [
    "string"
    ],
  "id": "string",
  "name": "string",
  "modifiedObjects": {},
  "forceRefreshDeploymentData": False,
  "type": "deploymentstatus"
  }

  data = json.dumps(payload)

  response = requests.post(deploy, headers=headers, data=data,verify=False)
  if response.status_code == 200:
    print(response.status_code)
    print('Deploying')
  else:
    print(response.status_code)
    pass





#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def revoke():
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

  uri = '/api/fdm/v6/fdm/token'
  token_url = protocol+url+uri

  headers = {
      "Content-Type": "application/json",
      "Accept": "application/json",
      "Authorization":"Bearer"
  }
  payload = {
        'grant_type' : 'revoke_token',
        "access_token": token,
        "token_to_revoke": token,
        }

  response = requests.post(token_url, data=payload, verify=False)
  if response.status_code == 200:
    print("Access token revoked")
  else:
    print(response.status_code)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


while True:
  x = input("""
            Press 1 for deployment status
            Press 2 to deploy
            Enter Exit to exit
            > """).lower()
  if x == "1":
    deploy()
    pprint('Status is: ' + status)
  elif x == "2":
    deploy2()
  elif x == "exit":
    break
    revoke()
  elif x != "1" or "2" or "exit":
    attempts += 1
    print("The options are 1, 2 or Exit only!")
    if attempts == 3:
      print('Closing the program')
      revoke()
      break
  else:
    raise Exception("Program shutting down")