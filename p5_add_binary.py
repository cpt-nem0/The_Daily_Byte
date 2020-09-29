"""
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0.

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""


def addBinary(a: str, b: str)->str:
    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = ''
    while i>=0 or j>=0:
        sum = carry
        if i>=0:
            sum += int(a[i])
        if j>=0:
            sum += int(b[j])
        i-=1
        j-=1
        carry = 1 if sum > 1 else 0
        result += str(sum%2)
    if carry:
        result += str(carry)
    return result[::-1]


if __name__ == "__main__":
    a = input('a> ')
    b = input('b> ')

    print(addBinary(a, b))
    
    
    
    
# Alternative: 
# def addBinary(a: str, b: str)->str:   
#   return str(bin(int(a,2)+int(b,2)))[2:]