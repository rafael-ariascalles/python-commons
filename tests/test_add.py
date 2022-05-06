from src.add import add
import numpy as np

def test_add():
    assert add(1) == 101

def test_vector():
    result = add(np.array([1,3])) == np.array([101,103])
    assert result.all()

def test_concatenation():
    result = add("Python","Module") == "PythonModule"
    assert result

def test_two_vectors():
    result = add(np.array([1,2,3]),[1,0,0]) == np.array([2,2,3])
    assert result.all()