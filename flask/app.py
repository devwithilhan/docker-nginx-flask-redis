from flask import Flask
from redis import Redis
import socket

app = Flask(__name__)

redis_cache = Redis(
    host="redis",
    port=6379
)

@app.route("/")
def hello_world():
    hostname = socket.gethostname()

    return (
        "<h1>Hi, hier sehen wir Flask, Redis und Nginx zusammen in Aktion!</h1>"
        f"<h3>Das ist der Container mit der ID {hostname}</h3>"
    )

@app.route("/health")
def health():
    return "Hallo Welt", 200
    
@app.route("/visits")
def count_visit():
    hostname = socket.gethostname()

    counter = redis_cache.incr("num_visits")

    return (
        f"<h2>Anzahl der Besucher: {counter}</h2>"
        f"<h3>Das ist der Container mit der ID {hostname}</h3>"
    )


@app.route("/visits/reset")
def reset_visits_counter():
    hostname = socket.gethostname()

    redis_cache.set("num_visits", 0)

    return (
        "<h2>Anzahl der Besucher wurde zurückgesetzt auf: 0</h2>"
        f"<h3>Das ist der Container mit der ID {hostname}</h3>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)