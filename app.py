"""
Script Name : app.py
Description : Melo AI main application
Author      : @tonybnya
"""

import os
import logging
from flask import Flask, jsonify, render_template, request
from google import genai
from dotenv import load_dotenv
from utils import build_questions_prompt, parse_questions

# config
load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# init the Gemini client once at startup (not per request)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise EnvironmentError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=GEMINI_API_KEY)
GEMINI_MODEL = "gemini-3-flash-preview"


@app.route("/", methods=['GET'])
def index():
    """
    Serve the single-page application.
    """
    return render_template("index.html")


@app.route("/health", methods=['GET'])
def health():
    """
    API health checker.
    """
    return {
        "service": "Melo AI API",
        "version": "1.0.0",
        "status": "running",
        "url": "http://127.0.0.1:5000",
        "timestamp": datetime.now()
    }, 200


@app.route("/api/questions", methods=['POST'])
def generate_questions():
    """
    POST /api/questions
    Body: { "job_title": "Customer Success Manager" }
    Returns: { "questions": ["Q1", "Q2", "Q3"] }
    """
    data = request.get_json(silent=True)

    # input validation
    if not data or "job_title" not in data:
        return jsonify({"error": "Missing required field: job_title"}), 400

    job_title = data["job_title"].strip()
    if not job_title:
        return jsonify({"error": "job_title must not be empty"}), 400

    if len(job_title) > 100:
        return jsonify({"error": "job_title must be 100 characters or fewer"}), 400

    logger.info("Generating questions for role: %s", job_title)

    # call Gemini API
    try:
        prompt =  build_questions_prompt(job_title)
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        raw_text = response.text
    except Exception:
        logger.exception("Gemini API call failed")
        return jsonify({"error": "AI service unavailable. Please try again later."}), 502

    # parse response
    try:
        questions = parse_questions(raw_text)
    except Exception:
        logger.exception("Failed to parse model response: %s", raw_text)
        return jsonify({"error": "Unexpected response format from Gemini AI. Please retry."}), 500

    return jsonify({"questions": questions}), 200


# entry point
if __name__ == "__main__":
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=5000, debug=debug)
