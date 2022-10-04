# mlt-server

## HOW TO RUN (Background)

If you want to run on Foreground,
skip the '&' at the end

### _Data collection_

- nohup python3 -u request.py 1>[logfile] 2>[errfile] &

### _Run FastApi_

- nohup uvicorn api:app --reload 1>[logfile] 2>[errfile] &

> option

- --host=[address]
- --port=[port]
