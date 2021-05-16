#Today's challenge utilizes a 3rd party service, this is the Hurdles 4 solution
#https://reeborg.ca/index_en.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def around_barrier():
    turn_right()
    move()
    turn_right()
    move()

while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif front_is_clear() and not wall_on_right():
        around_barrier()
    elif wall_in_front() and wall_on_right():
        turn_left()