"""
Script Name : utils.py
Description : Utilities for prompt and helper functions for questions parsing
Author      : @tonybnya
"""

import json
import re

# starter prompt
PROMPT = """You are an expert HR interviewer and talent acquisition specialist.

Your task: generate exactly 3 thoughtful, role-specific interview questions for the position of '{job_title}'.

"""
