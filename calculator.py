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
    tokens = input_string.split(' ')
    valid_tokens = {"+": 3, "-": 3, "*": 3, "/": 3, "square": 2, "cube": 2, "pow": 3, "mod": 3} 

    if input_string == "q":
        break

    # elif tokens[0] not in valid_tokens:
    #     print("Invalid input")
    
    elif len(tokens) != valid_tokens[tokens[0]]:
        print("Invalid input")
    
     
    # elif tokens[0] in valid_tokens:
    #     for i in range(1,len(tokens)):
    #         try: 
    #             int(tokens[i])
    #         except:
    #             print("Input not valid.")
    #             break

    for i in range(len(tokens)): 
        if i == 0: 
            if tokens[0] not in valid_tokens: 
                print("Invalid input.")
                break
        else: 
            try: 
                int(tokens[i])
            except: 
                print("Input not valid")
                break

    else:

        #create valid tokens list
        #iterate through tokens (using range of len)
            #if tokens[0] is not in our operator list
                #print error message
            #else:
                #try to convert the passed string to integer
                #exception would be a print statement with an error message

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
            
