# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    # Prompt the user to enter a temperature and specify whether it's in Celsius or Fahrenheit
    temperature = input("Enter the temperature to convert: ")
    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == 'C':
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {result:.1f}°F")
    elif unit == 'F':
        result = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {result:.1f}°C")
    else:
        print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
