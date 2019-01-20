def test_multiply_function():
    from tdd_example import multiply_two

    assert multiply_two(1, 4) == 4
    assert multiply_two(0, 3) == 0

def test_multiply_function_no_strings():
    """Test that attempting to use the multiply function with
    a string as an argument raises TypeError"""
    from tdd_example import multiply_two

    import pytest
    with pytest.raises(TypeError):
        multiply_two("abc", 2)
