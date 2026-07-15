from flask import Flask
import redis
app = Flask(__name__)

cache = redis.Redis(host='redis', port=6379)

@app.route("/")
def home():
    try:
        visits = cache.incr("counter")
    except:
        visits = "Redis connection failed"
    return f"""
    <h1>Docker Compose Demo</h1>
    <p>Visits:{visits}</p>
    """
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)