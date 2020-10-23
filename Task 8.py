def number_convert(num):
    num = num % (24 * 60)
    hour = num // 60
    num %= 60
    minutes = num // 1
    num %= 60
    return "%02d : %02d" % (hour, minutes)
n = 133
print(number_convert(n))

    