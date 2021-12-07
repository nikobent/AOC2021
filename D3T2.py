#calculate oxygen gen : input a list of binary sequences,
#ox is https://adventofcode.com/2021/day/3#part2
def oxygen(sequences):
    for i, num in enumerate(sequences[0]):
        helper = 0
        for j, seq in enumerate(sequences):
            if seq[i] == '1':
                helper = helper + 1
            else:
                helper = helper - 1
        helper = (1 if helper >= 0 else 0)
        sequences = list(filter(lambda x: int(x[i]) == helper, sequences))
        if len(sequences) == 1:
            break
    return sequences[0]

#calculate c02 gen : input a list of binary sequences,
#ox is https://adventofcode.com/2021/day/3#part2
def c02(sequences):
    for i, num in enumerate(sequences[0]):
        helper = 0
        for j, seq in enumerate(sequences):
            if seq[i] == '1':
                helper = helper + 1
            else:
                helper = helper - 1
        helper = (0 if helper >= 0 else 1)
        sequences = list(filter(lambda x: int(x[i]) == helper, sequences))
        if len(sequences) == 1:
            break
    return sequences[0]

#the main of the script
def main():
    with open("inputD3T1.txt","r") as f:
        numbers = f.readlines()
    numbers = [i[:-1] for i in numbers]
    ox = (oxygen(numbers))
    co2 = (c02(numbers))

    result = int(ox,2) * int(co2,2)
    print(result)

if __name__ == '__main__':
    main()