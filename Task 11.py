def common_characters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    s1 = set(str1)
    s2 = set(str2)
    first = s1 & s2
    print(first) 



common_characters()