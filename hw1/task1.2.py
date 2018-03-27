#Task L1.2 - НОД
a = int(input("Enter 1 number: "))
b = int(input("Enter 2 number: "))
print(f"НОД({a},{b})=", end='')
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)