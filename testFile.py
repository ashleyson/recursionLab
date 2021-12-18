#testFile.py Ashley Son lab03
from lab03 import multiply
from lab03 import collectOddValues
from lab03 import countInts
from lab03 import reverseString
from lab03 import removeSubString

def test_multiply():
    assert multiply(3,2) == 6
    assert multiply(5,4) == 20
    assert multiply(3,4) == 12

def test_collectOddValues():
    assert collectOddValues([1,2,3,4,5]) == [1,3,5]
    assert collectOddValues([2,3,4,5,6]) == [3,5]
    assert collectOddValues([12,13,14,15,16]) == [13,15]
    
def test_countInts():
    assert countInts([1,2,3,4,3,2,1], 2) == 2
    assert countInts([1,1,1,2,3,4,5], 1) == 3
    assert countInts([3,4,5,6,5,7,8], 5) == 2

def test_reverseString():
    x = "CMPSC9"
    y = "y"
    z = "hello"
    assert reverseString(x) == "9CSPMC"
    assert reverseString(y) == "y"
    assert reverseString(z) == "olleh"
    
def test_removeSubString():
    x = "Lolololol"
    y = "up or down?"
    z = "Hello: SB:"
    assert removeSubString(x,"lol") == "Loo"
    assert removeSubString(y,"or") == "up down?"
    assert removeSubString(z,":") == "Hello SB"
