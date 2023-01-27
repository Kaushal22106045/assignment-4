import random

for i in range(0,10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    ans = int(input(f"Question {i+1}: {num1}*{num2} = "))
    if (ans == num1*num2):
        print ("Right!")
    else:
        print ("Wrong. The answer is",num1*num2)
