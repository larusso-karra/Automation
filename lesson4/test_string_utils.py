import pytest
from lesson4.StringUtils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# Tests for capitilize method
def test_capitilize_positive(string_utils):
    assert string_utils.capitilize("skypro") == "Skypro"


def test_capitilize_negative_type_error(string_utils):
    with pytest.raises(TypeError):
        string_utils.capitilize(123)


# Tests for trim method
def test_trim_positive(string_utils):
    assert string_utils.trim("   skypro") == "skypro"


def test_trim_negative_attribute_error(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)


# Tests for to_list method
def test_to_list_positive(string_utils):
    assert string_utils.to_list("a,b,c,d") == ["a", "b", "c", "d"]


def test_to_list_negative_value_error(string_utils):
    with pytest.raises(ValueError):
        string_utils.to_list("", ",")


# Tests for contains method
def test_contains_positive_true(string_utils):
    assert string_utils.contains("SkyPro", "S") is True


def test_contains_positive_false(string_utils):
    assert string_utils.contains("SkyPro", "U") is False


# Tests for delete_symbol method
def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_negative_no_change(string_utils):
    assert string_utils.delete_symbol("SkyPro", "z") == "SkyPro"


# Tests for starts_with method
def test_starts_with_positive_true(string_utils):
    assert string_utils.starts_with("SkyPro", "S") is True


def test_starts_with_positive_false(string_utils):
    assert string_utils.starts_with("SkyPro", "P") is False


# Tests for end_with method
def test_end_with_positive_true(string_utils):
    assert string_utils.end_with("SkyPro", "o") is True


def test_end_with_positive_false(string_utils):
    assert string_utils.end_with("SkyPro", "y") is False


# Tests for is_empty method
def test_is_empty_positive_true_empty_string(string_utils):
    assert string_utils.is_empty("") is True


def test_is_empty_positive_true_whitespace_only(string_utils):
    assert string_utils.is_empty(" ") is True


def test_is_empty_negative_false_non_empty_string(string_utils):
    assert string_utils.is_empty("SkyPro") is False


# Tests for list_to_string method
def test_list_to_string_positive_valid_input(string_utils):
    assert string_utils.list_to_string([1, 2, 3, 4], ", ") == "1, 2, 3, 4"


def test_list_to_string_negative_type_error_joiner_none(string_utils):
    with pytest.raises(TypeError):
        string_utils.list_to_string([1, 2, 3, 4], None)