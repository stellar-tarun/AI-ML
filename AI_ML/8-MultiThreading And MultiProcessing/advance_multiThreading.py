##MultiThreading with Thread Pool executor

from concurrent.futures import ThreadPoolExecutor

import time

def print_numbers(number):
    time.sleep(1)
    return f"Number : {number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3 ) as executor1: ## 3 is denoting no of thread
    results=executor1.map(print_numbers,numbers)

for result in results:
    print(result)