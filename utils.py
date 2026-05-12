"""
Script Name : utils.py
Description : Utilities for prompt and helper functions for questions parsing
Author      : @tonybnya
"""

import json
import re

# starter prompt
PROMPT = """You are an expert HR interviewer and talent acquisition specialist.

Your task: generate exactly 3 thoughtful, role-specific interview questions for the position of "{job_title}".

Guidelines:
- Each question should be probe a different dimension: technical/functional
  skills, situational judgment, and cultural/behavioural fit.
- Questions must be specific to the "{job_title}" role -- avoid generic
  question that could apply to any job.
- Keep each question concise but substantive (1-2 sentences max).

Output format -- return ONLY a JSON array of exactly 3 strings, no preamble, no markdown fences:
["Question 1", "Question 2", "Question 3"]
"""


def build_questions_prompt(job_title: str) -> str:
    """
    Interpolate the job title into the prompt template.
    """
    return PROMPT.format(job_title=job_title)
