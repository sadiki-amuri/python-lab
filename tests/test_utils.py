from src.utils import square, is_even, celsius_to_fahrenheit

def test_square ():
        assert square(4) == 16

def test_is_even():
        assert is_even(2) == True
        assert is_even(3) == False
        
def test_celsius():
            assert celsius_to_fahrenheit(0) ==32