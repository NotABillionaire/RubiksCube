#hello 

#Thomas Keay 

#This is the Cube Generation of the Rubik Cube Program 

import tkinter as tk 

  

# Define the colours 

WHITE = 'W' 

RED = 'R' 

BLUE = 'B' 

GREEN = 'G' 

ORANGE = 'O' 

YELLOW = 'Y' 

  

# Initialize the cube faces 

faces = { 

    'U': [[WHITE] * 3 for _ in range(3)],  # Up 

    'L': [[RED] * 3 for _ in range(3)],    # Left 

    'F': [[BLUE] * 3 for _ in range(3)],   # Front 

    'R': [[GREEN] * 3 for _ in range(3)],  # Right 

    'B': [[ORANGE] * 3 for _ in range(3)], # Back 

    'D': [[YELLOW] * 3 for _ in range(3)]  # Down 

} 

  

# Define the colour mapping for tkinter 

colour_map = { 

    'W': 'white', 

    'R': 'red', 

    'B': 'blue', 

    'G': 'green', 

    'O': 'orange', 

    'Y': 'yellow' 

} 

  

def draw_face(canvas, face, start_x, start_y): 

    for i in range(3): 

        for j in range(3): 

            colour = colour_map[face[i][j]] 

            canvas.create_rectangle(start_x + j*30, start_y + i*30, start_x + (j+1)*30, start_y + (i+1)*30, fill=colour) 

  

def draw_cube(): 

    root = tk.Tk() 

    root.title("Rubik's Cube") 

  

    canvas = tk.Canvas(root, width=400, height=300) 

    canvas.pack() 

  

    # Draw the faces 

    draw_face(canvas, faces['U'], 150, 20)  # Up 

    draw_face(canvas, faces['L'], 20, 100)  # Left 

    draw_face(canvas, faces['F'], 150, 100) # Front 

    draw_face(canvas, faces['R'], 280, 100) # Right 

    draw_face(canvas, faces['B'], 410, 100) # Back 

    draw_face(canvas, faces['D'], 150, 180) # Down 

  

    root.mainloop() 

  

def main(): 

    draw_cube() 

  

if __name__ == "__main__": 

    main() 
