def convert_celsius():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        print(f"{celsius}°C is {fahrenheit}°F and {kelvin}K.")
    except ValueError:
        print("Please enter a valid number.")
