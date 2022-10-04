# import requests
# import json
# import schedule
# import time

# def save(likes_cnt,song_num,song_name,song_artist):
#   try:
#     with open('./Data/'+song_num+'.json', 'r', encoding='utf-8') as fp:
#       json_data = json.load(fp)
      
#     new_data = [{
#       "Date": time.strftime('%y%m%d'),
#       "Time":  time.strftime('%H%M'),
#       "Cnt": str(likes_cnt)
#     }]
#     json_data["data"] += new_data

#     with open('./Data/'+song_num+'.json', 'w') as fp:
#       json.dump(json_data,fp,indent=2)
      
#   except:  
#     initial_data = {
#         "Info": {
#     		"Num": song_num,
#     		"Name": song_name,
#     		"Artist": rtist,
#   		},
#         "data": [{
#       		"Date": time.strftime('%y%m%d'),
#       		"Time":  time.strftime('%H%M'),
#       		"Cnt": str(likes_cnt)
#     	}]
#     }
#     with open('./Data/'+song_num+'.json', 'w+', encoding='utf-8') as fp:
#       json.dump(initial_data,fp,indent=2)
    
    
# def req():
#   headers = {'User-Agent':'PostmanRuntime/7.29.2', 'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
#   endPoint = "https://m2.melon.com/song/likeAndCmt.json?songId="
    
#   with open('./Data/song_list.json', 'r') as file:
#     data = json.load(file)
    
#   for song in data["songlist"]:
#     song_num = str(song["Num"])
#     song_name = str(song["Name"])
#     song_artist = str(song["Artist"])
    
#     url = endPoint + song_num

#     try:
#         response = requests.get(url, headers=headers)
#         save(response.json()["likeCnt"],song_num,song_name,song_artist)
#     except requests.exceptions.RequestException as erra:
#       print(url)
#       print("AnyException : ", erra)
#       print(time.strftime('%y%m%d %H시 %M분 %S초', time.localtime(time.time())))
  
# #3초마다 
# schedule.every(3).seconds.do(req)
# # 매분마다
# # schedule.every().minute.at(":00").do(job)
# # schedule.every().minute.at(":00").do(req)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

import requests
import json
import schedule
import time

def save(likes_cnt,song_num,song_name,song_artist):
  try:
    with open('./Data/'+song_num+'.json', 'r', encoding='utf-8') as fp:
      json_data = json.load(fp)
      
    new_data = [{
      "Date": time.strftime('%y%m%d'),
      "Time":  time.strftime('%H%M'),
      "Cnt": str(likes_cnt)
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
      		"Cnt": str(likes_cnt)
    	}]
    }
    with open('./Data/'+song_num+'.json', 'w+', encoding='utf-8') as fp:
      json.dump(initial_data,fp,indent=2)
    
    
def req():
  headers = {'User-Agent':'PostmanRuntime/7.29.2', 'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
  endPoint = "https://m2.melon.com/song/likeAndCmt.json?songId="
    
  with open('./Data/song_list.json', 'r') as file:
    data = json.load(file)
    
  for song in data["songlist"]:
    song_num = str(song["Num"])
    song_name = str(song["Name"])
    song_artist = str(song["Artist"])
    
    url = endPoint + song_num

    try:
        response = requests.get(url, headers=headers)
        save(response.json()["likeCnt"],song_num,song_name,song_artist)
    except requests.exceptions.RequestException as erra:
      print(url)
      print("AnyException : ", erra)
      print(time.strftime('%y%m%d %H시 %M분 %S초', time.localtime(time.time())))
  
#3초마다 
schedule.every(3).seconds.do(req)
# 매분마다
# schedule.every().minute.at(":00").do(job)
# schedule.every().hour.at(":00").do(req)
while True:
    schedule.run_pending()
    time.sleep(1)