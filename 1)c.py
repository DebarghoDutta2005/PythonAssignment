import cmath

def find_quadratic_roots(a, b, c):

    if a == 0:

        if b == 0:
            return ("This is not an equation (a=0, b=0).",)
        else:
            root = -c / b
            return (f"This is a linear equation. The root is: {root}",)

    discriminant = (b**2) - 4*(a*c)

    if discriminant > 0:
   
        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return (f"Two distinct real roots: Root 1 = {root1:.4f}, Root 2 = {root2:.4f}",)
    elif discriminant == 0:

        root = -b / (2 * a)
        return (f"One real root (or two equal roots): Root = {root:.4f}",)
    else:

        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return (f"Two complex conjugate roots: Root 1 = {root1:.4f}, Root 2 = {root2:.4f}",)

if __name__ == "__main__":
    print("Welcome to the Quadratic Equation Root Finder!")
    print("For an equation of the form ax^2 + bx + c = 0")

    while True:
        try:
            a_str = input("Enter coefficient 'a': ")

            if a_str.lower() == 'q':
                break
            a = float(a_str)

            b_str = input("Enter coefficient 'b': ")
            if b_str.lower() == 'q':
                break
            b = float(b_str)

            c_str = input("Enter coefficient 'c': ")
            if c_str.lower() == 'q':
                break
            c = float(c_str)

            roots_info = find_quadratic_roots(a, b, c)
            for info in roots_info:
                print(info)
            print("-" * 30)
            print("Enter 'q' at any prompt to quit.")
        except ValueError:
            print("Invalid input. Please enter numbers for coefficients.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("Thank you for using the Quadratic Equation Root Finder!")
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
