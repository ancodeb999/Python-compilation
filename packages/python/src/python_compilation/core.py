"""Core example behavior for tests and builds."""


def compile_message(language: str = "Python") -> str:
    """Return a short status message for the template project."""
    normalized_language = language.strip() or "Python"
    return f"{normalized_language} compilation workflow is ready."

