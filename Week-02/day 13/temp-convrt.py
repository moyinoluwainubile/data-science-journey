def farenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

# Example usage:
f_temp = 100
c_temp = farenheit_to_celsius(f_temp)
print(f"{f_temp}°F is equal to {c_temp:.2f}°C")