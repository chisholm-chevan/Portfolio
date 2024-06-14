print("Enter a number")
x = int(input())
print("Enter a number")
y = int(input())
num = range(x, y+1)
prime = []
not_prime = []

for i in range(x, y+1):
    for a in range(2, i):
        if i%a == 0:
            not_prime.append(i)
            break
    else:
        prime.append(i)

print(prime)
prime_sum = sum(prime)
print("Sum of prime numbers in a range of 5 to 10 is:", prime_sum)
