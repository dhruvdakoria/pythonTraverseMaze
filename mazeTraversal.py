# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:29:09 2019

@author: dhruv
"""

import random,sys
from io import StringIO

def mazeGen(rows,cols):
    try :
       rows -= 1
       cols -= 1
    except (ValueError, IndexError) :
       print("2 command line arguments expected...")
       print("Usage: python maze.py rows cols")
       print("       minimum rows >= 10 minimum cols >= 20")
       quit( )
    try :
       assert rows >= 9 and cols >= 19
    except AssertionError :
       print("Error: maze dimensions must be at least 20 x 10...")
       print("Usage: python maze.py rows cols")
       print("       minimum rows >= 10 minimum cols >= 20")
       quit( )
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    (blank, roof, wall, corner) = ' -|+'
    M = str(roof * int(cols / 2))
    n = random.randint(1, (int(cols / 2)) * (int(rows / 2) - 1))
    
    for i in range(int(rows / 2)) :
       e = s = t = ''
       N = wall
       if i == 0 :
          t = '@'  # add entry marker '@' on first row first col only
       # end if
       for j in range(int(cols / 2)) :
          if i and(random.randint(0, 1) or j == 0) :
            s += N + blank
            t += wall
            N = wall
            M = M[1 : ] + corner
          else :
            s += M[0] + roof
            if i or j :
               t += blank  # add blank to compensate for '@' on first row only
             # end if
            N = corner
            M = M[1 : ] + roof
          # end if / else
          n -= 1
          t += ' #' [n == 0]
       # end for
       if cols & 1 :
            s += s[-1]
            t += blank
            e = roof
       # end if
       print(s + N + '\n' + t + wall)
    # end for
    
    if rows & 1 :
       print(t + wall)
    # end if
    print(roof.join(M) + e + roof + corner)
    sys.stdout = old_stdout
    strn = str(mystdout.getvalue())
    return strn

def createMazeMatrix(strn, rows, cols):
    print (strn)
    arr2d = [[strn[(j+(cols*i)+i)] for j in range(cols)] for i in range(rows)]
    #print (arr2d)
    return arr2d
    
def traverseMaze(arr2d):
    rows=len(arr2d)
    cols=len(arr2d[0])
    currentPath = [] 
    ch = x = a = 1
    y = b = 0
    # initSpace and remSpace will calculate initial and remaining empty spaces in the 2d array respectively
    initSpace = remSpace = 0
    stack = []
    stack.append([1,0])
    finalPath=''
    
    for i in range(len(arr2d)):     # calculates empty spaces in the maze initially
        for j in range(len(arr2d[0])):
            if arr2d[i][j] == ' ':
                initSpace+=1
                
    while ch!=0:
        if arr2d[x][y+1]!=' ' or arr2d[x+1][y]!=' ':   # when there is obstruction moving either moving North or East
            if arr2d[x+1][y]==' ':     # when moving East is possible 
                arr2d[x][y]='k'     # place once visited is marked with 'k'
                x+=1
                finalPath+='E'
                
            elif arr2d[x+1][y]=='#':      # when moving East '#' is found 
                arr2d[x][y]='k'     # place once visited is marked with 'k'
                x+=1
                finalPath+='E'
                ch=0        # the while loop will no longer execute
                break
            
            elif arr2d[x][y+1]==' ':       # when moving North is possible
                arr2d[x][y]='k'     # place once visited is marked with 'k'
                y+=1
                finalPath+='N'
            
            elif arr2d[x][y+1]=='#':       # when moving North '#' is found
                arr2d[x][y]='k'     # place once visited is marked with 'k'
                y+=1
                finalPath+='N'
                ch=0        # the while loop will no longer execute
                break
            
            else:                       # when dead end is reached
               arr2d[x][y]='k'
               coord=stack.pop()        # store the last item in stack under varible coord 
               x,y=coord[-1]            # store the coordinate values in x and y - (last coordinates where moving E and N was possible)
               finalPath=currentPath.pop()+'N'     # updating finalPath every time we start working on new coordinates
        
        else:                       # when possible to move both North and East
            arr2d[x][y]='k'         # place once visited is marked with 'k'
            stack.append([(x,y+1)])
            currentPath.append(finalPath)
            x+=1
            finalPath+='E'
    
# Iterates through the direction string and puts 'X' at the path to reach '#'
    for i in range(len(finalPath)-1):       
        if finalPath[i] == 'N':
            arr2d[a][b+1]='X'
            b+=1
        else:
            arr2d[a+1][b]='X'
            a+=1

    arr2d[1][0]='@'
    
# Calculates remaining empty spaces in the maze, clears the already traversed path 'k', prints the maze
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            if(arr2d[i][j])==' ':
                remSpace+=1
            if arr2d[i][j] == 'k':
                arr2d[i][j] = ' '
            print(arr2d[i][j],end='')
        print()
          
    print("\nMaze dimensions: (",rows,",",cols,")", sep = '')
    print("Found @ at coords: (1,0) path:",finalPath)
    print("Total searches: (",(initSpace-remSpace),"/",initSpace,") ","%.4f" %(((initSpace-remSpace)/initSpace)*100),"% of maze.", sep = '')

rows = 35
cols = 50
returned_strn=mazeGen(rows,cols)
returned_arr2d=createMazeMatrix(returned_strn,rows,cols)
traverseMaze(returned_arr2d)