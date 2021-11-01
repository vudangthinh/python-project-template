import os, sys
import json
from flask import Blueprint
from flask import Flask, request, jsonify
import requests
import logging
import argparse

# Config
parser = argparse.ArgumentParser(description="Config")
parser.add_argument("--host", type=str, default="0.0.0.0", help="host to service")
parser.add_argument("--port", type=int, default=5000, help="port to service")
args = parser.parse_args()

host = args.host
port = args.port

# Logging
logging.basicConfig(
    filename="",
    filemode="w",
    level=logging.DEBUG,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

# API
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World!"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host=host, port=port)
