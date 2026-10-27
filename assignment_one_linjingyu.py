# Name: [Lin Jingyu]
# Assignment One

from turtle import *
from random import randint


# ==========================================
# Task 1: Turtle Drawing 
# ==========================================
def draw_patterns():
    print("\n--- Task 1: Turtle Drawing ---")
    shape = input("Choose a pattern to draw (1 for Square, 2 for Triangle, 3 for Star): ")
    
    # 根据选择的图形设定旋转角度
    if shape == "1":
        angle = 90.991   # 正方形螺旋
    elif shape == "2":
        angle = 121      # 三角形螺旋
    elif shape == "3":
        angle = 144.5    # 五角星螺旋
    else:
        print("Invalid selection, defaulting to Star pattern.")
        angle = 144.5

    print("Drawing in progress... Click on the turtle window to close it when finished.")
    
    # 重置画布状态
    reset()
    bgcolor('black')
    speed(0)
    colormode(255)

    # for loops
    for x in range(1, 200):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        
        pencolor(r, g, b)  # 动态改变颜色
        fd(50 + x)         # 动态改变长度
        rt(angle)          # 旋转特定角度绘制对应形状

    exitonclick()


# ==========================================
# Task 2: QA Bot
# ==========================================
def run_qa_bot():
    print("\n--- Task 2: Question Answering Bot ---")
    print("Supported keywords: HKU, robot, jetson, ai, human ( plus hello, python, name )")
    question = input("Ask me something: ").lower()
    
    #HKU, robot, jetson, ai, human
    if "hku" in question:
        print("Bot: HKU is the University of Hong Kong, a world-renowned institution.")
    elif "robot" in question:
        print("Bot: Robots are programmable machines capable of carrying out complex actions.")
    elif "jetson" in question:
        print("Bot: Jetson Nano is an AI computer.")
    elif "ai" in question:
        print("Bot: AI means Artificial Intelligence.")
    elif "human" in question:
        print("Bot: Humans have creativity and empathy, while I process code and logic!")
    elif "hello" in question:
        print("Bot: Hello! Nice to meet you.")
    elif "python" in question:
        print("Bot: Python is a language.")
    elif "name" in question:
        print("Bot: My name is Python Bot.")
    else:
        print("Bot: Sorry, I don't understand.")


# ==========================================
# Task 3: Simple Calculator
# ==========================================
def run_calculator():
    print("\n--- Task 3: Simple Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /): ")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operation")
    except ValueError:
        print("Error: Please enter valid numbers.")


# ==========================================
# main
# ==========================================
print("----- Welcome to Assignment 1 System ----")
while True:
    a = input("\n---- Please select a task to run:\n"
              " (1 for Turtle Drawing, 2 for QA Bot, 3 for Simple Calculator, 0 to Exit)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_patterns()
        elif a == 2:
            run_qa_bot()
        elif a == 3:
            run_calculator()
        elif a == 0:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Please input the value in [1, 2, 3, 0]")
    except:
        print("Please input the value in [1, 2, 3, 0]")