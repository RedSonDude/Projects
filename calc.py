import string
from fractions import Fraction as f

exp = input("Expression: ")

def calc(num_1, oper, num_2):
    
# calculates value based on input

    if oper == "+":
        ans = (num_1) + (num_2)
    if oper == "-":
        ans = (num_1) - (num_2)
    if oper == "*":
        ans = (num_1) * (num_2)
    if oper == "/":
        ans = (num_1) / (num_2)
    if oper == "^":
        ans = (num_1) ** (num_2)
    return(ans)

def compute(i, exp):
    
    num_1 = ""
    x = i - 2

# puts together first number

    while (exp[x] in string.digits or exp[x] == "-") and x >= 0:
        num_1 += exp[x]
        x -=1
    first_ins = x + 1
    num_1 = int(num_1[::-1])
    if exp[x] == "/":
        numer = ""
        x -= 1
        while (exp[x] in string.digits or exp[x] == "-") and x >= 0:
            numer += exp[x]
            x -= 1
        first_ins = x + 1
        numer = numer[::-1]
        num_1 = f(int(numer), int(num_1))

    f_possible = 1
    num_2 = ""
    x = i + 2
 
# puts together second number

    while (exp[x] in string.digits or exp[x] == "-") and x < len(exp):
        num_2 += exp[x]
        if x + 1 < len(exp):
            x += 1
        else:
            f_possible = 0
            break
    last_ins = x - 1
    if not f_possible:
        last_ins += 1
    num_2 = int(num_2)
    if exp[x] == "/" and f_possible == 1:
        denom = ""
        x += 1
        while x < len(exp) and (exp[x] in string.digits or exp[x] == "-"):
            denom += exp[x]
            x += 1
        last_ins = x - 1
        num_2 = f(int(num_2), int(denom))
    a = exp[first_ins:last_ins + 1]
    b = str(calc(num_1, exp[i], num_2))
    exp = exp.replace(a, b)
    return(exp)

# i goes through string from last to first character

i = len(exp) - 2
while i > 2:
    i -= 1
    
# checks for exponent (PEMDAS)

    if exp[i] == "^":
        exp = compute(i, exp)
        i = len(exp) - 2

i = len(exp) - 2
while i > 2:
    i -= 1
  
# checks for division

    if exp[i] == "/" and exp[i+1] == " ":
        exp = compute(i, exp)
        i = len(exp) - 2

i = len(exp) - 2
while i > 2:
    i -= 1   
    
# checks for multiplication

    if exp[i] == "*":
        exp = compute(i, exp)
        i = len(exp) - 2

i = len(exp) - 2
while i > 2:
    i -= 1
    
# checks for subtraction

    if exp[i] == "-":
        exp = compute(i, exp)
        i = len(exp) - 2
        
i = len(exp) - 2
while i > 2:
    i -= 1
    
# checks for addition

    if exp[i] == "+":
        exp = compute(i, exp)
        i = len(exp) - 2

print(exp)
