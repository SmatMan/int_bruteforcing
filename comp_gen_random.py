### This function generates a random number by itself, but then instead of incrementally searching, it generates random numbers to brute-force. This method isn't the *best* but it works. Incremental is usually your best bet.
### Credits: https://github.com/smatman/

import random
from termcolor import colored
import time

min_gen = 1 # Pick the minimum number the function can generate
max_gen = 5000000 # Pick the maximum number the function can generate

print(colored("Generating a number...", 'yellow', attrs=['blink']))
number = random.randint(min_gen, max_gen)
start_time = time.time()

input(colored(f"The number I generated is {number}. Press enter to start bruteforcing", 'green'))

guess = 0
increment = 1

while guess != number:
    print(colored(f'{guess} was not the correct number. Trial {increment}.', 'red',))
    guess = random.randint(min_gen, max_gen)
    increment = increment + 1

print(colored(f'The number has been successfully guessed! The number was {number}, and I guessed {guess}. This program took {round(time.time() - start_time)} seconds to finish.', 'green', attrs=['reverse', 'blink']))