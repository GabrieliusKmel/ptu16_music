import http.client
import json

connector_class = http.client.HTTPConnection
conn = connector_class("localhost", 8000)

headersList = {
 "Accept": "*/*",
 "User-Agent": "PTU16 python browser" 
}

payload = ""

conn.request("GET", "/bands/", payload, headersList)
response = conn.getresponse()
bands_json = response.read()
bands = json.loads(bands_json)
for band in bands:
    print(band['name'])
# print(result.decode("utf-8"))