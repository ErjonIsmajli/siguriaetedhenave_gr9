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

def decrypt_trellis(ciphertext: str, rows: int) -> str:

 if rows < 2:
 return ciphertext
 if rows >= len(ciphertext):
 return ciphertext
 
 n = len(ciphertext)
 
 
 rail_lengths = [0] * rows
 row = 0
 going_down = True
 for _ in range(n):
 rail_lengths[row] += 1
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
 
 
 rails = []
 idx = 0
 for length in rail_lengths:
 rails.append(list(ciphertext[idx:idx + length]))
 idx += length
 
 
 result = []
 rail_indices = [0] * rows
 row = 0
 going_down = True
 for _ in range(n):
 result.append(rails[row][rail_indices[row]])
 rail_indices[row] += 1
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
 
 return "".join(result)
 
 
def visualize_trellis(text: str, rows: int, label: str = "Plaintext") -> None:

 grid = _build_trellis(text, rows)
 all_idx = [i for row in grid for i, ch in enumerate(row) if ch != ' ']
 used_cols = (max(all_idx) + 1) if all_idx else 1
 
 print(f"\n{'='*55}")
 print(f" Trellis Cipher - {label} (rows={rows})")
 print(f"{'='*55}")
 for i, row in enumerate(grid):
 print(f" Rreshti {i}: {''.join(row[:used_cols])}")
 print(f"{'='*55}")
