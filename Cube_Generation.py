# Thomas
# Cube Generation
# Last updated: 15/4/2025

import Config
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

def draw_unit_cube(colors):

    vertices = [
        [1, 1, -1],    # 0
        [1, -1, -1],   # 1
        [-1, -1, -1],  # 2
        [-1, 1, -1],   # 3
        [1, 1, 1],     # 4
        [1, -1, 1],    # 5
        [-1, -1, 1],   # 6
        [-1, 1, 1]     # 7
    ]
    # Define faces 
    surfaces = [
        (0, 1, 2, 3),  # Back
        (4, 5, 6, 7),  # Front
        (0, 4, 7, 3),  # Left
        (1, 5, 6, 2),  # Right
        (3, 2, 6, 7),  # Top
        (0, 1, 5, 4)   # Bottom
    ]
    glBegin(GL_QUADS)
    for i, face in enumerate(surfaces):
        glColor3fv(colors[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
    glEnd()
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(0, 0, 0)
    for edge in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


class Cubie:
    def __init__(self, position, colors):
      
        self.position = np.array(position, dtype=np.float32)
        self.colors = colors

    def draw(self):
        glPushMatrix()
        glTranslatef(*self.position)
        draw_unit_cube(self.colors)
        glPopMatrix()


class RubiksCube:
    def __init__(self):
    
        self.cubies = []
        # Solved state
        default_colors = {
            'F': (1, 0, 0),
            'B': (1, 0.5, 0),
            'L': (0, 1, 0),
            'R': (0, 0, 1),
            'U': (1, 1, 1),
            'D': (1, 1, 0)
        }
        # centre cords 
        positions = [-2, 0, 2]
        for x in positions:
            for y in positions:
                for z in positions:
                    # if the cubie is on the exterior use the appropriate color.
                    # Otherwise use gray for hidden faces.
                    colors = []
                    colors.append(default_colors['B'] if z == -2 else (0.5, 0.5, 0.5))  # Back
                    colors.append(default_colors['F'] if z == 2 else (0.5, 0.5, 0.5))   # Front
                    colors.append(default_colors['L'] if x == -2 else (0.5, 0.5, 0.5))  # Left
                    colors.append(default_colors['R'] if x == 2 else (0.5, 0.5, 0.5))   # Right
                    colors.append(default_colors['U'] if y == 2 else (0.5, 0.5, 0.5))   # Up
                    colors.append(default_colors['D'] if y == -2 else (0.5, 0.5, 0.5))  # Down
                    self.cubies.append(Cubie((x, y, z), colors))

    def draw(self):
        for cubie in self.cubies:
            cubie.draw()

    def rotate_face(self, face, angle):
    
        tol = 0.1  # Tolerance for floating point 
        if face == 'F':  # Front face
            axis = (0, 0, 1)
            for cubie in self.cubies:
                if abs(cubie.position[2] - 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, angle)
        elif face == 'B':  # Back 
            axis = (0, 0, 1)
            for cubie in self.cubies:
                if abs(cubie.position[2] + 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, -angle)
        elif face == 'L':  # Left 
            axis = (1, 0, 0)
            for cubie in self.cubies:
                if abs(cubie.position[0] + 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, angle)
        elif face == 'R':  # Right 
            axis = (1, 0, 0)
            for cubie in self.cubies:
                if abs(cubie.position[0] - 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, -angle)
        elif face == 'U':  # Up 
            axis = (0, 1, 0)
            for cubie in self.cubies:
                if abs(cubie.position[1] - 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, angle)
        elif face == 'D':  # Down 
            axis = (0, 1, 0)
            for cubie in self.cubies:
                if abs(cubie.position[1] + 2) < tol:
                    cubie.position = rotate_vector(cubie.position, axis, -angle)

def rotate_vector(vec, axis, angle):
  
    angle_rad = math.radians(angle)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    ax, ay, az = axis
    # Normalize axis
    norm = math.sqrt(ax*ax + ay*ay + az*az)
    ax, ay, az = ax/norm, ay/norm, az/norm
    x, y, z = vec
    rx = (cos_a + (1-cos_a)*ax*ax)*x + ((1-cos_a)*ax*ay - sin_a*az)*y + ((1-cos_a)*ax*az + sin_a*ay)*z
    ry = ((1-cos_a)*ay*ax + sin_a*az)*x + (cos_a + (1-cos_a)*ay*ay)*y + ((1-cos_a)*ay*az - sin_a*ax)*z
    rz = ((1-cos_a)*az*ax - sin_a*ay)*x + ((1-cos_a)*az*ay + sin_a*ax)*y + (cos_a + (1-cos_a)*az*az)*z
    return np.array([rx, ry, rz], dtype=np.float32)

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | pygame.OPENGL)
    glEnable(GL_DEPTH_TEST)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)
    glTranslatef(0.0, 0.0, -20)

    cube = RubiksCube()
    rotation_x, rotation_y = 0, 0
    mouse_down = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            if event.type == pygame.MOUSEMOTION and mouse_down:
                dx, dy = event.rel
                rotation_x += dy * Config.sensitivity
                rotation_y += dx * Config.sensitivity

            if event.type == pygame.KEYDOWN:
                # Use keys F, B, L, R, U, D to rotate faces clockwise.
                if event.key == pygame.K_f:
                    cube.rotate_face('F', 90)
                if event.key == pygame.K_b:
                    cube.rotate_face('B', 90)
                if event.key == pygame.K_l:
                    cube.rotate_face('L', 90)
                if event.key == pygame.K_r:
                    cube.rotate_face('R', 90)
                if event.key == pygame.K_u:
                    cube.rotate_face('U', 90)
                if event.key == pygame.K_d:
                    cube.rotate_face('D', 90)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rotation_x, 1, 0, 0)
        glRotatef(rotation_y, 0, 1, 0)
        cube.draw()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()

