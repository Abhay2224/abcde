# Design a program for accepting decimal number divisile by 2

def stateQ0(n):
    print("Q0->", end="")
    if (len(n)==0):
        print("\n **string accepted**")
    else:
        if(n[0]=='0'):
            stateQ0(n[1:])
        elif (n[0]=='1'):
            stateQ1(n[1:])

def stateQ1(n):
    print("Q1->", end="")
    if (len(n)==0):
        print("\n **string not accepted**")
    else:
        if(n[0]=='0'):
            stateQ0(n[1:])
        elif(n[0]=='1'):
            stateQ1(n[1:])

n=int(input("Enter a decimal no: "))
n=bin(n).replace("0b", "")
print(n)

print("Transition state: ")
stateQ0(n)
