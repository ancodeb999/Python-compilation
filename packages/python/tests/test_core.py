from python_compilation import compile_message


def test_compile_message_uses_default_language() -> None:
    assert compile_message() == "Python compilation workflow is ready."


def test_compile_message_normalizes_blank_language() -> None:
    assert compile_message("   ") == "Python compilation workflow is ready."


def test_compile_message_accepts_custom_language() -> None:
    assert compile_message("Rust") == "Rust compilation workflow is ready."

