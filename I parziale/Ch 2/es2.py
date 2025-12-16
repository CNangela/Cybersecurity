# Define a simple calculator.
# The user uses the terminal and it has three variables.
# - input1: first integer number
# - input2: second integer number
# - type of operation: a number associated to the operation
#    (e.g., 0 for the addition)

# era troppo noioso se ti ascoltavo

def main():
    expression = input("Type a simple expression: ")
    print(f"Input: {expression}")
    
    n1 = ""
    n2 = ""
    operator = ""
    flag = False
    error = False

    for n in expression:
        if not error:
            if n.isdigit() and not flag:
                n1 += n
            elif n.isdigit() and flag:
                n2 += n
            elif not n.isalpha():
                operator = n
                if not flag:
                    flag = True
                else: 
                    print("Syntax Error")
                    error = True
                    break
    
    if not error:
        if operator == "+":
            risultato = int(n1) + int(n2)
        elif operator == "-":
            risultato = int(n1) - int(n2)
        elif operator == "/":
            if (n1 == "0" and n2 =="0") or n2 == "0":
                risultato = "undefined"
            else:
                risultato = int(n1) / int(n2)
        elif operator == "*":
            risultato = int(n1) * int(n2)
        elif operator == "%":
            risultato = int(n1) % int(n2)
        print(f"Output: {risultato}")

if __name__ == "__main__":
    main()