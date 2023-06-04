from src.data import get_data, sort_data
import os.path


def test_get_data(result_test_get_data):
    assert get_data(os.path.join(os.path.dirname(__file__), 'test_operations.json')) == result_test_get_data


def test_sort_data(data_for_sort, result_test_sort_data):
    assert sort_data(data_for_sort) == result_test_sort_data
