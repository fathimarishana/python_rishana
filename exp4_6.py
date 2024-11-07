area_of_square = lambda side:side*side
area_of_rectangle = lambda length,width:length *width
area_of_triangle = lambda base,height: 0.5 * base * height
side = float(input("enter the side length of the square:"))
length = float(input("enter the length of the rectangle:"))
width = float(input("enter the width of the rectangle:"))
base = float(input("enter the base of the triangle:"))
height = float(input("enter the height of the triangle:"))
square_area = area_of_square(side)
rectangle_area = area_of_rectangle(length,width)
triangle_area = area_of_triangle(base,height)
print(f"area of square:{square_area}")
print(f"area of rectangle:{rectangle_area}")
print(f"area of triangle:{triangle_area}")

