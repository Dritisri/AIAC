from Task5 import convert_date_format
import pytest

def test_valid_date():
    result1 = convert_date_format("1999-01-24")
    result2 = convert_date_format("2000-12-31")
    print(result1)
    print(result2)
    assert result1 == "24-01-1999"
    assert result2 == "31-12-2000"

def test_invalid_format_missing_parts():
    with pytest.raises(ValueError):
        convert_date_format("2000-12")
    with pytest.raises(ValueError):
        convert_date_format("2000")

def test_invalid_format_extra_parts():
    with pytest.raises(ValueError):
        convert_date_format("2000-12-31-01")

def test_invalid_format_wrong_separator():
    with pytest.raises(ValueError):
        convert_date_format("2000/12/05")