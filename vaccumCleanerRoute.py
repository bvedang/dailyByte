s= "URURD"

def vaccumCleanerRoute(s):
    """. Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position.
    The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively."""
    routeInstruction = {}
    for i in s:
        if i in routeInstruction:
            routeInstruction[i] += 1
        else:
            routeInstruction[i] = 1
    leftRightFlag = False
    upDownFlag = False
    if "R" and "L" in routeInstruction :
        if routeInstruction['R'] == routeInstruction['L']:
            leftRightFlag = True
    if "U" and "D" in routeInstruction :
        if routeInstruction['U'] == routeInstruction['D']:
            upDownFlag = True
    print(routeInstruction)
    if upDownFlag and leftRightFlag:
        return True
    else:
        return upDownFlag and leftRightFlag
    



print(vaccumCleanerRoute(s))