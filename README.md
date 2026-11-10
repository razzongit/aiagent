# AI Agent

A from-scratch AI coding agent that runs in your terminal. Give it a task in plain English and it will plan, read your code, write files, and run Python — looping autonomously until the job is done.

Built as the final project for [Boot.dev's "Build an AI Agent in Python" course](https://www.boot.dev/courses/build-ai-agent-python).

## What It Does

The agent uses LLM function calling to interact with the filesystem through four tools:

| Tool | What it does |
|------|--------------|
| `get_files_info` | Lists files in a directory with sizes |
| `get_file_content` | Reads a file's contents |
| `write_file` | Creates or overwrites files |
| `run_python_file` | Executes Python files with optional arguments |

Every tool is sandboxed to the working directory — path traversal outside it is rejected. The agent can chain these tools across up to 20 iterations to complete multi-step tasks, e.g.:

> "fix the bug in the calculator project and then run its tests"

## Getting Started

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
# 1. Clone and install dependencies
git clone https://github.com/razzongit/aiagent.git
cd aiagent
uv sync

# 2. Add your OpenRouter API key to a .env file
echo "OPENROUTER_API_KEY=your-key-here" > .env
```

Get a free key at [openrouter.ai](https://openrouter.ai/keys).

## Usage

```bash
uv run main.py "your prompt here"
uv run main.py "explain the calculator pkg directory" --verbose
```

- `user_prompt` (required) — the task for the agent
- `--verbose` — shows prompts, token usage, and each tool call + result

### Example

```bash
$ uv run main.py "use the calculator project to evaluate (3 + 7) * 12 / 4 - 8" --verbose
```

The agent will inspect `calculator/`, write a small driver script, execute it, and report the result: `22.0`.

## How It Works

`main.py` runs an agent loop against an OpenAI-compatible API (OpenRouter):

1. Send the system prompt + user prompt to the model
2. If the model requests tool calls → execute them locally, append results, loop
3. If the model answers in plain text → print it and stop
4. Bail out after 20 iterations if the task never converges

The model runs at `temperature=0` for deterministic tool use.

## Project Structure

```
├── main.py                  # Entry point + agent loop
├── call_function.py         # Tool-call dispatcher
├── prompts.py               # System prompt
├── functions/               # Tool implementations + JSON schemas
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── calculator/              # Sample project the agent can operate on
├── test_*.py                # Quick check scripts for each tool
└── pyproject.toml
```

## Tests

Each `test_*.py` is a standalone script that exercises one tool, including the security checks (paths outside the working directory, invalid paths, etc.):

```bash
uv run test_get_files_info.py
uv run test_get_file_content.py
uv run test_write_file.py
uv run test_run_python_file.py
```

## Acknowledgements

Course and guidance by [Boot.dev](https://www.boot.dev). The `calculator/` directory ships with the course as a sample codebase for the agent to work on.
