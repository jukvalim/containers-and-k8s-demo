import socket
from os import environ

import redis
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    r = redis.Redis(
        host=environ.get("REDIS_HOST", "localhost"),
        port=int(environ.get("REDIS_PORT", "6379"))
    )

    r.incr("counter", 1)
    countervalue = r.get("counter").decode('utf-8')
    hostname = socket.gethostname()
    return f"Hello World! Host: {hostname} Request number: {countervalue}"

if __name__ == '__main__':
    app.run()
