# main.py

# Import all three functions from utils.py
from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        # Prompt user for a number
        num = float(input("Enter a number: "))
        
        # Calculate results using imported functions
        squared = square(num)
        even_check = is_even(num)
        fahrenheit = celsius_to_fahrenheit(num)
        
        # Display results
        print(f"\nResults for {num}:")
        print(f"Square: {squared}")
        print(f"Even or Odd: {'Even' if even_check else 'Odd'}")
        print(f"Fahrenheit equivalent: {fahrenheit:.2f}°F")
        
    except ValueError:
        print("Error: Please enter a valid number.")
if __name__== "__main__":
    main()
