import pytest
import sys
sys.path.append('src/.')
import utility


@pytest.mark.parametrize("original_string, find_text, replace_text, expected", [
    ('1a21f1af1jyr1', '1', '@', '@a2@f@af@jyr@'),
    ('123456712389', '123', '@', '@4567@89'),
    ('1231123', '11', '@', '123@23'),
    ('123111211113', '11', '@', '123@12@@3'),
    ('11123', '11', '1', '1123')
])
def test_replace_string(original_string, find_text, replace_text, expected):
    result = utility.replace_string(original_string, find_text, replace_text)
    assert(result) == expected

@pytest.mark.parametrize("original_text, front, back, expected", [
    ('123456789', None, None, '123456789'),
    ('123456789', 1, None, '23456789'),
    ('123456789', 0, 8, '12345678'),
    ('123456789', 4, 5, '5'),
    ('123456789', 5, 5, '')
])
def test_create_substring(original_text, front, back, expected):
    result = utility.create_substring(original_text, front, back)
    assert(result) == expected