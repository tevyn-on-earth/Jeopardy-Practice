from jservicepy import jService

jeopardy = jService()

# creates a 'deck' of clues containing the clue category, question, answer, point value, and airdate
def create_cluedeck(clue_count):
    # the deck of clues is a matrix containing lists storing relevant information
    cluedeck = []
    # makes the necessary amount of lists for storing questions
    for i in range(clue_count): cluedeck.append([])

    # counter keeps track of the number of clues added to the deck
    counter = 0
    # random clues are generated until 25 valid clues are added to the deck
    while counter < clue_count:
        # randomly gets a clue from the jService API
        random_clue = jeopardy.random(1)

        # adds the category, question, and answer, to a list within the matrix only if the clue is from 2010 or later
        if int(random_clue[0].airdate[0:4]) >= 2010:
            cluedeck[counter].append(random_clue[0].category.title.upper())
            cluedeck[counter].append(random_clue[0].question)
            cluedeck[counter].append(random_clue[0].answer)
            counter += 1

    return cluedeck
