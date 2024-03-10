import pygame
import heapq as hq
import numpy as np
from datetime import datetime
import sys

def valid_point(x,y): # this function is used to check if the point is in the obstacle space or not
    if ( (x >= 5) and (x<=1195) and (y<=495) and (y>=5) ): # To check if it is inside the window size
        # print( " Inside box ")
        if not ( (x>95) and (x<180) and (y > 95)) : # To check if it is inside the 1st rectangle
            # print(" Outside rectangle 1")
            if not ( (x>270) and (x<355) and (y<405) ): # To check if it is inside the 2nd rectangle
                # print(" Outside rectangle 2")
                if not ( ( ( y + 0.575 * x - 468.75 ) > 0 ) and (x>516) and ( ( y - 0.582 * x - 26.688) < 0) 
                        and ( ( y + 0.575*x - 778.8) < 0 ) and ( x < 784) and ( ( y - 0.582*x + 283.288) > 0 ) ): # To check if it is inside the hexagon
                    # print(" Outside hexagon")
                    if not ( (x>895) and (x<1105) and (y<455) and (y>45) ): # To check if it is inside the C shaped object
                        # print(" Outside C shaped object")
                        return True
                    else:
                        if ( (y<370) and (y>130) and (x<1015) ):
                            # print(" Safe zone of the C shaped object")
                            return True
                        else:
                            # print(" Inside the C shaped object")
                            return False
                else:
                    # print(" Inside Hexagon")
                    return False
            else:
                # print(" Inside rectangle 2")
                return False
        else:
            # print(" Inside rectangle 1")
            return False
    else:
        # print(" Outside box ")
        return False
        
    # return True


# taking the Start and Goal coordinates.

start_x = int(input("Enter the starting coordinate x: "))
start_y = int(input("Enter the starting coordinate y: "))
while not (valid_point(start_x,start_y)):
    print("Please try another starting point not in the object area")
    start_x = int(input("Enter the starting coordinate x: "))
    start_y = int(input("Enter the starting coordinate y: "))
    
goal_x = int(input("Enter the goal coordinate x: "))
goal_y = int(input("Enter the goal coordinate y: "))
while not (valid_point(goal_x,goal_y)) or ((goal_x == start_x)and(goal_y==start_y)):
    print("Please try another goal point not equal to start point and not in the object area")
    goal_x = int(input("Enter the goal coordinate x: "))
    goal_y = int(input("Enter the goal coordinate y: "))  

# This function moves the points and checks if the moves are valid or not using the valid_point() function defined above
def move(c,x,y): # I pass the cost values of the current node along with the coordinates to calculate the new cost of the neighboring nodes
    moves= {(1,0,-1),(1,0,1),(1,1,0),(1,-1,0),(1.4,-1,-1),(1.4,1,-1),(1.4,-1,1),(1.4,1,1)} # here I have attached the cost values to the moves
    moved = set()
    for i in moves:
        new_c,new_x,new_y = c+i[0],x+i[1],y+i[2]
        flag = valid_point(new_x,new_y)
        if flag:
            moved.add((new_c,new_x,new_y))
    return moved

