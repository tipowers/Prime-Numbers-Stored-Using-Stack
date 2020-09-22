# This program displays the first 50 prime numbers
# And ses a stack to store the prime numbers 

# Import Stack class 
from StackClass import Stack

# Create stack to store prime numbers
stack = Stack()

# Define isPrime with num as a parameter
# This function returns True if the number is prime and false is not
def isPrime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

# Define primeNum function
# Set accumalator name to 'num' with a value of 2
# Create while statement that calls the getSize method from the Stack class
# only if the numbers are below 50
# Create if statement within while statement that if num == 2 or isPrime == True
# then push num to the stack by calling the push method
# Have num increment by 1 so that each number can be checked if isPrime or not
# Print the stack while size of the stack if below 50
def primeNum():
    num = 2
    while stack.getSize()<50:
        if num == 2 or isPrime(num) == True:
            stack.push(num)
        num += 1
    printStack()

# Define printStack function
# Print program description
# Create while statement that while stack is not empty print the stack
# Do this by calling isEmpty and pop methods from the Stack class
def printStack():
    print('\nThis program will display the first 50 prime numbers in descending order.\n')
    while not stack.isEmpty():
        print(stack.pop())

# Call primeNum function
primeNum()

# Authored by
print('\nAuthor: Tim Powers')
        





