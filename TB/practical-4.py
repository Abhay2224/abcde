# Design a Program for creating a machine that accepts three consecutive one.

def stateQ0(inputstr):
    print("Q0->", end="")
    if(len(inputstr)<=2):
        print("String Rejected")
    elif(inputstr[0]=='1'):
        stateQ1(inputstr[1:])
    elif(inputstr[0]=='0'):
        stateQ0(inputstr[1:])
    
def stateQ1(inputstr):
    print("Q1->", end="")
    if(len(inputstr)<=1):
        print("String Rejected")
    elif(inputstr[0]=='0'):
        stateQ0(inputstr[1:])
    elif(inputstr[0]=='1'):
        stateQ2(inputstr[1:])

def stateQ2(inputstr):
    print("Q2->", end="")
    if(len(inputstr)<=0):
        print("String Rejected")
    elif(inputstr[0]=='1'):
        stateQ3(inputstr[1:])
    elif(inputstr[0]=='0'):
        if (len(inputstr)<2):
            print("String Rejected")
        else:
            stateQ0(inputstr[1:])

def stateQ3(inputstr):
    print("Q3->", end="")
    print("String Accepted")
    remainstr=len(inputstr)
    if(remainstr>=2):
        for i in range(remainstr):
            print("Q3->", end="")


inputstr = input("Enter a string of 1 and 0: ")
lenstr=len(inputstr)
print(lenstr)
if lenstr<3:
    print("Enter a string of atleast 3 numbers")
elif inputstr=="111":
    print("String Accepted")
else:
    # call state Q0
    stateQ0(inputstr)