#create a function that receives signals(forward, up and down) and
#modifies to position (aim, horizontal, depth) of the submarine

def movement(command, aim, horizontal, depth):
    if command[0] == "f":
        horizontal = horizontal + int(command[-1])
        depth = depth + aim * int(command[-1])
    elif command[0] == "d":
        aim = aim + int(command[-1])
    elif command[0] == "u":
        aim = aim - int(command[-1])
    return aim, horizontal, depth

plan = open("inputD2T1.txt","r").readlines()
aim, hor, dep = 0, 0, 0 #starting horizontal and depth is 0,0

for l in plan:
    #loop and change the position with each command
    aim, hor, dep = movement(l[:-1],aim, hor,dep)

print(hor,dep)
print(hor*dep)