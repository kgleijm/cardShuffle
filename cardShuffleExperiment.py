import random as r
import matplotlib.pyplot as plt


def getDistanceBetween(a, b, deck):
    distance = 0
    counting = False
    for e in deck:
        if counting:
            distance += 1
        if (e == a or e == b) and counting:
            return distance
        if e == a or e == b:
            counting = True

def getAverageDistance(deck):
    totalDifference = 1
    for i in range(1, len(deck)):
        totalDifference += getDistanceBetween(i, i-1, deck)
    avgDistance = totalDifference/len(deck)
    # print("average distance between cards: ", avgDistance)
    return avgDistance

def conductExperiment(shuffleTechnique, amountOfShuffles, amountDecks):
    # set the bar
    expDecks = []
    expResults = []

    # initialize decks
    for i in range(amountDecks):
        expDecks.append(getUnShuffledDeck())

    # initialize value list for each shuffle
    for i in range(amountOfShuffles):
        expResults.append([])

    # shuffle decks n times
    for i in range(amountOfShuffles):
        print("shuffeling done", i / amountOfShuffles * 100, "%")
        for deck in expDecks:
            shuffleTechnique(deck)
            expResults[i].append(getAverageDistance(deck))

    # take average of each resultList
    for i in range(amountOfShuffles):
        average = sum(expResults[i]) / amountDecks
        expResults[i] = average

    plt.grid(True)
    plt.title(shuffleTechnique.__name__ + "\n" + str(amountDecks) + " Decks " + str(amountOfShuffles) + " Shuffles")
    plt.ylabel("Avg card distance")
    plt.xlabel("Amount of shuffles")
    plt.plot(expResults)
    plt.show()
    return expResults

def getUnShuffledDeck():
    output = []
    for i in range(60):
        output.append(i)
    getAverageDistance(output)
    return output


def interleave(inputDeck, offset=0):

    interleavedDeck = []
    pileA = inputDeck[len(inputDeck) // 2:]
    pileB = inputDeck[:len(inputDeck) // 2]

    # print("pileA", pileA)
    # print("pileB", pileB)
    # print("interleaved deck")

    # used to cap max consecutive a's or b's
    randomOffset = 0.5

    while len(pileA) > 0 or len(pileB) > 0:
        if len(pileA) == 0 and len(pileB) > 0:
            interleavedDeck.append(pileB.pop())
        elif len(pileB) == 0 and len(pileA) > 0:
            interleavedDeck.append(pileA.pop())
        elif offset > 0:
            interleavedDeck.append(pileA.pop())
            offset += 1
        elif offset < 0:
            interleavedDeck.append(pileB.pop())
            offset -= 1
        elif r.random() > randomOffset:
            interleavedDeck.append(pileA.pop())
            randomOffset += 0.15
        else:
            interleavedDeck.append(pileB.pop())
            randomOffset -= 0.15
        # print("pileA", pileA)
        # print("pileB", pileB)
        # print("interleaved deck", interleavedDeck)

    interleavedDeck

    inputDeck.clear()
    inputDeck += interleavedDeck




# different shuffle techniques

def shuffleOverhandTopPackets(inputDeck):
    smallestPacketSize = 5
    largestPacketSize = 15
    deck = inputDeck.copy()
    shuffledDeck = []
    while len(deck) > 0:
        packetSize = r.randint(smallestPacketSize, largestPacketSize)
        if packetSize > len(deck):  # never overdraw
            packetSize = len(deck)
        packet = deck[0: packetSize]
        shuffledDeck = packet + shuffledDeck
        deck = deck[packetSize:]

    #  change inputDeck using mutable operations
    inputDeck.clear()
    inputDeck += shuffledDeck

def shuffleOverhandAlternatingPackets(inputDeck):
    smallestPacketSize = 5
    largestPacketSize = 15
    deck = inputDeck.copy()
    shuffledDeck = []
    step = 0
    while len(deck) > 0:
        packetSize = r.randint(smallestPacketSize, largestPacketSize)
        if packetSize > len(deck):  # never overdraw
            packetSize = len(deck)
        packet = deck[0: packetSize]
        if step % 2 == 0:
            shuffledDeck = packet + shuffledDeck
        else:
            shuffledDeck = shuffledDeck + packet

        print(shuffledDeck)
        deck = deck[packetSize:]
        step += 1

    #  change inputDeck using mutable operations
    inputDeck.clear()
    inputDeck += shuffledDeck

def riffleShuffle(inputDeck):
    interleave(inputDeck)

def ABshuffle(inputDeck):
    interleavedDeck = []
    pileA = inputDeck[len(inputDeck) // 2:]
    pileB = inputDeck[:len(inputDeck) // 2]

    # print("pileA", pileA)
    # print("pileB", pileB)
    # print("interleaved deck")

    # used to cap max consecutive a's or b's
    stepcount = 0
    while len(pileA) > 0 or len(pileB) > 0:
        if len(pileA) == 0 and len(pileB) > 0:
            interleavedDeck.append(pileB.pop())
        elif len(pileB) == 0 and len(pileA) > 0:
            interleavedDeck.append(pileA.pop())
        elif stepcount % 2 == 0:
            interleavedDeck.append(pileA.pop())
        else:
            interleavedDeck.append(pileB.pop())
        stepcount += 1

conductExperiment(riffleShuffle, 10, 1000)


# deck = getUnShuffledDeck()
# print(deck)
# interleave(deck)
# print(deck)




# resultList = conductExperiment(r.shuffle, 60, 1000)
# average = sum(resultList)/len(resultList)
# print("average: ", average)















