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

#POST users

```
curl -X POST -i http://127.0.0.1:5000/users -d “name=foo”
```

#GET users

```
curl -X GET -i http://127.0.0.1:5000/users/1
```

#DELETE users

```
curl -X DELETE -i http://127.0.0.1:5000/users/1
```
