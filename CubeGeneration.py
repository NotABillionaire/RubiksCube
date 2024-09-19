#hello
#Thomas
#This is the Cube Generation of the Rubik Cube Program

# Define the colors
WHITE = 'W'
RED = 'R'
BLUE = 'B'
GREEN = 'G'
ORANGE = 'O'
YELLOW = 'Y'

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

def print_face(face):
    return [' '.join(row) for row in face]

def print_cube():
    up = print_face(faces['U'])
    left = print_face(faces['L'])
    front = print_face(faces['F'])
    right = print_face(faces['R'])
    back = print_face(faces['B'])
    down = print_face(faces['D'])

    # Print the cube faces next to each other
    print("    Up")
    for row in up:
        print("      " + row)
    print("Left  Front  Right  Back")
    for l, f, r, b in zip(left, front, right, back):
        print(f"{l}  {f}  {r}  {b}")
    print("    Down")
    for row in down:
        print("      " + row)

def main():
    # Print the initial state of the cube
    print_cube()

if __name__ == "__main__":
    main()

