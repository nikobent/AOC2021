#create a function that receives signals(forward, up and down) and
#modifies to position (horizontal, depth) of the submarine
def movement(command, horizontal, depth):
    if command[0] == "f":
        horizontal = horizontal + int(command[-1])
    elif command[0] == "d":
        depth = depth + int(command[-1])
    elif command[0] == "u":
        depth = depth - int(command[-1])
    return horizontal, depth

plan = open("inputD2T1.txt","r").readlines()
hor, dep = 0, 0 #starting horizontal and depth is 0,0

for l in plan:
    #loop and change the position with each command
    hor, dep = movement(l[:-1],hor,dep)

print(hor,dep)
print(hor*dep)