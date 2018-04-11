if __name__ == '__main__':
    n = int(input("Введите количество пар: "))
    data = []
    for i in range(n):
        a = input(f"Пара {i} (через пробел): ").split()
        data += [a]

    for pair, i in zip(data, range(n)):
        print(f"\nПарa {i}")
        try:
            a = int(pair[0])
        except ValueError as e:
            print("invalid literal for int() with base 10", pair[0])
        except IndexError:
            print("list index out of range")
        else:
            try:
                b = int(pair[1])
            except ValueError:
                print("invalid literal for int() with base 10", pair[1])
            except IndexError:
                print("list index out of range")
            else:
                try:
                    print(a / b)
                except ZeroDivisionError as e:
                    print("integer division or modulo by zero")
