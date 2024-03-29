from pynput.keyboard import Listener, KeyCode
import os
import sys

counter = 0
initial_coords = [1, 1]
map = [[' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.', ' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.', ' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.',' '],[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']]
os.system('cls')

for line in map:
    print(''.join(line))
sys.stdout.write('\033[H')
sys.stdout.flush()

def print_key(*key):
    global initial_coords
    x = initial_coords[0]
    y = initial_coords[1]
    
    if key[0] == KeyCode.from_char('x'):
        os.system('cls')
        sys.stdout.flush()
        os._exit(0)
    if key[0] == KeyCode.from_char('d'):
        if x +1 > len(map[y]) - 2:
            pass
        else:
            initial_coords[0] += 1
            map[y][initial_coords[0]] = '#'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('a'):
        if initial_coords[0] -1 < 1:
            pass
        else:
            initial_coords[0] -= 1
            map[y][initial_coords[0]] = '#'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('w'):
        if initial_coords[1] - 1 < 1:
            pass
        else:
            initial_coords[1] -= 1
            map[initial_coords[1]][x] = '#'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    elif key[0] == KeyCode.from_char('s'):
        if initial_coords[1] + 1 > len(map) -2:
            pass
        else:
            initial_coords[1] += 1
            map[initial_coords[1]][x] = '#'
            for line in map:
                print(''.join(line))
            sys.stdout.write('\033[H')
            sys.stdout.flush()
    
def key():
    with Listener(on_press=print_key) as listener:
        listener.join()

# Callback function for key presses
# def on_press(key):
#     try:
#         char = key.char
#     except AttributeError:
#         return
#     print_key(key, initial_coords)

while True:
    key()