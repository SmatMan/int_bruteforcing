### This function generates a random number by itself, tells you the number, and then attempts to bruteforce it itself. 
### Credits: https://github.com/smatman/

import random
from termcolor import colored
import time

min_gen = 1 # Pick the minimum number the function can generate
max_gen = 5000000 # Pick the maximum number the function can generate
start_time = time.time()

### Function starts below

print(colored("Generating a number...", 'yellow', attrs=['blink']))
number = random.randint(min_gen, max_gen)

input(colored(f"The number I generated is {number}. Press enter to start bruteforcing", 'green'))

guess = 0

while guess != number:
    print(colored(f'{guess} was not the correct number', 'red',))
    guess = guess + 1

print(colored(f'The number has been successfully guessed! The number was {number}, and I guessed {guess}. This program took {round(time.time() - start_time)} seconds to finish.', 'green', attrs=['reverse', 'blink']))