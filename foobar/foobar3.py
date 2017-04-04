# part 2 of level 2 in foobar
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

# move map:

# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9| A|11| B|13|14|15|
# -------------------------
# |16| C|18|19|20| D|22|23|
# -------------------------
# |24|25|26| S|28|29|30|31|
# -------------------------
# |32| E|34|35|36| F|38|39|
# -------------------------
# |40|41| G|43| H|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------
# A = -17, B = -15
# C = -10, D = -6
# E = 6, F = 10
# G = 15, H = 17

def get_coords(v):
    c = [0, 0]
    while v - 8*c[0] >= 8:
        c[0] += 1
    while v - 8*c[0] - c[1] >= 1:
        c[1] += 1
    return c

def get_v(c):
    return 8*c[0]+c[1]

def accessible(src):
    # return accessible squares from src in one move
    a = get_coords(src)
    return [get_v(b) for b in
        map(get_coords, [x for x in
            range(64) if abs(src - x) in (6, 10, 15, 17)])
                if abs(a[0]-b[0]) < 3 and abs(a[1]-b[1]) < 3]


def answer(src, dest, moves=None):
    # on 8x8 grid numbered 0-63, find number of knight's moves required to go from src to dest
    if src == dest:
        return 0
    path_found = False
    if moves == None:
        moves = 0
    A = set(accessible(src))
    moves += 1
    if dest in accessible(src):
        return moves
    while path_found == False:
        moves += 1
        C = []
        for b in A:
            C.extend(accessible(b))
            if dest in C:
                path_found = True
                return moves
        A.clear()
        A = set(C)
        C = []
    return moves
