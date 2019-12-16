
def fibonacci(num):
    if num < 0:
        print("Incorrect input. Enter a positive value.")
    if num == 1:
        return 0
    if num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)

#Euclid's Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

#Compare two strings 
def compareTo(s1, s2):
    if s1 < s2:
        return -1
    elif s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])
