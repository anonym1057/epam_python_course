#Тask L1.1 - FizzBuzz
for i in range(1, 101):
    if i % 3 != 0 and i % 5 != 0:
        print(i)
        continue

    if i % 3 == 0:
        print("Fizz", end='')
    if i % 5 == 0:
        print("Buzz", end='')
    print('')