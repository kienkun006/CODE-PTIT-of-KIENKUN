import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n > 1


for i in range(int(input())):
    n = input()
    sum = 0
    for j in n:
        sum += ord(j) - ord('0')
    if isPrime(sum):
        print("YES")
    else:
        print("NO")