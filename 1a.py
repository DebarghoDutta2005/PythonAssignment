import math
def triangle_area(a, b, c):
  
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area
def triangle_perimeter(a, b, c):
    return a + b + c
def rectangle_area(length, width):
    return length * width
def rectangle_perimeter(length, width):
    return 2 * (length + width)
def circle_area(radius):
    return math.pi * radius ** 2
def circle_perimeter(radius):
    return 2 * math.pi * radius
def main():
    while True:
        print("\nChoose a shape:")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            a = float(input("Enter side a of the triangle: "))
            b = float(input("Enter side b of the triangle: "))
            c = float(input("Enter side c of the triangle: "))
            print("Area of Triangle:", triangle_area(a, b, c))
            print("Perimeter of Triangle:", triangle_perimeter(a, b, c))
        elif choice == '2':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Area of Rectangle:", rectangle_area(length, width))
            print("Perimeter of Rectangle:", rectangle_perimeter(length, width))

        elif choice == '3':
            radius = float(input("Enter the radius of the circle: "))
            print("Area of Circle:", circle_area(radius))
            print("Perimeter (Circumference) of Circle:", circle_perimeter(radius))
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
main()
