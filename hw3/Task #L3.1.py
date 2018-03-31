def str2num(str, num=0):
    if not str:
        return num
    else:
        # определение длины кода числа
        ch = str[0]
        num_ch = ord(ch)
        len_code_ch = 0
        while (num_ch != 0):
            len_code_ch += 1;
            num_ch = num_ch // 10
        # складываем
        num_str = num * 10 ** (len_code_ch) + ord(ch)
        return str2num(str[1:], num_str)


print(str2num('abcd'))
