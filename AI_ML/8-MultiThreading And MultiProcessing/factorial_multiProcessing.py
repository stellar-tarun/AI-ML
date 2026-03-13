'''
Real-world Example: Multiprocesing for CPU-Bound tasks
Scenario: Factorial Calculation
Factorial Calculations ,especially for large numbers,
involve significant computational work. Multiprocessing 
can be used to distribute the workload acroos multiple CPU cores,
improving performance.
'''

import multiprocessing
import math
import sys ## sys is a module that gives you access to system-level information and controls — basically it lets your Python code interact with the Python interpreter itself.
import time

# Increase the max number of digits for integer conversion
sys.set_int_max_str_digits(100000000)

## function to compute factorials of a given number

def compute_factorial(number):
    print(f"computing factorial of {number}")
    result=math.factorial(number)
    print(f"Factorial of {number} is {result}")
    return result

if __name__=="__main__":
    numbers=[50000,60000,200000,50000222]
    start_time=time.time()

    ## create a pool of worker of prcoess 
    with multiprocessing.Pool() as pool:
        results=pool.map(compute_factorial,numbers)
    
    end_time=time.time()

    print(f"Results: {results}")
    print(f"Time taken :{end_time-start_time} seconds ")