def street_fighter_selection(fighters, initial_position, moves):
    position = list(initial_position)
    fightersList = []
    #moveT = {"up": (1, 0), "down": (-1, 0), "left": (0, 1), "right": (0, -1)}
    moveT = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
    for move in moves:
        position[0] = position[0] + moveT[move][0]
        if position[0] <= 0:
            position[0] = 0
        elif position[0] >= 1:
            position[0] = 1

        position[1] = (position[1] + moveT[move][1])%6
        #print(position)
        #print(fighters[position[0]][position[1]])
        fightersList.append(fighters[position[0]][position[1]])
    return fightersList

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up","down","right","left"]

moves =  ["up"]*4
print(street_fighter_selection(fighters,(0,0), moves))
