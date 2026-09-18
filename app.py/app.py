from flask import Flask
import logging
import time

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route("/")
def home():
    logging.info("Home page accessed")
    return "Cloud Monitoring Application is Running!"

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": time.time()
    }

@app.route("/error")
def error():
    logging.error("Test application error generated!")
    return "Test error generated", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)