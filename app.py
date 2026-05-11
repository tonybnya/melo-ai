"""
Script Name : app.py
Description : Melo AI main application
Author      : @tonybnya
"""

import os
import logging
from flask import Flask
from datetime import datetime
from dotenv import load_dotenv

# config
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/health", methods=['GET'])
def health():
    return {
        "service": "Melo AI API",
        "version": "1.0.0",
        "status": "running",
        "url": "http://127.0.0.1:5000",
        "timestamp": datetime.now()
    }, 200


# entry point
if __name__ == "__main__":
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug)
