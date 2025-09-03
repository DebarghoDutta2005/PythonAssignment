import socket
import time
import tracemalloc

def isPerfect(num):
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return sum_div == num

tracemalloc.start()
start_time = time.time()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

n = int(input("Enter a number: "))

if isPerfect(n):
    print(n, "is a Perfect Number")
else:
    print(n, "is not a Perfect Number")

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
