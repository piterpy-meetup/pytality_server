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
```
<file with the random incorrect snippet>
```

[2] Submit corrected snippet from developer: `POST /snippets/<snippet_id>/`

Request:
```
<file with the corrected snippet>
```

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