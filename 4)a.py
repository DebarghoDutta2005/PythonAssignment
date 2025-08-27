import socket
import time
import tracemalloc

tracemalloc.start()
start_time = time.time()

n = int(input("Enter the number of lines (N): "))
for i in range(1, n + 1):
    if i == 1:
        spaces = ' ' * (n - i)
        print(spaces + '.' + spaces)
    elif i < n:
        spaces = ' ' * (n - i)
        inner_spaces = ' ' * (2 * i - 3)
        print(spaces + '/' + inner_spaces + '\\' + spaces)
    else:  # last row
        underscores = '_' * (2 * i - 3)
        print('/' + underscores + '\\')

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP Address: {ip_address}")
end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
time_taken = end_time - start_time
memory_used = current_memory / 1024
peak_memory_used = peak_memory / 1024
print(f"Time Taken: {time_taken:.6f} seconds")
print(f"Current Memory Used: {memory_used:.2f} KB")
print(f"Peak Memory Used: {peak_memory_used:.2f} KB")

