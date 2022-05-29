#PROGRAM TO CHECK GIVEN STRING IS BINARY OR NOT

str = '0110101010111'
b = {'0','1'}
t = set(str)

if b == t or t == {'0'} or t == {'1'}:
    print("String is a binary string.")
else:
    print("String is not a binary string.")
