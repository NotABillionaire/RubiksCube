#hello
#Thomas 
#This is the Cube Generation of the Rubik Cube Program
#changed 29/9/2024

import pygame
from pygame.locals import * # this should install all
from OpenGL.GL import *
from OpenGL.GLU import *

#Cube colors for each face 
cube_colors = [
    (1, 0, 0),  #Red
    (0, 1, 0),  #Green
    (0, 0, 1),  #Blue
    (1, 1, 0),  #Yellow
    (1, 0.5, 0),   #Orange
    (1, 1, 1)   #White
]

#Vertices of cube
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
]

#Edges for wireframe
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7)
]

#Surfaces for rendering
surfaces = [
    (0, 1, 2, 3),  #Back
    (4, 5, 6, 7),  #Front
    (0, 4, 7, 3),  #Left
    (1, 5, 6, 2),  #Right
    (3, 7, 6, 2),  #Top
    (0, 4, 5, 1)   #Bottom
]

def draw_cube():
    """Draws the cube."""
    glBegin(GL_QUADS)
    for i, face in enumerate(surfaces):
        glColor3fv(cube_colors[i])  #Set color for each face
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0, 0, 0)  #Black 
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    #Set perspective
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    #Main loop
    running = True
    rotation_x, rotation_y = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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


