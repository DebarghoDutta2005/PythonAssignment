import socket
import time
import tracemalloc

# Function to reverse a number
def reverse_num(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    return rev

# Start memory tracking
tracemalloc.start()
start_time = time.time()

# Get IP Address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Input
num = int(input("Enter a number: "))
print("Reversed number:", reverse_num(num))

# End time and memory usage
end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_used = current_memory / 1024    # Convert to KB
peak_memory_used = peak_memory / 1024  # Convert to KB

# Output
print(f"IP Address: {ip_address}")
print(f"Time Taken: {time_taken:.6f} seconds")
print(f"Current Memory Used: {memory_used:.2f} KB")
print(f"Peak Memory Used: {peak_memory_used:.2f} KB")
