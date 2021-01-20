"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# loop for an input string
# if q --> quit
# otherwise: tokenize it
# look at first token
# do equation/math for whatever it corresponds to
# return as a float number

while True:
    input_string = input("Write an equation > ")
    if input_string == "q":
        break
    else:
        tokens = input_string.split(' ')
        if tokens[0] == "+":
            answer = (add(int(tokens[1]), int(tokens[2])))

        elif tokens[0] == "-":
            answer = (subtract(int(tokens[1]), int(tokens[2])))

        elif tokens[0] == "*":
            answer = (multiply(int(tokens[1]), int(tokens[2])))
        
        elif tokens[0] == "/":
            answer = (divide(int(tokens[1]), int(tokens[2])))
        
        elif tokens[0] == "square":
            answer = (square(int(tokens[1])))
        
        elif tokens[0] == "cube":
            answer = (cube(int(tokens[1])))

        elif tokens[0] == "pow":
            answer = (power(int(tokens[1]), int(tokens[2])))

        elif tokens[0] == "mod":
            answer = (mod(int(tokens[1]), int(tokens[2])))
    
        print(float(answer))
