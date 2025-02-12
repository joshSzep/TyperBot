# Default recipe to display all available commands
default:
    @just --list

# Install all dependencies including development ones
install:
    uv pip install -e ".[dev]"

# Run all code quality checks
check: format lint type-check test

# Format code using ruff
format:
    uv run ruff format .

# Check formatting without making changes
format-check:
    uv run ruff format --check .

# Run linting with ruff
lint:
    uv run ruff check .

# Fix auto-fixable lint issues
lint-fix:
    uv run ruff check --fix .

# Run type checking with pyright
type-check:
    uv run pyright .

# Run tests with pytest
test:
    uv run pytest

# Run tests with coverage report
test-cov:
    uv run pytest --cov=typerbot --cov-report=html
    @echo "Coverage report generated in htmlcov/index.html"

# Clean up Python cache files
clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
    find . -type f -name "*.pyo" -delete
    find . -type f -name "*.pyd" -delete
    find . -type d -name "*.egg-info" -exec rm -rf {} +
    find . -type d -name "*.egg" -exec rm -rf {} +
    find . -type d -name ".coverage" -delete
    find . -type d -name "htmlcov" -exec rm -rf {} +
    find . -type d -name ".pytest_cache" -exec rm -rf {} +
    find . -type d -name ".ruff_cache" -exec rm -rf {} +

# Watch for file changes and run tests
watch-test:
    find src tests -name "*.py" | entr -c uv run pytest

# Install pre-commit hooks
setup-hooks:
    cp {{justfile_directory()}}/hooks/pre-commit .git/hooks/
    chmod +x .git/hooks/pre-commit
