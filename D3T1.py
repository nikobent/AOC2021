#calculate gamma : input a list of binary sequences,
#gamma is calculated by the majority of binary per position of all sequences
def gamma(sequences):
    gamma = []
    print(sequences[0])
    for i, num in enumerate(sequences[0]):
        helper = 0
        for j, seq in enumerate(sequences):
            print(seq)
            print(i)
            if seq[i] == '1':
                helper = helper + 1
            else:
                helper = helper - 1
        gamma.append(1 if helper > 0 else 0)
    gm = ''.join(str(i) for i in gamma)
    return gm

def epsilon(gamma):
    eps = []
    for i, num in enumerate(gamma):
        if int(num) >0 :
            eps.append(str(0))
        else:
            eps.append(str(1))
    ep = ''.join(j for j in eps)
    return ep

#the main of the script
def main():
    with open("inputD3T1.txt","r") as f:
        numbers = f.readlines()
    numbers = [i[:-1] for i in numbers]
    gam = gamma(numbers)
    eps = epsilon(gam)
    print(gam)
    print(eps)
    consumption = int(gam,2) * int(eps,2)
    print(consumption)

if __name__ == '__main__':
    main()