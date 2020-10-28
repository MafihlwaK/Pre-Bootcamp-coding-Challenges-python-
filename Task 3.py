def my_number(no1, no2):
    if no1 == 65 or no2 == 65:
        return True
    elif no1 + no2 == 65:
        return True
    else:
        return False

print(my_number(45, 25))