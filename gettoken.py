
import requests
import json

def main():
    url = "https://aip.baidubce.com/oauth/2.0/token?client_id=FitzYqFqjile7u1zhmlC0TOm&client_secret=uZx2PUMo2XbefsZ0jAsIoc9z9D3sZE1F&grant_type=client_credentials"
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
        }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")

if __name__ == '__main__':
    access_token = main()
    print(access_token)
