import math

def triangle_area_perimeter():
    a = float(input("Enter side a of the triangle: "))
    b = float(input("Enter side b of the triangle: "))
    c = float(input("Enter side c of the triangle: "))
    s = (a + b + c) / 2 
    try:
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print(f"Area of triangle: {area:.2f}")
        print(f"Perimeter of triangle: {perimeter:.2f}")
    except ValueError:
        print("Invalid triangle sides entered!")

def rectangle_area_perimeter():
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    area = length * width
    perimeter = 2 * (length + width)
    print(f"Area of rectangle: {area:.2f}")
    print(f"Perimeter of rectangle: {perimeter:.2f}")

def circle_area_perimeter():
    radius = float(input("Enter radius of circle: "))
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    print(f"Area of circle: {area:.2f}")
    print(f"Circumference of circle: {perimeter:.2f}")

def main():
    while True:
        print("\nChoose a shape:")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            triangle_area_perimeter()
        elif choice == '2':
            rectangle_area_perimeter()
        elif choice == '3':
            circle_area_perimeter()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


main()

import socket 
import time
import tracemalloc
# Start memory and time tracking 
tracemalloc.start()
start_time = time.time() 
# Get the local IP address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
# Perform any task (example: printing the IP address) 
print(f"IP Address: {ip_address}")
# End time and memory tracking 
end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory() 
tracemalloc.stop()
# Calculate time taken and memory used 
time_taken = end_time - start_time
memory_used = current_memory / 1024 # Convert to KB 
peak_memory_used = peak_memory / 1024 # Convert to KB 
# Display results
print(f"Time Taken: {time_taken:.6f} seconds") 
print(f"Current Memory Used: {memory_used:.2f} KB")
print(f"Peak Memory Used: {peak_memory_used:.2f} KB")
