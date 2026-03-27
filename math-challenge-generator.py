from random import randint, choice
from time import time

MIN_OPERAND = 3
MAX_OPERAND = 12
OPERATORS = ('+', '-', '*')
TOTAL_PROBLEMS = 10
def take_input_param():
    global MIN_OPERAND, MAX_OPERAND, TOTAL_PROBLEMS
    MIN_OPERAND = input(f"Enter the minimum operand: ")
    MAX_OPERAND = input("Enter the maximum operand: ")
    TOTAL_PROBLEMS = input("Enter the total number of problems: ")
    
def generate_problem():
    operand_1 = randint(MIN_OPERAND, MAX_OPERAND)
    operand_2 = randint(MIN_OPERAND, MAX_OPERAND)
    operator = choice(OPERATORS)
    
    problem = f"{operand_1} {operator} {operand_2}"
    answer = eval(problem)
    
    return problem, answer

inpt = input("Press ENTER to start (d to enter detailed troubleshooter): ").lower()
if inpt == 'd':
    take_input_param()
    
print("--------------------------")
start_time = time()
for i in range(TOTAL_PROBLEMS):
    ques, ans = generate_problem()
    
    while True:
        user_ans = input(f"Problem #{i + 1}: {ques} = ")
        if user_ans == str(ans):
            break
end_time = time()
time_taken = round(end_time - start_time, 2)
print("--------------------------")
print(f"Congratulations! You solved all the problems in {time_taken} seconds.")
    