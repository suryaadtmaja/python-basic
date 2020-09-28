import sys

x = int(input('x: '))
y = int(input('y: '))

try:
  result = round(x / y)
except ZeroDivisionError:
  print("Error: Can't divided by zero")
  sys.exit(1)

print(f'{x} divided by {y} is {result}')