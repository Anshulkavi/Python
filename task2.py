import math

num = float(input("Enter a number: "))

if num < 0:
    print("Square root of negative number is not real.")
else:
    result = math.sqrt(num)
    print("Square root:", result)

if num <= 0:
    print("Logarithm undefined for 0 or negative numbers.")
else:
    result1 = math.log(num)
    print("Logarithm (base e):", result1)

# Sine in degrees
sine_value = math.sin(math.radians(num))
print(f"Sine of {num}° is: {sine_value}")
