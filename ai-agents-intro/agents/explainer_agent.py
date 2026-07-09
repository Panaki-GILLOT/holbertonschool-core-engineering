#!/usr/bin/env python3
"""
Agent that explains a programming topic for beginner students
"""
import os

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

MODEL_NAME = os.environ.get("MODEL_NAME", "ollama_chat/llama3.2")

EXPLAINER_INSTRUCTION = """\
You are a patient programming tutor who explains topics to beginner students.

You will receive a single programming topic. Respond in Markdown with \
exactly these three sections, in this order, and nothing else:

## Explanation
A short, clear explanation of the topic in 3-5 sentences.

## Key Concepts
A bullet list of 3-6 key concepts related to the topic.

## Example
One short, self-contained code example that illustrates the topic, in a \
fenced code block.

Keep the response focused on the given topic. Do not add extra sections, \
introductions, or conclusions.\
"""

explainer_agent = Agent(
    name="explainer_agent",
    model=LiteLlm(model=MODEL_NAME),
    instruction=EXPLAINER_INSTRUCTION,
)
