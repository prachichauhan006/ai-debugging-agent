import pytest
from app.utils.code_parser import parse_traceback

def test_index_error():
    tb = "File 'test.py', line 2, in <module>\nIndexError: list index out of range"
    result = parse_traceback(tb)
    assert result["error_type"] == "IndexError"
    assert result["line_number"] == 2
    assert result["file_name"] == "test.py"

def test_zero_division_error():
    tb = "File 'main.py', line 5, in divide\nZeroDivisionError: division by zero"
    result = parse_traceback(tb)
    assert result["error_type"] == "ZeroDivisionError"
    assert result["line_number"] == 5

def test_no_traceback():
    result = parse_traceback("")
    assert result["error_type"] is None
    assert result["line_number"] is None