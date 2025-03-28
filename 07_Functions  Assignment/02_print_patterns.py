def odd_pattern(num):
    for i in range(num):
        for j in range(i+1):
            print("*", end=" ")
        print()

def even_pattern(num):
    for i in range(num):
        for j in range(num-i):
            print("*", end=" ")
        print()

num = int(input("Enter a value: "))
if num % 2 == 1:
    odd_pattern(num)
else:
    even_pattern(num)