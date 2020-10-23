def triangle_area(a, b, c):
    perimeter = a + b + c
    s = perimeter / 2
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    return area
side1 = float(input("Enter the length of the first side: ") )
side2 = float(input("Enter the length of the second side: ") )
side3 = float(input("Enter the length of the third side: ") )

area = triangle_area(side1, side2, side3)

print("The area of a triangle is: " + str(area))
