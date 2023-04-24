#!python3
"""
##### Problem 2
Create a function that determines if a triangle is scalene, right or obtuse.  
3 input parameters:  
float: one side  
float: another side  
float: 3rd side  

return:
0 : triangle does not exist
1 : if the triangle is acute
2 : if the triangle is right
3 : if the triangle is obtuse

Sample assertions:  
assert triangle(12,5,13) == 2     
assert triangle(5,3,3) == 3  
assert triangle(5,15,12) == 3  
assert triangle(1,1,4) == 0  
(2 points)
"""
import math
def triangle(a,b,c):
    x = 0
    y = 0
    z = 0
    TheList = [a,b,c]
    TheList.sort()
    if ((TheList[0] **2) + (TheList[1]**2)) < (TheList[2] **2):
            if a + b > c:
                x = 1
        
            if a + c > b:
                y = 1
        
            if b + c > a:
                z = 1
            if x == 1 and y == 1 and z == 1:
                return 3
            else: 
                return 0
    elif ((TheList[0] **2) + (TheList[1]**2)) > (TheList[2] **2):
        return 1
    elif ((TheList[0] **2) + (TheList[1]**2)) == (TheList[2] **2):
        return 2

        

def tests():
    assert triangle(12,5,13) == 2     
    assert triangle(5,3,3) == 3  
    assert triangle(5,15,12) == 3  
    assert triangle(1,1,4) == 0  


if __name__== "__main__":
    tests()
