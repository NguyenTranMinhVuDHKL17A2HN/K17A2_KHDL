Binary of x 0b1111 , Binary of y 0b1100
x & y =  0b1100
x | y =  0b1111
x ^ y =  0b11
~x =  -0b10000
x << 2 =  0b111100
y >> 2 =  0b11
x = 15
y = 12

print('Binary of x', bin(x), ', Binary of y', bin(y))
# Output:
# Binary of x 1111, Binary of y 1100

print('x & y = ', bin(x & y))
# Output:
# x & y = 1100

print('x | y = ', bin(x | y))
# Output:
# x | y = 1111

print('x ^ y = ', bin(x ^ y))
# Output:
# x ^ y = 0011

print('~x = ', bin(~x))
# Output:
# ~x = 0000

print('x << 2 = ', bin(x << 2))
# Output:
# x << 2 = 11100

print('y >> 2 = ', bin(y >> 2))
# Output:
# y >> 2 = 0011