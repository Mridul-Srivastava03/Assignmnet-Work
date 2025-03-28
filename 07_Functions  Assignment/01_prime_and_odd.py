def is_prime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num) and num % 2 == 1:
    print(f'{num} is odd prime number.')
elif is_prime(num) and num % 2 == 0:
    print(f'{num} is even prime number.')
else:
    print(f'{num} is composite.')
