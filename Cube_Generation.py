#hello
#Thomas
#This is the Cube Generation of the Rubik Cube Program
#changed 29/9/2024

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

def draw_cube():
    glBegin(GL_QUADS)
    for i, face in enumerate(surfaces):
        glColor3fv(cube_colors[i])  #set color for each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glLineWidth(3) 
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)  #black
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    draw_grid()

def draw_grid():
    glColor3f(0, 0, 0)  #black lines
    for face in surfaces:
        v0, v1, v2, v3 = [vertices[i] for i in face]
        
        #draw two horizontal lines
        for i in range(1, 3):
            factor = i / 3
            glBegin(GL_LINES)
            glVertex3f(v0[0] * (1 - factor) + v1[0] * factor,
                       v0[1] * (1 - factor) + v1[1] * factor,
                       v0[2] * (1 - factor) + v1[2] * factor)
            glVertex3f(v3[0] * (1 - factor) + v2[0] * factor,
                       v3[1] * (1 - factor) + v2[1] * factor,
                       v3[2] * (1 - factor) + v2[2] * factor)
            glEnd()

        #draw two vertical lines
        for i in range(1, 3):
            factor = i / 3
            glBegin(GL_LINES)
            glVertex3f(v0[0] * (1 - factor) + v3[0] * factor,
                       v0[1] * (1 - factor) + v3[1] * factor,
                       v0[2] * (1 - factor) + v3[2] * factor)
            glVertex3f(v1[0] * (1 - factor) + v2[0] * factor,
                       v1[1] * (1 - factor) + v2[1] * factor,
                       v1[2] * (1 - factor) + v2[2] * factor)
            glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #enable depth testing to avoid rendering faces incorrectly
    glEnable(GL_DEPTH_TEST)
    
    #set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

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
                rotation_x += dy * Config.sensitivity  #use to change the rotation sensitivity
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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #rotation
        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)

        draw_cube()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
