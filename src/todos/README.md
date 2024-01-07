# :bookmark: My Little Todo App
![test](https://github.com/github/docs/actions/workflows/todos.yml/badge.svg)

This project includes the simple CRUD todo API sources.
The API defines with [FastAPI](https://fastapi.tiangolo.com/). 

## How to use
### :one: Run the app server
```bash
# Run main.py
$ make run

pants run main.py
INFO:     Started server process [35328]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
### :two: Request to app server
There's two way to try out this application.
#### A) FastAPI docs
Access FastAPI docs and try it out with simple execute buttons
* http://0.0.0.0:8000/docs
* http://0.0.0.0:8000/monitor/docs
* http://0.0.0.0:8000/todos/v1/docs
#### B) In console
```bash
# /apis
$ curl -X 'GET' \
  'http://0.0.0.0:8000/apis' \
  -H 'accept: application/json'

# /monitor
$ curl -X 'GET' \
  'http://0.0.0.0:8000/monitor/l7check' \
  -H 'accept: application/json'

# /todos/v1/add
$ curl -X 'POST' \
  'http://0.0.0.0:8000/todos/v1/add' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "completed": false
}'

# /todos/v1/retrieve
$ curl -X 'GET' \
  'http://0.0.0.0:8000/todos/v1/retrieve' \
  -H 'accept: application/json'

# /todos/v1/update
$ curl -X 'PUT' \
  'http://0.0.0.0:8000/todos/v1/update/7d73b5f68af54d12977ff4f421c746d8' \ # item_id
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "string",
  "description": "string",
  "completed": false
}'

# /todos/v1/delete
$ curl -X 'DELETE' \
  'http://0.0.0.0:8000/todos/v1/delete/7d73b5f68af54d12977ff4f421c746d8' \ # item_id
  -H 'accept: application/json'
```


## ETC
```bash
# Formatting codes in this project
$ make fmt

# Linting codes in this project
$ make lint

# Build docker image with Dockerfile in this project
$ make docker-build

# Run docker container with Dockerfile in this project
$ make docker-run
```
