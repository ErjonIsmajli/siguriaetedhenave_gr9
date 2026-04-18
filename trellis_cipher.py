import math

def _build_trellis(text: str,rows: int) -> list[list[str]]:

 n = len(text)
cols = n

grid = [[' ' for _ in range(cols)] for _ in range(rows)]

row, col = 0, 0
going_down = True

for char in text:
    grid[row][col] = char
    if going_down:
        if row == rows - 1:
            going_down=False
            row-= 1
        else:
            row+= 1 
            
    else:
     if row == 0:
      going_down = True
    row += 1
else:
    row -= 1
    col += 1       
    
   return grid

def encrypt_trellis(plaintext: str,rows: int) -> str:


    if rows < 2:
        return plaintext
    if rows >= len(plaintext):
        return plaintext
    
    rails = [[] for _ in range(rows)]
    row = 0
    going_down = True

    for char in plaintext:
        rails[row].append(char)
        if going_down:
            if row == rows - 1:
                going_down = False
                row -= 1
            else:
                row += 1
        else:
         if row == 0:
          going_down = True
    row += 1
    else:
    row -= 1
 
 
return "".join("".join(rail) for rail in rails)
