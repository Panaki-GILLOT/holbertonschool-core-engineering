#!/usr/bin/env python3
"""
Entry point for the AI Study Guide Generator
"""
import asyncio
import sys

from google.genai import types

from google.adk.runners import InMemoryRunner

from agents.explainer_agent import explainer_agent
from tools.file_writer import save_markdown_file

APP_NAME = "ai_study_guide_generator"
USER_ID = "cli_user"
OUTPUT_PATH = "output/study_guide.md"


async def run_explainer(topic: str) -> str:
    """Runs the explainer agent on a topic and returns its Markdown response"""
    runner = InMemoryRunner(agent=explainer_agent, app_name=APP_NAME)
    session = await runner.session_service.create_session(
        app_name=APP_NAME, user_id=USER_ID
    )
    message = types.Content(role="user", parts=[types.Part(text=topic)])

    response_text = ""
    async for event in runner.run_async(
        user_id=USER_ID, session_id=session.id, new_message=message
    ):
        if event.is_final_response() and event.content and event.content.parts:
            response_text = "".join(
                part.text for part in event.content.parts if part.text
            )
    return response_text


async def generate_study_guide(topic: str) -> str:
    """Generates a study guide for topic and saves it to OUTPUT_PATH"""
    content = await run_explainer(topic)
    return save_markdown_file(OUTPUT_PATH, content)


def main():
    """Runs the study guide generation workflow from the command line"""
    topic = " ".join(sys.argv[1:]).strip()
    if not topic:
        topic = input("Enter a programming topic: ").strip()

    saved_path = asyncio.run(generate_study_guide(topic))
    print(f"Study guide saved to {saved_path}")


if __name__ == "__main__":
    main()
