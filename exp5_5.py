from rectangle import area as rect_area, perimeter as rect_perimeter
from circle import area as circ_area,perimeter as circ_perimeter
from cuboid import area as cuboid_area,perimeter as cuboid_perimeter
from sphere import area as sphere_area,perimeter as sphere_perimeter
def main():
    print("choose a shape to calculate:")
    print("1.rectangle")
    print("2.circle")
    print("3.cuboid")
    print("4.sphere")
    choice = int(input("enter your choice (1-4):"))
    if choice == 1:
        length = float(input("enter the length of the rectangle:"))
        width = float(input("enter the width of the rectangle:"))
        print("rectangle area:",rect_area(length, width))
        print("rectangle perimeter:",rect_perimeter(length, width))
    elif choice == 2:
        radius = float(input("enter the radius ofthe circle:"))
        print("circle area:",circ_area(radius))
        print("circle perimeter:",circ_perimeter (radius))
    elif choice == 3:
        length = float(input("enter the length of the cuboid:"))
        width = float(input("enter the width of the cuboid:"))
        height = float(input("enter the height of the cuboid:"))
        print("cuboid area:",cuboid_area(length,width,height))
        print("cuboid perimeter:",cuboid_perimeter(length,width,height))
    elif choice == 4:
        radius = float(input("enter the radius of the sphere:"))
        print("sphere area:",sphere_area(radius))
        print("sphere perimeter(circumference):",sphere_perimeter(radius))
    else:
        print("invalid choice! please select a valid option.")
if __name__ == "__main__":
    main()

