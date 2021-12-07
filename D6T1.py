def expand(lanternfishes):
    """here the internal clock of the fish will clock down and the reproduction procedure will occur.
     -1 towards 0, if 0 renew clock and create a new instance.
     Plan: create a counter and add 1 when 1 element reached 0
                --> after all iterations add these to the end."""
    c = 0
    for i, fish in enumerate(lanternfishes):
        if fish == 0:
            lanternfishes[i] = 6
            c = c + 1
        else:
            lanternfishes[i] = lanternfishes[i] - 1
    if c >0:
        new = [8] * c
        lanternfishes.extend(new)
    return lanternfishes

def main():
    """ first let's read the txt file and extract the list of integers.
    After that I will call a function on the list for the required number of times.
    """
    with open("inputD6T1.txt","r") as f:
        fish = f.readlines()[0]
    fishes = fish.split(",")
    fishes = list(map(int,fishes))

    for i in range(0, 256):
        fishes = expand(fishes)

    print(len(fishes))

if __name__ == "__main__":
    main()

