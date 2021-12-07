#create a function that has as an input a list with measurements
#calculate how many of the measurements are bigger than the previous measurement
def increases(measurements):
    counter = 0
    for i, measurement in enumerate(measurements):
        if i == 0:
            continue
        if measurements[i] > measurements[i-1]:
            counter = counter +1
    return counter

#create a function that gets a list of numbers as an input and
#sums them with a sliding window process of length of 3
def sliding(measuments):
    additions = []
    for i, measument in enumerate(measuments):
        if i+2 < len(measuments) - 1:
            additions.append(int(measuments[i])+int(measuments[i+1])+int(measuments[i+2]))
        elif i+1 < len(measuments) - 1:
            additions.append(int(measuments[i]) + int(measuments[i + 1]))
        else:
            additions.append(int(measuments[i]))
    return additions

numbers = open("inputD1T1.txt","r").readlines()
print(len(numbers))

ex = [199,200,208,210,200,207,240,269,260,263]
print(increases(sliding(numbers)))


