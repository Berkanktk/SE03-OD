# Function for nth Fibonacci number
import time


def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# Method which uses a lot of space
def use_space(loops):
    for i in range(0, loops):
        arr = bytearray(512000000)

# Program
start_time = int(round(time.time() * 1000))
use_space(2)
end_time = int(round(time.time() * 1000))
print('time: ' + str(end_time - start_time))
