import socket
import time
import tracemalloc

SEGMENTS = {
    '0': (1,1,1,1,1,1,0),
    '1': (0,1,1,0,0,0,0),
    '2': (1,1,0,1,1,0,1),
    '3': (1,1,1,1,0,0,1),
    '4': (0,1,1,0,0,1,1),
    '5': (1,0,1,1,0,1,1),
    '6': (1,0,1,1,1,1,1),
    '7': (1,1,1,0,0,0,0),
    '8': (1,1,1,1,1,1,1),
    '9': (1,1,1,1,0,1,1)
}

def print_digit(digit):
    a,b,c,d,e,f,g = SEGMENTS[digit]
    print(' ' + ('_' * 2 if a else ' ' * 2) + ' ')
    print(('|' if f else ' ') + '   ' + ('|' if b else ' '))
    print(' ' + ('_' * 2 if g else ' ' * 2) + ' ')
    print(('|' if e else ' ') + '   ' + ('|' if c else ' '))
    print(' ' + ('_' * 2 if d else ' ' * 2) + ' ')

tracemalloc.start()
start_time = time.time()
digit = input("Enter a digit (0-9): ").strip()
if digit in SEGMENTS:
    print_digit(digit)
else:
    print("Invalid digit.")
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP Address: {ip_address}")
end_time = time.time()
current_memory, peak_memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Time Taken: {end_time - start_time:.6f} seconds")
print(f"Current Memory Used: {current_memory / 1024:.2f} KB")
print(f"Peak Memory Used: {peak_memory / 1024:.2f} KB")
