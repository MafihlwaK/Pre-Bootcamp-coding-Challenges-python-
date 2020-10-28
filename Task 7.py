def convert_temp(num = None, scale_temp = None):
    if num == "F":
        return 'C', (scale_temp - 32.0) *(5.0 / 9.0)
    elif num == "C":
        return 'F', (scale_temp * (9.0 / 5.0)) + 32.0
    else:
        print("Have to be (F) or (C)!")
        return

num = input("Select (F) or (C): ")
scale_temp = int(input("Temperature: "))
m, k = convert_temp(num, scale_temp)
print(scale_temp, "degrees", num, "is", k, "degrees", m)
