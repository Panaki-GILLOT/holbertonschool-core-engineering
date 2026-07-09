# AI Study Guide Generator

A small multi-agent system that receives a programming topic and generates a
Markdown study guide (explanation, key concepts, example, practice exercise,
common mistakes, review comments, and summary).

Built with [Google ADK](https://google.github.io/adk-docs/) for agent
orchestration, [LiteLLM](https://docs.litellm.ai/) to connect to a model
provider, and [Ollama](https://ollama.com/) to run a small model locally by
default.

## Project Structure

```
ai-agents-intro/
├── agents/         # Agent definitions (one responsibility per agent)
├── tools/          # Deterministic Python tools used by agents
├── output/         # Generated Markdown study guides
├── data/           # Example/reference data
├── .env.example    # Template for local environment configuration
├── .gitignore
├── requirements.txt
├── README.md
└── main.py         # Entry point
```

## Status

This repository is being built incrementally. Setup, usage instructions,
examples, and a reflection will be added here as the agents and tools are
implemented in later steps.
