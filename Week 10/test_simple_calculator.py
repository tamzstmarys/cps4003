import simple_calculator as calculator


def test_addition():
    result = calculator.add(20, 30)
    assert result == 50, f"Addition failed. Expected 50. Got {result}."