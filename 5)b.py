import socket
import time
import tracemalloc

tracemalloc.start()
start_time = time.time()

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == n

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

print("IP Address:", ip_address)

end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

time_taken = end_time - start_time
memory_used = current_memory / 1024
peak_memory_used = peak_memory / 1024

print(f"Time Taken: {time_taken:.6f} seconds")
print(f"Current Memory Used: {memory_used:.2f} KB")
print(f"Peak Memory Used: {peak_memory_used:.2f} KB")
