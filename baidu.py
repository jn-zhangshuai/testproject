import requests
import json
#修改成自己的api key和secret key
API_KEY = "FitzYqFqjile7u1zhmlC0TOm"
SECRET_KEY = "uZx2PUMo2XbefsZ0jAsIoc9z9D3sZE1F"
 
 
def main():
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
#注意message必须是奇数条
    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "你好"
            }
            #,
            #{
            #    "role": "assistant",
            #    "content": "你好，有什么我可以帮助你的吗？"
            #}
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }
 
    response = requests.request("POST", url, headers=headers, data=payload)
 
    print(response.text)
 
 
def get_access_token():

    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))
 
 
if __name__ == '__main__':
    main()
