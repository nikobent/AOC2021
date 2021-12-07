import numpy as np

def row_win(bingoNumbers, card):
    for i, num in enumerate(bingoNumbers):
        for j, row in enumerate(card):
            if all(elem in bingoNumbers[:i] for elem in row):
                return i-1


def win(bingoNumbers, card):
    #transpose card
    cardTran = np.array(card).T.tolist()

    row_bingo = row_win(bingoNumbers, card)
    column_bingo = row_win(bingoNumbers, cardTran)
    return row_bingo if row_bingo < column_bingo else column_bingo

def main():
    """find out which bingo board will win first"""
    with open("inputD4T1.txt","r") as f:
        data = f.readlines()

    #now get the numbers for the bingo
    helper = data[0].split(",")
    bingoNumbers = list(map(int, helper))

    #now get the cards ready
    cards = []
    card = []
    for i, row in enumerate(data[1:]):
        if row == "\n" or i == len(data[1:])-1:
            if card:
                cards.append(card)
                card = []
            continue
        onlyNumbers = row.split("\n")[0]
        seperatedNumbers = onlyNumbers.split(" ")
        helper2 = list(filter(lambda ele: ele!="", seperatedNumbers))
        helper3 = list(map(int,helper2))
        card.append(helper3)
    won = []
    for i, card in enumerate(cards):
        won.append(win(bingoNumbers, card))


    #which card won first
    min_value = min(won)
    print(won)
    min_index = won.index(min_value)
    print(bingoNumbers[min_value])
    flat_card = list(item for sublist in cards[min_index] for item in sublist)
    sum_out = 0
    print(cards)
    print("oi")
    for k, num in enumerate(flat_card):
        if num in bingoNumbers[:min_value+1]:
            continue
        print(num)
        sum_out = sum_out + num
    print(sum_out)
    print(sum_out*bingoNumbers[min_value])



if __name__ == "__main__":
    main()