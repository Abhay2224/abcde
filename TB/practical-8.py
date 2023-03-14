# Design a program for creating a machine which count number of 1's and 0's in a given string.

def stateq0(n,countzero,countone):
    print("Q0->",end="")
    if(len(n)==0):
        print("\n total no of 0:", len(countzero))
        print("\n total no of 1:", len(countone))
    else:
        if(n[0]=='0'):
            countzero.append('0')
            stateq0(n[1:],countzero,countone)
        elif(n[0]=='1'):
            countone.append('1')
            stateq1(n[1:],countzero,countone)

def stateq1(n,countzero,countone):
    print("Q1->",end="")
    if(len(n)==0):
        print("\n total no of 0:", len(countzero))
        print("\n total no of 1:", len(countone))
    else:
        if(n[0]=='0'):
            countzero.append('0')
            stateq0(n[1:],countzero,countone)
        elif(n[0]=='1'):
            countone.append('1')
            stateq1(n[1:],countzero,countone)

countzero=[]
countone=[]
n=input("Enter 0 and 1 sequence:")

print("Transition state:")
stateq0(n,countzero,countone)