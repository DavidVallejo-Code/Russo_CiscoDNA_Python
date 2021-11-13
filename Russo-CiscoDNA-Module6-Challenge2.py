import time
import requests
from Russo_CiscoDNA_Module6 import get_token


token=get_token()

headers={'Content-type':'application/json','X-auth-token':token}
api_path="https://sandboxdnac.cisco.com/dna"

new_device_dict={
	"cliTransport": "ssh",
	"snmpVersion":"v2",
	"snmpROCommunity":"readonly",
	"snmpRWCommuity":"readwrite",
	"snmpRetry":"1",
	"snmpTimeout":"60",
	"username":"nick",
	"password":"secret123",
	"enablePassword": "cisco123",
	"ipAddress": [
		"10.1.1.111"
	]
}

#issue HTTP POST request to add a new device 
add_resp=requests.post(f"{api_path}/intent/api/v1/network-device",json=new_device_dict,headers=headers)

if add_resp.ok:
	#wait for seconds after server 
	print(f"requests acceted: status code {add_resp.status_code}")
	time.sleep(10)

	#query DNA center fo rthe status of the specific task
	task=add_resp.json()["resonse"]["taskid"]
	task_resp=requests.get(f"{api_path}/api/v1/task/{task}",headers=headers)

	if task_resp.ok:
		task_data=task_resp.json()["resonse"]
		if not task_data["isError"]:
			print("new device added")
		else:
			print(f"async task isError")
	else:
		print(f"async get failed tatus code {task_resp.status_code}")
else:
	print(f"POST failed with code: {add_resp.status_code}")
	print(f"failure body: {add_resp.text}" )