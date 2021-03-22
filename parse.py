from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""

def parse(fname, points, transform, screen, color):
    file = open(fname, "r")
    line = ""

    while(line != "quit\n"):
        line = str(file.readline())
        print(line)
        if line == "line\n" :
            cors = file.readline().split()
            add_edge(points, int(cors[0]), int(cors[1]), int(cors[2]),
                     int(cors[3]), int(cors[4]), int(cors[5]))
        elif line == "ident\n":
            ident(transform)
        elif line == "scale\n":
            cors = file.readline().split()
            matrix_mult(make_scale(int(cors[0]), int(cors[1]), int(cors[2])),
                        transform)
        elif line == "apply\n":
            matrix_mult(transform, points)
            print_matrix(points)
        elif line == "move\n":
            cors = file.readline().split()
            move = make_translate(int(cors[0]), int(cors[1]), int(cors[2]))
            matrix_mult(move, transform)
        elif line == "rotate\n":
            cors = file.readline().split()
            rotate = new_matrix()
            if cors[0] == "x":
                rotate = make_rotX(int(cors[1]))
            elif cors[0] == "y":
                rotate = make_rotY(int(cors[1]))
            elif cors[0] == "z":
                rotate = make_rotZ(int(cors[1]))
            matrix_mult(rotate, transform)
        elif line == "display\n":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)  
        elif line == "save\n":
            clear_screen(screen)
            draw_lines(points, screen, color)
            name = file.readline().split()
            save_extension(screen, name[0])
            
            
        
       

    file.close()
