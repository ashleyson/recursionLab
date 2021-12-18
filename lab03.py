#lab03 Ashley Son
def multiply(x,y):
    if x == 0:
        return 0
    if y == 0:
        return 0
    return x + multiply(x, y-1)

def collectOddValues(listOfInt):
    if listOfInt == []:
        return []
    if listOfInt[0] % 2 == 1:
        return [listOfInt[0]] + collectOddValues(listOfInt[1:])
    return collectOddValues(listOfInt[1:])

def countInts(listOfInt, num):
    if listOfInt == []:
        return 0
    if listOfInt[0] == num:
        return countInts(listOfInt[1:], num) +1
    return countInts(listOfInt[1:], num)
        
def reverseString(s):
    if len(s) == 0:
        return ""

    else: 
        return s[-1] + reverseString(s[:-1])

def removeSubString(s, sub):
    if sub in s:
        x = s.find(sub)
        length = len(sub) + x
        y = s[0:x] + s[length:]
        return removeSubString(y,sub)
    else: 
        return s
