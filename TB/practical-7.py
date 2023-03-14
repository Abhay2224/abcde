# Design a program for creating a machine which accept string having equal no. of 1's and 0's

def stateq0(n,countzero,countone):
    print("Q0->", end="")
    if(len(n)==0):
        if(len(countzero)==len(countone)):
            print("\n String accepted ******")
            print("\n String having equal no of 1")
        else:
            print("\n String rejected*******")
    else:
        if(n[0]=='0'):
            countzero.append('x')
            stateq0(n[1:],countzero,countone)
        elif (n[0]=='1'):
            countone.append('y')
            stateq1(n[1:],countzero,countone)

def stateq1(n, countzero,countone):
    print("Q1->", end="")
    if(len(n)==0):
        if(len(countzero)==len(countone)):
            print("\n String accepted ******")
            print("\n String having equal no of 1")
        else:
            print("\n String rejected*******")
    else:
        if(n[0]=='0'):
            countzero.append('x')
            stateq0(n[1:], countzero,countone)
        elif (n[0]=='1'):
            countone.append('y')
            stateq1(n[1:],countzero,countone)

countzero = []
countone = []

n = input("Enter 0 and 1 sequence:")

print("Transition state:")
stateq0(n,countzero,countone)
