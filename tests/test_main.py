from src.main import print_operation


def test_print_operation(result_test_encode_numbers, result_test_print_operation):
    assert print_operation(result_test_encode_numbers) == result_test_print_operation
