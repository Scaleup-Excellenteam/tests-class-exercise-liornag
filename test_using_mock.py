import pytest
from unittest.mock import Mock, patch, MagicMock
import my_class_mock_example

# Basic mock example
def test_basic_mock_example():
    mock = Mock()
    mock.some_method.return_value = 42

    result = mock.some_method(10)
    assert result == 42, f"Expected 42 but got {result}"
    print(f"Basic mock example result: {result}")  # Should print 42

# Mocking methods in a class
def test_mock_method_example():
    mock_dependency = Mock()
    mock_dependency.some_method.return_value = 42

    obj = my_class_mock_example.MyClass(mock_dependency)
    #obj = my_class_mock_example.MyClass(my_class_mock_example.Dependency)
    result = obj.my_method(10)
    assert result == 42, f"Expected 42 but got {result}"
    print(f"Mock method example result: {result}")  # Should print 42

# Patching an object
def test_patch_example():
    # Example with differnt import
    print("a")
    # my_class_mock_example.MyClass = Mock()
    with patch('my_class_mock_example.MyClass') as MockClass:
        instance = MockClass.return_value
        instance.my_method.return_value = 42

        obj = my_class_mock_example.MyClass(None)
        result = obj.my_method(10)
        assert result == 42, f"Expected 42 but got {result}"
        print(f"Patch example result: {result}")  # Should print 42

