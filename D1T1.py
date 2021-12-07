#create a function that has as an input a list with measurements
#calculate how many of the measurements are bigger than the previous measurement
def increases(measurements):
    counter = 0
    for i, measurement in enumerate(measurements):
        if i == 0:
            continue
        if measurements[i] > measurements[i-1]:
            counter = counter +1
    return counter + 1

numbers = open("inputD1T1.txt","r").readlines()
print(len(numbers))
print(increases(numbers))



