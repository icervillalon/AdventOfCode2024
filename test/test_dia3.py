import pytest
import dia3 as script

# Correct answer for exercise 3: 159833790
def test_answer():
    result = script.ex_3("data/3.txt")
    assert result == 159833790, f"Expected  result for test data -> 159833790, received -> {result}"