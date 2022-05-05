"""
----------------------------------------
#################                ########
##     ########    ###    #####  ########
###     #####   #####     #####  ########
#######        #########             ####
#######   ##       #######    ####  #####
#######   #####    ######   #####  ######
#######   #####    ####    #####   ######
####                        ####  #######
###   ##########   #######             ##
###   ###########   #####   #############
###   ############          #############
#########################################
----------------------------------------
"""
import os
import random
import readchar

POS_X = 0
POS_Y = 1

my_position = [3, 0]
tail_length = 0
obstacle_definition = """\
----------------------------------------
################## ############ #########
#################                ########
##     ########    ###    #####  ########
###     #####   #####     #####  ########
#######        #########             ####
#######   ##       #######    ####  #####
#######   #####    ######   #####  ######
#######   #####    ####    #####   ######
####                        ####  #######
###   ##########   #######             ##
###   ###########   #####   #############
###   ############          #############
#### ##################### ##############
----------------------------------------\
"""
tail = []
NUM_OBJECTS = 10
objects = []
end_game = False

obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGTH = len(obstacle_definition)
while len(objects) < NUM_OBJECTS:
    new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGTH - 1)]
    if new_position not in objects and new_position != my_position and obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
        objects.append(new_position)



while not end_game:
    print("+" + "-" * (MAP_WIDTH * 3) + "+")

    for coordinate_y in range(MAP_HEIGTH):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            draw = " "
            object_in_cell = None
            tail_in_cell = None
            wall_in_cell = None


            for object in objects:
                if object[POS_X] == coordinate_x and object[POS_Y] == coordinate_y:

                    draw = "*"
                    object_in_cell = object
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    draw = "@"
                    tail_in_cell = tail_piece


            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                draw = "@"

                if object_in_cell:
                    objects.remove(object_in_cell)
                    tail_length += 1
                    objects.append([random.randint(0, MAP_WIDTH), random.randint(0, MAP_HEIGTH)])
                if tail_in_cell:
                    print("Has muerto", end="")
                    end_game = True

            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                draw = "#"


            print(" {} ".format(draw), end="")

        print("|")

    print("+" + "-" * (MAP_WIDTH * 3) + "+")


    direction = readchar.readchar().decode()
    print(direction)
    new_position = None
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]


    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "u":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]

            my_position = new_position

    os.system("cls")



