"""
Given a string representing the sequence of moves a robot vacuum makes, 
return whether or not it will return to its original position. 
The string will only contain L, R, U, and D characters, 
representing left, right, up, and down respectively.

Ex: Given the following strings...
"LR", return true
"URURD", return false
"RUULLDRD", return true
"""


def check_home(directions):
    x, y = 0, 0

    for direct in directions:
        if direct == 'U':
            y += 1
        elif direct == 'D':
            y -= 1
        elif direct == 'L':
            x -= 1
        elif direct == 'R':
            x += 1
    return (x == y == 0)


if __name__ == "__main__":
    directions = input('> ')
    print(check_home(directions))
