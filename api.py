from fastapi import FastAPI
from fastapi.responses import FileResponse
from starlette.middleware.cors import CORSMiddleware
import json

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

@app.get("/{song_num}")
async def user_data(song_num: int):
  return FileResponse('./Data/'+str(song_num)+'.json')

