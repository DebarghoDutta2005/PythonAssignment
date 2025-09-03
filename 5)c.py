import socket
import time
import tracemalloc

# Start memory tracking
tracemalloc.start()
start_time = time.time()

# Get IP Address
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_krishnamurthy(num):
    temp = num
    sum_fact = 0
    while temp > 0:
        digit = temp % 10
        sum_fact += factorial(digit)
        temp //= 10
    return sum_fact == num

num = int(input("Enter a number: "))

if is_krishnamurthy(num):
    print(num, "is a Krishnamurthy number.")
else:
    print(num, "is not a Krishnamurthy number.")

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
