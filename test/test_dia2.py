import pytest
import dia2 as script

# Correct answer for exercise 2: 224
def test_answer():
    result = script.ex_2("data/2.txt")
    assert result == 224, f"Expected result for test data -> 224, received -> {result}"