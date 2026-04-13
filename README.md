# python-portfolio

![CI](https://github.com/mmb28g59j6-boop/python-portfolio/actions/workflows/ci.yml/badge.svg)

A small, ready-to-show Python portfolio repo with three starter projects and basic CI.

## What's included
- **CLI** calculator (`portfolio/cli.py`) using `argparse`
- **String manipulation** utilities (`portfolio/textops.py`) for whitespace cleanup, word counts, and reversing words
- **REST API** using FastAPI (`portfolio/api.py`)
- **Tests** in `tests/` with `pytest`
- **Linting** with `ruff` and GitHub Actions CI (`.github/workflows/ci.yml`) that runs on push/pull request

## Setup
Create a virtual environment and install the tools used by the repo:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -U pip
pip install fastapi uvicorn pytest ruff
```

## Run linting and tests

```bash
ruff check .
pytest
```

## Project 1: CLI calculator
Run the CLI with `python -m` and subcommands:

```bash
python -m portfolio.cli add 2 3
python -m portfolio.cli mul 4 5
```

## Project 2: String manipulation helpers
Import `textops` and call the helpers:

```python
from portfolio import textops

print(textops.normalize_whitespace("a\n b\t c"))
print(textops.reverse_words("one two three"))
print(textops.word_frequencies("a b a"))
```

## Project 3: FastAPI REST API
Start the API locally with uvicorn:

```bash
uvicorn portfolio.api:app --reload
```

Endpoints:
- `GET /ping`
- `POST /echo` with JSON `{"text": "..."}`
- `POST /add` with JSON `{"left": number, "right": number}`

## Repository layout
- `.github/workflows/ci.yml`: CI workflow
- `portfolio/`: project code
- `tests/`: pytest suite
