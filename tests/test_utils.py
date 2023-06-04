from src.utils import get_operations, encode_numbers
from src.data import get_data, sort_data


def test_get_operations(result_test_sort_data, result_test_get_operations):
    assert get_operations(result_test_sort_data) == result_test_get_operations


def test_encode_numbers(result_test_get_operations, result_test_encode_numbers):
    assert encode_numbers(result_test_get_operations) == result_test_encode_numbers
