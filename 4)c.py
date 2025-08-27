import socket
import time
import tracemalloc

tracemalloc.start()
start_time = time.time()
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

n = int(input("Enter N: "))
matrix = [[0] * n for _ in range(n)]

num = 1
top, left = 0, 0
bottom, right = n - 1, n - 1

while top <= bottom and left <= right:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for row in matrix:
    print(" ".join(map(str, row)))

end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"IP Address: {ip_address}")
print(f"Time Taken: {end_time - start_time:.6f} seconds")
print(f"Current Memory Used: {current_memory / 1024:.2f} KB")
print(f"Peak Memory Used: {peak_memory / 1024:.2f} KB")
