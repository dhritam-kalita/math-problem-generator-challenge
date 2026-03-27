from random import randint, choice

MIN_OPERAND = 3
MAX_OPERAND = 12
OPERATORS = ('+', '-', '*')
TOTAL_PROBLEMS = 3

def generate_problem():
    operand_1 = randint(MIN_OPERAND, MAX_OPERAND)
    operand_2 = randint(MIN_OPERAND, MAX_OPERAND)
    operator = choice(OPERATORS)
    if operator == '+':
        answer = operand_1 + operand_2
    elif operator == '-':
        answer = operand_1 - operand_2
    else:
        answer = operand_1 * operand_2
    
    problem = f"{operand_1} {operator} {operand_2} = "
    return problem, answer

for i in range(TOTAL_PROBLEMS):
    ques, ans = generate_problem()
    
    while True:
        user_ans = input(f"Problem #{i + 1}: {ques}")
        if user_ans == str(ans):
            break

print("Congratulations! You solved all the problems.")
    