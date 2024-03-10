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
        
    return True