def find_the_ball(start, swaps):
    """ Where is the ball? """
    position = start
    for t in swaps:
        print "Ball is at position " + str(position)
        if t[0] == position:
            print "Ball is moving to position " + str(t[1])
            position = t[1]
        elif t[1] == position:
            print "Ball is moving to position " + str(t[0])
            position = t[0]
    return position

print find_the_ball(0,[(0, 1), (2, 1), (0, 1)])
