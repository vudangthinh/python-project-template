import os, sys
import json
from flask import Blueprint
from flask import Flask, request, jsonify
import requests
import logging
import argparse

# Config
parser = argparse.ArgumentParser(description="Config")
parser.add_argument("--", type=str, default="", help="")
args = parser.parse_args()

# Logging
logging.basicConfig(filename="", filemode="w", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s")

# API
home_api = Blueprint("api", __name__)

if __name__=='__main__':
    pass