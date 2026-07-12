"""Command line entry point for the example package."""

from python_compilation.core import compile_message


def main() -> None:
    """Print the template status message."""
    print(compile_message())


if __name__ == "__main__":
    main()

