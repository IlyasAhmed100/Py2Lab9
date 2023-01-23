# Import Functions
from stacksQueues import Stack

def parChecker(parString):
    S = Stack()

    if parString == "":
        return True
    else:

        if parString[0] == "(":
            S.push("(")
        elif parString[0] == ")":
            return False

        for i in range(1, len(parString)):
            if parString[i] == "(":
                S.push("(")
            elif parString[i] == ")":
                if S.isEmpty() == True:
                    return True
                else:
                    S.pop()

        if S.isEmpty() == True:
            return True
        else:
            return False

print(parChecker("()("))
