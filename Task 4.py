def my_number(no1, no2):
    if "3" in str(no1 + no2) == 3 and (no1 == 3 or no2 == 3):
        return True
    else :
        return False
    
print(my_number(2, 11))