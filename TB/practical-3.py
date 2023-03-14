# Write a program for generating derivation sequence / language

def computeAll():
    global rules,diction

    for rule in rules:
        k = rule.split("->")
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multirhs = rhs.split('|')
        print("len(multirhs): ", len(multirhs))

        for i in range(len(multirhs)):
            multirhs[i] = multirhs[i].strip()
            multirhs[i] = multirhs[i].split()
            diction[k[0]] = multirhs

    print(f"\nRules:  \n")

    for y in diction:
        print(f"{y}->{diction[y]}")

rules = ["S -> A k o",
        "A -> A d | a B | a C",
        "C -> c",
        "B -> b B C | r"]

sample_input_string = "a r k o"    
diction = {}
computeAll()