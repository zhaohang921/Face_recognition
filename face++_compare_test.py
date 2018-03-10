import requests
from json import JSONDecoder

http_url ="https://api-cn.faceplusplus.com/facepp/v3/compare"
key ="GJZbKHdqCbgFoqDjPxdgzN9l8v3hkHuc"
secret ="jlt1C_M0pUZ27U1XCd4cpkPcjXA4pSsp"
filepath1 ="D:/data/1.jpg"
filepath2 ="D:/data/2.jpg"
data = {"api_key": key, "api_secret": secret, "return_landmark": "0"}
files = {"image_file1": open(filepath1, "rb"),"image_file2": open(filepath2, "rb")}
response = requests.post(http_url, data=data, files=files)
req_con = response.content.decode('utf-8')
req_dict = JSONDecoder().decode(req_con)
print(req_dict)
