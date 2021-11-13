import requests 
from requests.auth import HTTPBasicAuth

def get_token(): 

	api_path="sandboxdnac2.cisco.com/dna"
	auth={'dnacdev','D3v93T@wK'}
	headers={'Content-type':'application/json'}

	auth_resp=requests.post(url="https://sandboxdnac.cisco.com:443/dna/system/api/v1/auth/token",auth=HTTPBasicAuth('devnetuser','Cisco123!'),verify=False)
	#auth_resp=requests.post(f"{api_path}:443/dna/system/api/v1/auth/token",auth=auth,headers=headers)

	#response.raise_for_status() returns an HTTPError object if an error has occurred during the process. It is used for debugging the requests module and is an integral part of Python requests. 
	auth_resp.raise_for_status()

	token=auth_resp.json()["Token"]
	return token


token=get_token()
print("anything")
print(token)

#ensure that main is called whenever the module is ran from the shell

