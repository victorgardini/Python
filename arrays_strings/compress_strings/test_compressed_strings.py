import pytest
from compres import CompressedString


@pytest.mark.parametrize("data, expected", [
    ("AABBCC", "AABBCC"),
    ("AAABCCDDDDE", "A3BC2D4E"),
    ("BAAACCDDDD", "BA3C2D4"),
    ("AAABAACCDDDD", "A3BA2C2D4"),
    ("A", "A"),
    ("", ""),
])
def test_compress_string(string, expected):
    assert CompressedString(string).string == expected


@pytest.mark.parametrize("data, expected", [
    ("A3BC2D4E", "AAABCCDDDDE"),
    ("BA3C2D4", "BAAACCDDDD"),
    ("A3BA2C2D4", "AAABAACCDDDD"),
    ("A", "A"),
    ("", ""),
])
def test_uncompress_string(string, expected):
    assert CompressedString.uncompress_string(string) == expected
