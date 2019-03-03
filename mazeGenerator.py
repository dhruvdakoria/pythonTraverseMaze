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

rows = 35
cols = 50
mazestring = mazeGen(rows,cols)
print(mazestring)