# ENPM-661-project2
ENPM 661 Project 2
Dijkstras algorithm Project 2:

Prathinav, Karnala Venkata
120380983
pratkv

github link: https://github.com/Prathinav-kV/ENPM-661-project2

Code execution:

1. When running the code, it will ask you for the start and goal coordinates.
Input the x coordinate and then input the y coordinate, based on the bottom left origin (0,0). It checks if the inputted coordinates are lying on the object space or not. It will ask you to input the right coordinates in case they fall in the obstacle space. It also ensures that the start node and goal node are not the same.

eg: 
    start x coordinate: 10
    start y coordinate: 10
    goal x coordinate: 400
    goal y coordinate: 450

2. I have defined the equations taking into consideration the clearance of 5 pixels. I calculated the equations of all the boundaries and used them in the valid_point(x,y) function. It checks if the point lies in the obstacle space or not, and returns a boolean value where True means it is a valid point and False means it is in the obstacle space.

3. The graph is a numpy matrix where each element is structured in this manner:
[ cost, node index, previous node, x coordinate, y coordinate]

The visited list is a set. 
The open queue is a heapq.

4. The animation is not real-time, I perform the animation after computing the path.

5. The red dot is the starting index.
The blue dot is the goal index.
The black line is the final path.
The white portion in the animation is the visited list. It does not grow from the starting point, it just starts all over.

Libraries used:

pygame
heapq 
numpy
datetime
sys 

