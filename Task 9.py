sum_of_multiple = []
i = 1
while i < 1000:
    if i % 3 == 0:
        sum_of_multiple.append(i)
    elif i % 5 == 0:
        sum_of_multiple.append(i)
    i = i + 1
print(sum_of_multiple)
sums = 0
for i in sum_of_multiple:
    sums = sums + i
    print(sums)