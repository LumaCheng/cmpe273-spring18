# How to Setup

```
virtualenv my-venv
.my-venv/bin/activate
pip3 install -r requirements.txt
```

# how to run it?

```
FLASK_APP=hello.py flask run
```

# GET/

```
curl -l -i http://127.0.0.1:5000/
```

# POST users

```
curl -X POST -i http://127.0.0.1:5000/users -d “name=foo”
```

## Response

```
HTTP/1.0 201 Created
...
{
    "id": 1,
    "name": "foo"
}
```

# GET users

```
curl -X GET -i http://127.0.0.1:5000/users/1
```

## Response

```
HTTP/1.0 200 OK
...
{
    "id": 1,
    "name": "foo"
}
```

# DELETE users

```
curl -X DELETE -i http://127.0.0.1:5000/users/1
```

## Response

```
HTTP/1.0 204 No Content
...
```
