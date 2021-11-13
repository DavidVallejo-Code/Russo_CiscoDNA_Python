import json
import requests 
from requests.auth import HTTPBasicAuth

DNAC="sandboxdnac.cisco.com"
DNAC_PORT=443
URL_PARAM="network-device"
api_path="https://sandboxdnac.cisco.com/dna"

def get_token():
	api_path="https://sandboxdnac.cisco.com/dna"
	auth={'devnetuser','Cisco123!'}
	headers={'Content-type':'application/json'}

	auth_resp=requests.post(url="https://sandboxdnac.cisco.com:443/dna/system/api/v1/auth/token",auth=HTTPBasicAuth('devnetuser','Cisco123!'),verify=False)
	#auth_resp=requests.post(f"{api_path}:443/dna/system/api/v1/auth/token",auth=auth,headers=headers)

	#response.raise_for_status() returns an HTTPError object if an error has occurred during the process. It is used for debugging the requests module and is an integral part of Python requests. 
	auth_resp.raise_for_status()

	token=auth_resp.json()["Token"]
	return token


def get_ip(token):
	url=f"http://{DNAC}:{DNAC_PORT}/api/v1/{URL_PARAM}"
	headers={'X-auth-token':token}
	try:
		response = requests.get(url, headers=headers, verify=False)
	except requests.exceptions.RequestException as cerror:
		print("Error processing request", cerror)
		sys.exit(1)

	return response.json()

token=get_token()
headers={'Content-type':'application/json','X-auth-token':token}
get_resp=requests.get("https://sandboxdnac.cisco.com:443/api/v1/network-device",headers=headers)	
api_path="https://sandboxdnac.cisco.com/dna"
print(json.dumps(get_resp.json(),indent=2))
#get and print IP's and ID's 
#ensure that main is called whenever the module is ran from the shell
