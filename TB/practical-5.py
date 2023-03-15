# Design a Program for creating machine that accepts the string always ending with 101.
#Inside State Q0.

def stateQ0(inputstr):
    print("Q0->",end="")
    if(len(inputstr)<=0):
        print("String rejected")
    elif(inputstr[0]=='1'):
        stateQ1(inputstr[1:])
    elif(inputstr[0]=='0'):
        stateQ0(inputstr[1:])

#Inside State Q1
def stateQ1(inputstr):
    print("Q1->",end="")
    if(len(inputstr)<=0):
        print("String rejected")
    elif(inputstr[0]=='0'):
        stateQ2(inputstr[1:])
    elif(inputstr[0]=='1'):
        stateQ1(inputstr[1:])

#Inside State Q2
def stateQ2(inputstr):
    print("Q2->",end="")
    if(len(inputstr)<=0):
        print("String rejected")
    elif(inputstr[0]=='1'):
        stateQ3(inputstr[1:])
    elif(inputstr[0]=='0'):
        stateQ0(inputstr[1:])

#Inside Sate Q3
def stateQ3(inputstr):
    print("Q3->",end="")
    if(len(inputstr)<=0):
        print("String Accepted")
    elif(inputstr[0]=='0'):
        stateQ2(inputstr[1:])
    elif(inputstr[0]=='1'):
        stateQ1(inputstr[1:])
inputstr=input("Enter a string of 1 and 0 :")
lenstr=len(inputstr)
print(lenstr)
if lenstr<3:
    print("Enter a string of atleast 3 numbers")
else:
    print("Trasition of state:")
    #call states Q0
    stateQ0(inputstr)
