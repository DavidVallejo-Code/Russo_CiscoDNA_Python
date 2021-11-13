import requests
from requests.auth import HTTPBasicAuth


#def get_auth_token(IP,username,password):
DNAC="sandboxdnac.cisco.com"
DNAC_USER="devnetuser"
DNAC_PASSWORD="Cisco123!"
DNAC_PORT=443
path="network-device"

def list_network_devices():
    return get_url("network-device")

def get_url(url):

    url = create_url(path=url,port=443)
    print(url)
    token = get_auth_token()

    #use the token retreived using  get_auth_token() func to make a query to the sandbox using GET
    headers = {'X-auth-token' : token['token']}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("Error processing request", cerror)
        sys.exit(1)

    return response.json()

def get_auth_token():
	#this site is just used to get the AUTH token.Not to make queries to DNA
	login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(DNAC, DNAC_PORT)
	#https://www.w3schools.com/python/ref_requests_post.asp
	#https://docs.python-requests.org/en/latest/user/authentication/
	result = requests.post(url=login_url, auth=HTTPBasicAuth(DNAC_USER, DNAC_PASSWORD), verify=False)
	result.raise_for_status()

	token=result.json()["Token"]
	return{
		"token":token,
		"controller_ip":DNAC
	}

def create_url(path, port, controller_ip=DNAC):
    """ Helper function to create a DNAC API endpoint URL
    """

    return "https://{0}:{1}/api/v1/{2}".format(controller_ip, port, path)


response = list_network_devices()
print(type(response))

for x in response:
	print(x)
	print("===============")