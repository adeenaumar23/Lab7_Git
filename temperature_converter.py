# Temperature Converter
# A small program for practising Git and GitHub.
# It converts a temperature from Celsius to Fahrenheit.
#
# How to run it:  python temperature_converter.py

# Ask the user for a temperature in Celsius
celsius = float(input("Temperature in Celsius: "))

# Validate temperature
if celsius < -273.15:
    print("Error: Temperature cannot be below absolute zero.")
else:
    fahrenheit = celsius * 9 / 5 + 32
    print("Temperature in Fahrenheit:", fahrenheit