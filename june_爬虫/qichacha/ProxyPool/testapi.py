#-*- coding:utf-8 -*-        
# @time  :18-11-28 下午7:40    
# @Author :董振兵                
# @File   :testapi
import requests

# 根据协议类型，选择不同的代理
proxies = {
    # "http": "http://39.137.2.210:8080",
    "http": "61.187.206.207:57819",
}

response = requests.get(
    "https://www.qichacha.com",
    timeout=10,
    proxies = proxies
)
print(response.status_code)
