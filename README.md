# TyperBot

## Overview

TyperBot is a powerful terminal-based chatbot built with Python, leveraging modern AI capabilities through LangChain and Anthropic's Claude. It provides an intuitive command-line interface for natural conversations while maintaining a clean, professional user experience with rich text formatting.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- Anthropic API key

### Installation

```bash
# Clone the repository
git clone https://github.com/joshszep/TyperBot.git
cd TyperBot

# Install dependencies using uv
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

## Key Features

- Interactive chat interface powered by Claude AI
- Clean and intuitive command-line interface using Typer
- Beautiful terminal formatting with Rich
- Conversation context management
- Command history support
- Secure configuration management
- Type-safe implementation with comprehensive test coverage

## Implementation Steps

- [x] Project Setup
  - [x] Initialize project structure
  - [x] Configure dependency management with uv
  - [x] Set up linting (ruff) and type checking (pyright)
  - [x] Create initial documentation

- [x] Core Development
  - [ ] Implement configuration management
  - [x] Create chat logic with LangChain
  - [x] Build CLI interface using Typer
  - [x] Add Rich text formatting
  - [ ] Implement conversation context handling

- [ ] Testing
  - [ ] Write unit tests for chat functionality
  - [ ] Write unit tests for CLI commands
  - [ ] Configure pytest and ensure >80% coverage

- [ ] Documentation and Polish
  - [ ] Complete API documentation
  - [ ] Add usage examples
  - [ ] Create contributing guidelines
  - [ ] Final testing and refinements
