#py -m pip uninstall package_name

#hello
#Thomas
#This is the Cube Generation of the Rubik Cube Program
#changed 2/01/2025

import Config
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#cube colors for each face
cube_colors = [
    (1, 0, 0),  #red
    (0, 1, 0),  #green
    (0, 0, 1),  #blue
    (1, 1, 0),  #yellow
    (1, 0.5, 0),  #orange
    (1, 1, 1)   #white
]

#vertices of the cube
vertices = [
    [1, 1, -1],  #0
    [1, -1, -1], #1
    [-1, -1, -1], #2
    [-1, 1, -1], #3
    [1, 1, 1],   #4
    [1, -1, 1],  #5
    [-1, -1, 1], #6
    [-1, 1, 1]   #7
]

#edges for wireframe
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

#surfaces for rendering
surfaces = [
    (0, 1, 2, 3),  #back
    (4, 5, 6, 7),  #front
    (0, 4, 7, 3),  #left
    (1, 5, 6, 2),  #right
    (3, 7, 6, 2),  #top
    (0, 4, 5, 1)   #bottom
]


# --- THE COORDINATE SYSTEM ---
# We create a list to store the X, Y, Z and Rotation for every cube.
# Format: [x, y, z, rot_y, rot_x, rot_z]
cube_system = []
for x in range(-1, 2):
    for y in range(-1, 2):
        for z in range(-1, 2):
            cube_system.append([x, y, z, 0, 0, 0])

def draw_cube(bottom_rotation, top_rotation, middle_rotation, bottom_side_rotation, middle_side_rotation,top_side_rotation):
    #Distance between cubes 
    spacing = 2.1 

    #Loop through X (Left/Right), Y (Up/Down), and Z (Front/Back)
    for x in range(-1, 2):      
        for y in range(-1, 2):  
            for z in range(-1, 2): 

                glPushMatrix() #Save current position 

                
                if y == 1:
                    glRotatef(top_rotation, 0, 1, 0)
                if y == 0:
                    glRotatef(middle_rotation, 0, 1, 0)
                if y == -1:
                    glRotatef(bottom_rotation, 0, 1, 0)

                if x == 1:
                    glRotatef(top_side_rotation, 1, 0, 0)
                if x == 0:
                    glRotatef(middle_side_rotation, 1, 0, 0)
                if x == -1:
                    glRotatef(bottom_side_rotation, 1, 0, 0)



                
                #Move to the specific grid slot for this cube
                glTranslatef(x * spacing, y * spacing, z * spacing)

                #Draw Faces
                glBegin(GL_QUADS)
                for i, face in enumerate(surfaces):
                    glColor3fv(cube_colors[i])  #set color for each face
                    for vertex in face:
                        glVertex3fv(vertices[vertex])
                glEnd()

                #OUtlines for the cube
                glLineWidth(5) 
                glBegin(GL_LINES)
                glColor3f(0, 0, 0)  #black
                for edge in edges:
                    for vertex in edge:
                        glVertex3fv(vertices[vertex])
                glEnd()

                glPopMatrix() #Reset position for the next cube

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #these are the variables for the roation in the same function
    bottom_rotation = 0 
    top_rotation = 0 
    middle_rotation = 0 
    top_side_rotation = 0
    middle_side_rotation = 0
    bottom_side_rotation = 0

    #enable depth testing so front cubes block back cubes
    glEnable(GL_DEPTH_TEST)
    
    #set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    
    #Zoom out code is here

    #Changed from -5 to -20 to fit the larger 3x3x3 cube
    glTranslatef(0.0, 0.0, -20) 
    
    #Rotate slightly so we see it's 3D immediately
    glRotatef(30, 1, 1, 0)

    #main loop
    running = True
    rotation_x, rotation_y = 0, 0
    mouse_down = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #physical mouse button 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            #physical mouse movement
            if event.type == pygame.MOUSEMOTION and mouse_down:
                dx, dy = event.rel
                rotation_x += dy * Config.sensitivity  
                rotation_y += dx * Config.sensitivity

            #physical keyboard input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation_y -= 5
                if event.key == pygame.K_RIGHT:
                    rotation_y += 5
                if event.key == pygame.K_UP:
                    rotation_x -= 5
                if event.key == pygame.K_DOWN:
                    rotation_x += 5

            #rubix cube z controls
            if event.type == pygame.KEYDOWN:
                #camera
                if event.key == pygame.K_LEFT: rotation_y -= 5
                if event.key == pygame.K_RIGHT: rotation_y += 5
                if event.key == pygame.K_UP: rotation_x -= 5
                if event.key == pygame.K_DOWN: rotation_x += 5

            if event.type ==pygame.KEYDOWN:
                
                if event.key == pygame.K_KP9:
                    top_rotation += 45              #change this to change the movement speed

                if event.key == pygame.K_KP7:
                    top_rotation -= 45              #change this to change the movement speed
                    

                if event.key == pygame.K_KP6:
                    middle_rotation -= -45          #change this to change the movement speed
                    

                if event.key == pygame.K_KP4:
                    middle_rotation -= 45           #change this to change the movement speed
                   

                if event.key == pygame.K_KP1:
                    bottom_rotation -= 45           #change this to change the movement speed
                    

                if event.key == pygame.K_KP3:
                    bottom_rotation -= -45          #change this to change the movement speed
                    

                if event.key == pygame.K_KP8:
                    middle_side_rotation += -45      #change this to change the movement speed
                    

                if event.key == pygame.K_KP2:
                    middle_side_rotation += 45      #change this to change the movement speed



                    


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #rotation
        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        draw_cube(bottom_rotation, top_rotation, middle_rotation, bottom_side_rotation, middle_side_rotation,top_side_rotation) #draws the cube with the roations in it

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
