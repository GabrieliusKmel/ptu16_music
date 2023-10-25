import requests
import json

reqUrl = "http://localhost:8000/bands/"

headersList = {
 "Accept": "*/*",
 "User-Agent": "PTU16 browser",
 "Authorization": "Token d94b41d6e31ed338334db90d4e855c4530fc4454",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "name" : "aaa3 per requests"
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)