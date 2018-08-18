# Pytality server

server for the code-battle interactive game

## Install & run a local machine

Setup postgres as described in `settings.py`.

```bash

$ python manage.py migrate
$ python manage.py runserver

```

## API documentation

[1] Get next random snippet: `GET /snippets/next/`

Response:
```json
{
    "status": "OK",
    "snippet_id": 17,
    "code": "print a\n\nprint b",
    "time_so_solve": 5
}
```

[2] Submit state of a snippet from developer (websocket)

Request:
```json
{
    "snippet_id": 17,
    "code": "print(a)\n\nprint(b)" 
}
```

Response:
```json
{
    "status": "OK"
}
```

[3] Submit the fact that developer is finished (websocket)

Response:
```json
{
    "status": "OK",
    "data": {
        "result": "passed" | "failed"
    }    
}
```

or

```json
{
    "status": "error",
    "errors": [<..>]
}
```