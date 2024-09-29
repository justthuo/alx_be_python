# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.
    """
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.
    """
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
    """
    Main function to interact with the user and perform temperature conversions.
    """
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        else:
            raise ValueError("Invalid unit. Please enter C or F.")
    except ValueError as e:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()