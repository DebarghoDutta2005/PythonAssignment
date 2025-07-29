def generate_magic_square(n):
    if n % 2 == 0 or n < 1:
        return "Magic square is only possible for positive odd numbers."

    magic_square = [[0] * n for _ in range(n)]

    num = 1
    i, j = 0, n // 2  

    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        new_i = (i - 1) % n
        new_j = (j + 1) % n

        if magic_square[new_i][new_j]:
            i = (i + 1) % n
        else:
            i = new_i
            j = new_j

    return magic_square

n = int(input("Enter an odd number (n): "))
square = generate_magic_square(n)

if isinstance(square, str):
    print(square)
else:
    print(f"\nMagic Square of order {n}:")
    for row in square:
        print(" ".join(f"{val:3}" for val in row))
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

