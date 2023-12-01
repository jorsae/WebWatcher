import pytest
import sys
sys.path.append('src/.')
import utility


@pytest.mark.parametrize("original_string, find_text, replace_text, expected", [
    ('1a21f1af1jyr1', '1', '@', '@a2@f@af@jyr@'),
    ('123456712389', '123', '@', '@4567@89')
])
def test_replace_string(original_string, find_text, replace_text, expected):
    result = utility.replace_string(original_string, find_text, replace_text)
    assert(result) == expected