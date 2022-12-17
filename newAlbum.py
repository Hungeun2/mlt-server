import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    
def newAlbum():
  endPoint = "https://m2.melon.com/new/album/list.json?areaFlg=A"
  response = requests.get(endPoint, headers=headers)
  data = response.json()

  return data

def albumInfo(id):
  endPoint = 'https://m2.melon.com/m6/v4/album/info.json?albumId=' + str(id)
  response = requests.get(endPoint, headers=headers)
  data = response.json()
  return data