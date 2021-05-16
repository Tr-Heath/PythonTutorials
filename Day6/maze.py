#Today's challenge utilizes a 3rd party service, this is the Maze solution
#https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()