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




# Defining the variables

visited = set() # visited list
q = []      # the open queue
c = 0       # counter for the nodes
p = -1      # prev index for the starting node
cost = 0.0      # starting cost value
vc = 0          # visited list counter
goal_index = 0  # variable to check the goal index
start_element = (cost,c,p,start_x,start_y) # starting point added as an element to the heapq in the format : cost, node index, prev node, x, y coordinate
goal = (goal_x,goal_y)
start = (start_x,start_y)

hq.heappush(q, start_element)
hq.heapify(q)       # creating the heapq

graph = np.matrix([start_element]) # adding the starting element to the graph which is a numpy matrix 

start_time = datetime.now()  # start time 
while q:
    
    point = hq.heappop(q)
    
    if (point[3]==goal_x) and (point[4]==goal_y):  # checking if the start node is the goal node ( not possible but left that there )
        break
    
    c_c = point[0]      # current cost of the popped element
    neighbors = move(c_c,point[3],point[4])  # getting all the neighboring elements
    
    for n in neighbors:
        i = np.where((graph[:, 3] == n[1]) & (graph[:, 4] == n[2]))[0]
        if i.size > 0:
            if n[0] < graph[i,0]:  # checking if cost is lesser than current cost
                graph[i,0] = n[0]   # updating cost if it is lesser than known cost
                if point[1] == -1: # updating the prev node in the graph
                    graph[i,2] = point[1] + 1  #starting node has prev value of -1
                else:
                    graph[i,2] = point[1]
        else:   # in case the node does not exist in the graph, add it to the graph as a new node
            c += 1
            temp = (n[0],c,point[1],n[1],n[2])
            graph = np.vstack((graph,temp)) # vertically stacking the new node to the graph
            hq.heappush(q,temp)     # adding the element to the heapq
            
    visited.add((vc,point[3],point[4]))  # adding the node to the visited list and updating the visited counter
    vc += 1
    
    goal_index = np.where((graph[:, 3] == goal_x) & (graph[:, 4] == goal_y))[0]  # checking if the goal node is present in the graph
    if goal_index.size > 0:
        break

end_time = datetime.now()
time_taken = end_time - start_time      # calculating the time taken to complete the search

# Print the time taken
print("Time taken:", time_taken)


path_x = np.array([graph[goal_index,3]])    # storing the x coordinate of the goal node
path_y = np.array([graph[goal_index,4]])    # storing the y coordinate of the goal node

path_ind = int(graph[goal_index,2])         # taking the path ind which notes the prev node of the node in the graph

while path_ind != -1:               # setting the condition where the prev node index reaches that of the starting node
    
    x = graph[path_ind,3]
    y = graph[path_ind,4]
    
    path_x = np.append(path_x,x)
    path_y = np.append(path_y,y)
    
    path_ind = int(graph[path_ind,2])
    
# Reversing the path coordinates
path_xrev = path_x[::-1]
path_yrev = path_y[::-1]

# storing the path coordinates and the visited list in  .txt files, to visulaize without running the code again

f = open("Path.txt","w")
for i in range(len(path_xrev)):
    f.write(f"{path_xrev[i]} {path_yrev[i]}")
    f.write("\n")

f.close()

g = open("Visted.txt","w")
for i in visited:
    for j in i:
        g.write(f"{j} ")
    g.write("\n")

g.close()
