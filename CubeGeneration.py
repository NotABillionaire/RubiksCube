##hello
#Thomas 
#This is the Cube Generation of the Rubik Cube Program
#changed 29/9/2024
import tkinter as tk

# Define the colors
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

# Define the color mapping for tkinter
color_map = {
    'W': 'white',
    'R': 'red',
    'B': 'blue',
    'G': 'green',
    'O': 'orange',
    'Y': 'yellow'
}

# Initialize selection
selected_face = 'F'
selected_row = 0
selected_col = 0

def draw_face(canvas, face, start_x, start_y, highlight=None):
    for i in range(3):
        for j in range(3):
            color = color_map[face[i][j]]
            if highlight and (i, j) == highlight:
                canvas.create_rectangle(start_x + j*30, start_y + i*30, start_x + (j+1)*30, start_y + (i+1)*30, fill=color, outline='Pink', width=3)
            else:
                canvas.create_rectangle(start_x + j*30, start_y + i*30, start_x + (j+1)*30, start_y + (i+1)*30, fill=color)

def rotate_face(face):
    # Rotate the face 90 degrees clockwise
    return [list(reversed(col)) for col in zip(*face)]

def rotate_cube(cube, move):
    if move == 'U':
        cube['U'] = rotate_face(cube['U'])
        # Update adjacent faces
        cube['F'][0], cube['R'][0], cube['B'][0], cube['L'][0] = \
            cube['R'][0], cube['B'][0], cube['L'][0], cube['F'][0]
    elif move == 'D':
        cube['D'] = rotate_face(cube['D'])
        # Update adjacent faces
        cube['F'][2], cube['R'][2], cube['B'][2], cube['L'][2] = \
            cube['L'][2], cube['F'][2], cube['R'][2], cube['B'][2]
    # Add more moves for 'L', 'R', 'F', 'B'
    # ...

def draw_cube():
    root = tk.Tk()
    root.title("Rubik's Cube")

    canvas = tk.Canvas(root, width=400, height=300)
    canvas.pack()

    def update_cube(move=None):
        if move:
            rotate_cube(faces, move)
        canvas.delete("all")
        draw_face(canvas, faces['U'], 150, 20, highlight=(selected_row, selected_col) if selected_face == 'U' else None)  # Up
        draw_face(canvas, faces['L'], 20, 100, highlight=(selected_row, selected_col) if selected_face == 'L' else None)  # Left
        draw_face(canvas, faces['F'], 150, 100, highlight=(selected_row, selected_col) if selected_face == 'F' else None) # Front
        draw_face(canvas, faces['R'], 280, 100, highlight=(selected_row, selected_col) if selected_face == 'R' else None) # Right
        draw_face(canvas, faces['B'], 410, 100, highlight=(selected_row, selected_col) if selected_face == 'B' else None) # Back
        draw_face(canvas, faces['D'], 150, 180, highlight=(selected_row, selected_col) if selected_face == 'D' else None) # Down

    def select_next_face():
        global selected_face
        faces_order = ['U', 'L', 'F', 'R', 'B', 'D']
        current_index = faces_order.index(selected_face)
        selected_face = faces_order[(current_index + 1) % len(faces_order)]
        update_cube()

    def move_selection(event):
        global selected_row, selected_col
        if event.keysym == 'Up':
            selected_row = (selected_row - 1) % 3
        elif event.keysym == 'Down':
            selected_row = (selected_row + 1) % 3
        elif event.keysym == 'Left':
            selected_col = (selected_col - 1) % 3
        elif event.keysym == 'Right':
            selected_col = (selected_col + 1) % 3
        update_cube()

    root.bind('<Up>', move_selection)
    root.bind('<Down>', move_selection)
    root.bind('<Left>', move_selection)
    root.bind('<Right>', move_selection)
    root.bind('<space>', lambda event: select_next_face())

    update_cube()  # Initial draw

    root.mainloop()

def main():
    draw_cube()

if __name__ == "__main__":
    main()

