class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def compare_area(self,other):
        if self.area() > other.area():
            return " rectangle 1 is bigger!"
        elif self.area() < other.area():
            return "rectangle 2  is bigger!"
        else:
            return "both rectangle are the same size!"
print("enter details for rectangle 1:")
length1 = int(input("length:"))
breadth1 = int(input("breadth:"))
rect1 = rectangle(length1,breadth1)
print("\nenter details for rectangle 2:")
length2 = int(input("length:"))
breadth2 = int(input("breadth:"))
rect2 = rectangle(length2,breadth2)
print(f"\nrectangle 1 area:{rect1.area()} | perimeter:{rect1.perimeter()}")
print(f"rectangle 2 area:{rect2.area()} | perimeter:{rect2.perimeter()}")
print("\n comparison result:")
print(rect1.compare_area(rect2))
~                                
