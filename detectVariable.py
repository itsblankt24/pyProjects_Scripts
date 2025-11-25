#AI generated used to test what is being outputted by a function
def detect_output_type(value):
    """
    Detects and returns a human-friendly description of the value's data type.
    """

    # Basic types
    if isinstance(value, str):
        return "String"
    elif isinstance(value, int):
        return "Integer"
    elif isinstance(value, float):
        return "Float"
    elif isinstance(value, complex):
        return "Complex Number"
    elif isinstance(value, bool):
        return "Boolean"
    elif value is None:
        return "NoneType (Null Value)"

    # Sequence types
    elif isinstance(value, list):
        return "List (Sequence)"
    elif isinstance(value, tuple):
        return "Tuple (Immutable Sequence)"
    elif isinstance(value, set):
        return "Set (Unique Collection)"
    elif isinstance(value, frozenset):
        return "FrozenSet (Immutable Set)"

    # Mapping
    elif isinstance(value, dict):
        return "Dictionary (Key-Value Mapping)"

    # Binary data
    elif isinstance(value, bytes):
        return "Bytes (Binary Data)"
    elif isinstance(value, bytearray):
        return "ByteArray (Mutable Binary Data)"

    # Function or class
    elif callable(value):
        return "Function or Callable Object"

    # Catch-all for custom objects
    else:
        return f"Custom Object of type: {type(value).__name__}"
