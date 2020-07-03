import requests
import json

headers = {  # 请求头
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0'
}

# 封装requests，直接请求并处理返回json数据
# 链接 -> json
def reqjson(link):  # 请求并处理json数据1
  r = requests.get(link, headers=headers)
  cont_str = r.text
  return json.loads(cont_str)
