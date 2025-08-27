import socket
import time
import tracemalloc
tracemalloc.start()
start_time = time.time()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

n = int(input("Enter the number of lines: "))
for i in range(n):
    num = 1
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
time_taken = end_time - start_time
memory_used = current_memory / 1024
peak_memory_used = peak_memory / 1024
print(f"IP Address: {ip_address}")
print(f"Time Taken: {time_taken:.6f} seconds")
print(f"Current Memory Used: {memory_used:.2f} KB")
print(f"Peak Memory Used: {peak_memory_used:.2f} KB")
