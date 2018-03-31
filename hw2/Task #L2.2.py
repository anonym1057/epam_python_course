def str2num(str):
    num_str = 0;
    for ch in str:
        # определение количества цифр в числе
        num = ord(ch)
        k = 0;
        while (num != 0):
            k = k + 1
            num = num // 10
        # складываем
        num_str = num_str * 10 ** (k) + ord(ch)
    return num_str
