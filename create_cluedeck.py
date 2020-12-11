from jservicepy import jService

jeopardy = jService()

# creates a 'deck' of clues containing the clue category, question, answer, point value, and airdate
def create_cluedeck(clue_count):
    # the deck of clues is a matrix containing lists storing relevant information
    cluedeck = []

    # makes the necessary amount of lists for storing questions
    for i in range(clue_count): cluedeck.append([])

    # randomly gets a set of clues from the jService API
    random_clues = jeopardy.random(clue_count)

    # adds the category, question, answer, point value, and airdate to a list within the matrix
    for k in range(len(random_clues)):
        cluedeck[k].append(random_clues[k].category.title.upper())
        cluedeck[k].append(random_clues[k].question)
        cluedeck[k].append(random_clues[k].answer)
        cluedeck[k].append(random_clues[k].value)
        cluedeck[k].append(random_clues[k].airdate[0:4])

    return cluedeck
