from permutations import max_permutations


def test_permutations():
    assert max_permutations("a") == ["a"]
    assert max_permutations("ab") == ["ab", "ba"]
    assert max_permutations("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"]
    assert max_permutations("AABC") == [
        "AABC", "AACB", "ABAC", "ABCA", "ACAB", "ACBA", "BAAC", "BACA", "BCAA", "CAAB", "CABA", "CBAA"
    ]
