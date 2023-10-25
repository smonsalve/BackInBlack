# How to solve the 3n+1 problem using python

# The 3n+1 problem is a simple problem that can be solved using a simple algorithm.
# The problem is as follows:

# Take a number n. If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.
# Repeat this process until n is 1.

# The Collatz conjecture states that this process will always reach 1, regardless of the starting number.

# This program will take a number n and output the number of steps it takes to reach 1.

# This program will also output the number that takes the most steps to reach 1 between 1 and n.

# This program will also output the number that takes the least steps to reach 1 between 1 and n.

# This program will also output the average number of steps it takes to reach 1 between 1 and n.

# This program will also output the number of numbers between 1 and n that take 1 step to reach 1.


# This function will take a number n and return the number of steps it takes to reach 1.

def steps(n):
    steps = 0
    while n != 1:
        if n%2 == 0:
            n = n/2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1
    return steps

# This function will take a number n and return the number that takes the most steps to reach 1 between 1 and n.

def max_steps(n):
    max = 0
    max_num = 0
    for i in range(1,n+1):
        if steps(i) > max:
            max = steps(i)
            max_num = i
    return max_num

# This function will take a number n and return the number that takes the least steps to reach 1 between 1 and n.

def min_steps(n):
    min = n
    min_num = 0
    for i in range(1,n+1):
        if steps(i) < min:
            min = steps(i)
            min_num = i
    return min_num

# This function will take a number n and return the average number of steps it takes to reach 1 between 1 and n.

def avg_steps(n):
    total = 0
    for i in range(1,n+1):
        total += steps(i)
    return total/n

# This function will take a number n and return the number of numbers between 1 and n that take 1 step to reach 1.

def one_steps(n):
    count = 0
    for i in range(1,n+1):
        if steps(i) == 1:
            count += 1
    return count

# This function will take a number n and return the number of numbers between 1 and n that take 2 steps to reach 1.

def two_steps(n):
    count = 0
    for i in range(1,n+1):
        if steps(i) == 2:
            count += 1
    return count    




