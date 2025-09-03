import socket
import time
import tracemalloc


tracemalloc.start()
start_time = time.time()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(n, "is a Prime Number.")
else:
    print(n, "is NOT a Prime Number.")

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
