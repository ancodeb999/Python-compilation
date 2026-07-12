# Python Compilation

Open source GitHub Actions template for compiling, testing, and validating a Python project. The repository is organized so more languages can be added later without moving the Python example.

## Repository Layout

```text
.
├── .github/workflows/python.yml
└── packages/
    └── python/
        ├── pyproject.toml
        ├── src/python_compilation/
        └── tests/
```

Each language should live in `packages/<language>/` and have its own workflow job or workflow file. For example, a future Rust project can be added under `packages/rust/` while keeping the Python workflow unchanged.

## Python CI

The Python workflow runs on every push and pull request. It checks Python `3.10`, `3.11`, `3.12`, and `3.13`.

The workflow validates:

- dependency installation with `uv`
- linting with `ruff`
- tests with `pytest`
- source and wheel builds with `uv build`

## Local Development

Install `uv`, then run the Python checks from `packages/python`:

```powershell
cd packages/python
uv sync --all-extras --dev
uv run ruff check .
uv run pytest
uv build
```

The package exposes a small example function and CLI so the template has real code to lint, test, and build.

## Adding Another Language

1. Create a new directory such as `packages/rust` or `packages/node`.
2. Add that language's build and test files inside the new directory.
3. Add a dedicated GitHub Actions job or workflow that sets its working directory to the new package.
4. Keep shared repository policy in the root README and language-specific commands inside each package.

