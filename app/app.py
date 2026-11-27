from flask import Flask, jsonify, Response
from prometheus_client import Counter, generate_latest
from prometheus_client import CONTENT_TYPE_LATEST
import os
import socket

# --------------------------------
# 1. Flask Application
# --------------------------------

app = Flask(__name__)

# --------------------------------
# 2. Prometheus Metrics
# --------------------------------

REQUEST_COUNT = Counter(
    "app_requests_total",
    "Total number of application requests",
    ["endpoint"]
)

# --------------------------------
# 3. Home Page
# --------------------------------

@app.route("/")
def home():

    REQUEST_COUNT.labels(endpoint="/").inc()

    return jsonify({
        "project": "AWS DevOps CI/CD Platform",
        "application": "DevOps Monitoring Portal",
        "status": "Running",
        "technology": "Python Flask",
        "monitoring": "Prometheus and Grafana"
    }), 200


# --------------------------------
# 4. Application Health Check
# --------------------------------

@app.route("/health")
def health():

    REQUEST_COUNT.labels(endpoint="/health").inc()

    return jsonify({
        "status": "Healthy",
        "message": "Application is working",
        "http_status": 200
    }), 200


# --------------------------------
# 5. Application Information
# --------------------------------

@app.route("/info")
def info():

    REQUEST_COUNT.labels(endpoint="/info").inc()

    return jsonify({
        "application": "Flask DevOps App",
        "hostname": socket.gethostname(),
        "environment": os.getenv(
            "ENVIRONMENT", "Development"
        ),
        "port": 5000
    }), 200


# --------------------------------
# 6. Prometheus Metrics Endpoint
# --------------------------------

@app.route("/metrics")
def metrics():

    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST
    )


# --------------------------------
# 7. Application Startup
# --------------------------------

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
# Devops Project version -2

# --------------------------------
# 8. github webhook
# --------------------------------

@app.route("/webhook-test")
def webhook_test():
    return "GitHub Webhook Working!"
