# FlaskPort
Simple flask app, show the port client using.
For testing wheather http client is using same connection.

# Dependency
```sh
pip install flask
```

# Server
```sh
./FlaskPort.py
```

# Client
```python
>>> from requests import session
>>> [s1, s2] = [session(), session()]
>>> url='http://127.0.0.1:5000'
>>> s1.get(url).text == s1.get(url).text
True
>>> s2.get(url).text == s2.get(url).text
True
>>> s1.get(url).text == s2.get(url).text
False
```
