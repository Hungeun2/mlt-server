import requests
import json
import schedule
import time

def save(likeCnt,listnerCnt,streamCount,streamUser,song_num,song_name,song_artist):
  try:
    with open('./Data/'+song_num+'.json', 'r', encoding='utf-8') as fp:
      json_data = json.load(fp)
      
    new_data = [{
      "Date": time.strftime('%y%m%d'),
      "Time":  time.strftime('%H%M'),
      "Cnt": str(likeCnt),
      "listnerCnt": str(listnerCnt),
      "StreamCount": str(streamCount),
      "StreamUser": str(streamUser)
    }]
    json_data["data"] += new_data

    with open('./Data/'+song_num+'.json', 'w') as fp:
      json.dump(json_data,fp,indent=2)
  except:
    initial_data = {
        "Info": {
    		"Num": song_num,
    		"Name": song_name,
    		"Artist": song_artist,
  		},
        "data": [{
      		"Date": time.strftime('%y%m%d'),
      		"Time":  time.strftime('%H%M'),
      		"Cnt": str(likeCnt),
          "listnerCnt": str(listnerCnt),
          "StreamCount": str(streamCount),
          "StreamUser": str(streamUser)
    	}]
    }
    with open('./Data/'+song_num+'.json', 'w+', encoding='utf-8') as fp:
      json.dump(initial_data,fp,indent=2)

def Info(song_num, headers):
  Info_endPoint = "https://m2.melon.com/m6/v1/song/info.json?songId="
  response_info = requests.get(Info_endPoint + song_num, headers=headers)
  data = response_info.json()
  likeCnt = data["response"]["LIKECNT"]
  listnerCnt = data["response"]["DAILYLISTENINFO"]["LISTNERCNT"]
  
  return likeCnt, listnerCnt
    
def Streaming(song_num, headers):
  stream_endPoint = "https://m2.melon.com/m6/chart/streaming/card.json?songId="
  response_stream = requests.get(stream_endPoint + song_num, headers=headers)
  data = response_stream.json()
  streamCount = data["response"]["STREAMCOUNT"]
  streamUser = data["response"]["STREAMUSER"]
  
  return streamCount,streamUser
  
def req():
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36','Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}

  with open('./Data/song_list.json', 'r') as file:
    data = json.load(file)
    
  for song in data["songlist"]:
    song_num = str(song["Num"])
    song_name = str(song["Name"])
    song_artist = str(song["Artist"])
    
    try:
      likeCnt,listnerCnt = Info(song_num, headers)
    except:
      try:
        time.sleep(1)
        print("try second")
        likeCnt,listnerCnt = Info(song_num, headers)
      except:
        likeCnt,listnerCnt = (0,0)
    
    try:
      streamCount,streamUser = Streaming(song_num, headers)
    except:
      try:
        time.sleep(1)
        print("try second")
        streamCount,streamUser = Streaming(song_num, headers)
      except:
        streamCount,streamUser = (0,0)
    
    save(likeCnt,listnerCnt,streamCount,streamUser,song_num,song_name,song_artist)
    

#3sec for test
# schedule.every(30).seconds.do(req)

# everyMin
schedule.every().minute.at(":00").do(req)

# everyHour
# schedule.every().hour.at(":00").do(req)
while True:
    schedule.run_pending()
    time.sleep(1)
# req()