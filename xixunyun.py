import requests
import json
import os

# 配置开始 
a = 108.218438
b = 22.837583
user = os.environ["USER"]
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"]  # 签到坐标（注意小数点取后6位）
longitude = a # 经度
latitude = b# 纬度
data = {
  "account":account,
  "password":password,
  "school_id":school_id,
  "longitude":longitude,
  "latitude":latitude,
  "address_name":os.environ["ADDRESS_NAME"] 
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url='https://service-nm4jylpg-1251957121.gz.apigw.tencentcs.com/release/xixunyun', headers=headers, data=json.dumps(data))
print(response.json()["data"])

SCKEY=os.environ["SCKEY"]
if len(SCKEY) >= 1:
  url = 'https://sctapi.ftqq.com/'+SCKEY+'.send'
  requests.post(url, data={"title": "习讯云签到提醒", "desp": response.json()["data"]})

