import struct
import math
import numpy as np
import sympy
import decimal as d

#Question 1
binary_number = "0100000001111110101110010000000000000000000000000000000000000000"
decimal_number = struct.unpack('>d', int(binary_number, 2).to_bytes(8, byteorder='big'))
print(decimal_number[0])

decimal_number = decimal_number[0]
original_decimal = decimal_number

# convert the decimal to a string
original_decimal_str = str(original_decimal)

# split the string by '.' to separate the whole number and decimal parts
whole, decimal = original_decimal_str.split(".")

# move the decimal point by the number of digits in the whole number
new_decimal = "0." + whole + decimal[:6]

# add an exponent to indicate the position of the decimal point
normalized_decimal = new_decimal + "*10^" + str(len(whole))

# exponent variable
exponent = str(len(whole))
exponent = int(exponent)
exp_var = 10**(exponent)

#Turning new_decimal into float from string
new_decimal = float(new_decimal)

# Three-digit chopping 
chopped_decimal = float(str(new_decimal)[:-4])
chopped_decimal = chopped_decimal * exp_var
print()
print(chopped_decimal)

# Three-digit rounding arithmeticmat
new_decimal = new_decimal + 0.0005

rounded_decimal = round(new_decimal, 3)
rounded_decimal = rounded_decimal * exp_var

print()
print(rounded_decimal)

#Absolute Error
exact_value = decimal_number #491.5625
rounded_value = rounded_decimal #492.0
absolute_error = abs(exact_value - rounded_value)

print()
print(absolute_error)

#Relative Error
absolute_error = d.Decimal(absolute_error)
exact_value = d.Decimal(exact_value)

relative_error = absolute_error / exact_value
print(relative_error)
#Question 5
#Solve for n
n = sympy.Symbol('n')
equation = 1/(n+1)**3 < 10**-4
solution = sympy.solve(equation)

solution_string = str(solution)
solution_list = solution_string.split()
#Isolates theh value n < 20.5443469003188 (number of iterations needed)
iterations = solution_list[solution_list.index('(20.5443469003188')]
iterations = iterations[1:]

#turn into number
iterations = float(iterations)

#tound up
iterations = math.ceil(iterations)
print()
print(iterations)

#Question 6 (a)
def f(x):
    return x**3 + 4*x**2 - 10

a = -4
b = 7
tolerance = 10**-4
iterations = 0

while abs(b-a) > tolerance:
    c = (a + b) / 2
    if f(c) == 0:
        break
    elif f(c) * f(a) < 0:
        b = c
    else:
        a = c
    iterations += 1

root = c
print()
print(iterations)

#Quesion 6 (b)
x = sympy.Symbol('x')
f = x**3 + 4*x**2 - 10
f_prime = f.diff(x)

a = -4
b = 7
tolerance_nr = 10**-4
iterations_nr = 0
x0 = 6

while True:
    x1 = x0 - f.evalf(subs={x: x0})/f_prime.evalf(subs={x: x0})
    iterations_nr += 1
    if abs(x1 - x0) < tolerance_nr:
        break
    x0 = x1

print()
print(iterations_nr)

