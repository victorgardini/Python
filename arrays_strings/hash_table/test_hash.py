import pytest

from hash import HashTable


@pytest.fixture
def hash_table():
    return HashTable()


def test_get_empty_hash_table_index(hash_table):
    with pytest.raises(KeyError):
        var = hash_table[0]


@pytest.mark.parametrize("key, value", [(0, 'foo'), (1, 'bar'), (2, 'baz')])
def test_set_on_an_empty_hash_table_index(hash_table, key, value):
    hash_table[key] = value
    assert hash_table[key] == value


def test_set_on_a_non_empty_hash_table_index(hash_table):
    hash_table[0] = 'foo'
    hash_table[10] = 'foo2'
    assert hash_table[0] == 'foo'
    assert hash_table[10] == 'foo2'


@pytest.mark.parametrize("key, value", [(10, 'foo'), (10, 'foo2')])
def test_set_on_a_non_empty_hash_table_index_with_same_key(hash_table, key, value):
    hash_table[key] = value
    assert hash_table[key] == value


def test_delete_on_a_non_empty_hash_table_index(hash_table):
    hash_table[0] = 'foo'
    hash_table[10] = 'foo2'
    del hash_table[0]
    del hash_table[10]
    with pytest.raises(KeyError):
        var = hash_table[0]
    with pytest.raises(KeyError):
        var = hash_table[10]


def test_delete_a_key_that_does_not_exist(hash_table):
    with pytest.raises(KeyError):
        del hash_table[0]
