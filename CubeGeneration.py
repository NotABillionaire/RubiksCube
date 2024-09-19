#hello
#Thomas
#This is the Cube Generation of the Rubik Cube Program

import tkinter as tk
import math


def main():
    # Define the vertices of the cube
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]

    # Define the edges of the cube
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]

    # Define the perspective projection function
    def project_vertex(vertex, distance):
        x, y, z = vertex
        factor = distance / (z + distance)
        x_proj = x * factor
        y_proj = y * factor
        return (x_proj, y_proj)

    # Distance from the viewer to the screen
    distance = 5

    # Project the vertices
    projected_vertices = [project_vertex(vertex, distance) for vertex in vertices]

    # Create the  window
    root = tk.Tk()
    root.title("3D Cube")

    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # Center of the window
    center_x = 200
    center_y = 200

    # Draw the cube
    for edge in edges:
        start, end = edge
        x1, y1 = projected_vertices[start]
        x2, y2 = projected_vertices[end]

        x1 = int(x1 * 100 + center_x)
        y1 = int(y1 * 100 + center_y)
        x2 = int(x2 * 100 + center_x)
        y2 = int(y2 * 100 + center_y)

        canvas.create_line(x1, y1, x2, y2, fill="black")

    root.mainloop()

if __name__ == "__main__":
    main()
