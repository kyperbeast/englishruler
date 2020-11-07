def generateTick(tick, number, tick_dictionary):
    if number-1 > 0 and round(tick/2) > 0:
        tick_dictionary[round(tick/2)] = round(number-1)
        number = number - 1
        if (number > 0):
            generateTick(2**(number - 1) - 1, number, tick_dictionary)
    return tick_dictionary

def getmod(number, tick_dictionary):
    for i in tick_dictionary.keys():
        if number % i == 0:
            return tick_dictionary.get(i)
    return -1

def printLine(tick_dictionary, numberOfTickPerInch, rulerSize):
    for j in range(0, rulerSize):
        print("-"*numberOfTickPerInch, j)
        for i in range(1, ticks+1):
            mode = getmod(i, tick_dictionary)
            if i in tick_dictionary.keys():
                print("-"*tick_dictionary.get(i))
            elif mode != -1:
                print("-"*mode)
            else:
                print("-")
    print("-"*numberOfTickPerInch, rulerSize)

if __name__ == '__main__':
    rulerSize = 2
    numberOfTickPerInch = 5
    ticks = 2**(numberOfTickPerInch - 1) - 1
    tick_dictionary = {}

    generateTick(ticks, numberOfTickPerInch, tick_dictionary)
    printLine(tick_dictionary, numberOfTickPerInch, rulerSize)
