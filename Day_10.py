#Calculator Application 
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operator = {
    "+": add,
    "-": sub,
    '*': mul,
    "/": div,
}

def calculator():
    a = int(input("Enter the first number: "))
    loop = True
    while loop:
        for i in operator:
            print(i)
        op = input("Enter the operator: ")
        b = int(input("Enter the next number: "))
        ans = operator[op](a,b)
        print(f"{a}{op}{b}={ans}")
        if input("Do you want to continue? Enter 'y' for yes and 'n' for no.") == 'y':
            if input("Use previous result or start a new calculation? Enter 'new' for new.") == 'new':
                a = int(input("Enter the first number: "))
            else:
                a = ans

        else:
            break


calculator()