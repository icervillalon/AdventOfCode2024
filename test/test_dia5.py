import pytest
import dia5 as script

# Correct answer for exercise 5: 4959
def test_answer():
    result = script.ex_5("data/5.txt")
    assert result == 4959, f"Expected  result for test data -> 4959, received -> {result}"