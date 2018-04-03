def str2num(string, num=0):
    """Translates a string into a number consisting of character codes
    if parametr 'string' is not а string, function will translate into a string
    abcd ->  979899100
    .... ->  46464646
    """
    if not string:
        if num==0:
            print("string is empty")
        return num
    else:
        if num==0:
            string=str(string)
        # определение длины кода числа
        ch = string[0]
        num_ch = ord(ch)
        len_code_ch = 0
        while (num_ch != 0):
            len_code_ch += 1;
            num_ch = num_ch // 10
        # складываем
        num_str = num * 10 ** (len_code_ch) + ord(ch)
        return str2num(string[1:], num_str)


if __name__ == '__main__':
    print("abcd -> ", str2num(""))
    print(".... -> ", str2num("...."))
