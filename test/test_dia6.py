import pytest
import dia6 as script

# Correct answer for exercise 6: 4665
def test_answer():
    result = script.ex_6("data/6.txt")
    assert result == 4665, f"Expected  result for test data -> 4665, received -> {result}"