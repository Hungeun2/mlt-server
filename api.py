from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import json
from pydantic import BaseModel
import newAlbum

app = FastAPI()
favicon_path = 'favicon.ico'

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def aa():
    return FileResponse('./Data/song_list.json')

@app.get('/favicon.ico')
async def favicon():
    return FileResponse(favicon_path)

@app.get("/artist")
async def bb(name: str):
    temp = []
    with open('./Data/song_list.json','r') as file:
        data = json.load(file)
    
    for song in data["songlist"]:
        if song["Artist"] == name:
            temp.append(song)
    
    return temp

@app.get("/newalbum")
async def albumlist():
  data = newAlbum.newAlbum()
  return data

@app.get("/albuminfo")
async def albuminfo(id: int):
  data = newAlbum.albumInfo(id)
  return data

@app.get("/{song_num}")
async def user_data(song_num: int):
  return FileResponse('./Data/'+str(song_num)+'.json')

# Register
class Model(BaseModel):
  Num :int
  Name :str
  Artist :str
  
@app.post("/register")
async def Register(data : Model):
  new_data = [data.dict()]
  
  with open('./Data/song_list.json','r', encoding='utf-8') as fp:
    ori_data = json.load(fp)
  
  for song in ori_data["songlist"]:
    # already exists -> fail
    if(song["Num"] == new_data[0]["Num"]):
      return 'exists'
    
  ori_data["songlist"] += new_data
  with open('./Data/song_list.json', 'w') as fp:
    json.dump(ori_data,fp,indent=2)
  
  return 'success'