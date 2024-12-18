import pytest
import dia1 as script

# Correct answer for exercise 1: 2031679
def test_answer():
    result = script.ex_1("data/1.txt")
    assert result == 2031679, f"Expected result for test data -> 2031679, received -> {result}"