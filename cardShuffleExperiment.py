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
    averageDistancesUsingTopPackets = [getAverageDistance(mainDeck)]
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
        average = sum(expResults[i]) / amountOfShuffles
        expResults[i] = average

    print(expResults)
    plt.plot(expResults)
    plt.show()

def getUnShuffledDeck():
    output = []
    for i in range(60):
        output.append(i)
    getAverageDistance(output)
    return output


# different shuffle techniques

def shuffleOverhandTopPackets(inputDeck):
    smallestPacketSize = 5
    largestPacketSize = 8
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


# initialization
# mainDeck = getUnShuffledDeck()
# print("mainDeck:")
# print(mainDeck)




conductExperiment(shuffleOverhandTopPackets, 100, 100)


# # run experiment n times
# experimentCount = 1
# for experiment in range(experimentCount):
#     mainDeck = getUnShuffledDeck()
#     for i in range(1, 101):
#         shuffleOverhandTopPackets(mainDeck, 5, 8)
#         averageDistancesUsingTopPackets[i] += getAverageDistance(mainDeck)
# for i in range(experimentCount):
#     averageDistancesUsingTopPackets[i] = averageDistancesUsingTopPackets[i]/experimentCount

#
# print(mainDeck)
# getAverageDistance(mainDeck)














