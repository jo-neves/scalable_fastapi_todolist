# FASTAPI TODOLIST

## Run through docker
```
docker build -t todolist-app:0.1.0 .
docker run -p 8000:8000 --name todolist-app todolist-app:0.1.0
# http://127.0.0.1:8000/docs
```

## Run through the CLI:
`uvicorn main:app --reload`
