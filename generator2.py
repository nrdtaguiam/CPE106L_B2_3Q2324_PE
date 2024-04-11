import random

articles = ("A","THE")
nouns = ("BOY", "GIRL","BAT","BALL")
verbs =("HIT","SAW","LIKED",)
prepositions = ("WITH","BY")
adjectives=('RED','BIG','LONG')
conjunctions=("AND","OR",'BUT')
def sentences():
    """ Here Builds and returns a sententce. """
    x = random.randint(0, 1)
    if x == 0:
        return nounPhrases() +" "+ verbPhrases()
    else:
        return nounPhrases() + " " + verbPhrases()+clause()


def nounPhrases():
    """Here Builds and returns a noun phrase."""
    x = random.randint(0, 1)
    if x == 0:
        return random.choice(articles)+" " + random.choice(nouns)
    else:
        return random.choice(articles) + " " + random.choice(adjectives)+" "+random.choice(nouns)
def clause():
    return random.choice(conjunctions)+" "+nounPhrases()+" "+random.choice(verbs) + " " + nounPhrases()

def verbPhrases():
    """Here Builds and retruns a verb phrase."""
    x=random.randint(0,1)
    if x== 0:
        return random.choice(verbs) + " " + nounPhrases() + " "
    else:
        return random.choice(verbs) + " " + nounPhrases() + " " + prepositionalPhrases()+" "


def prepositionalPhrases():
    """Here Builds and returns a prepositional Phrase."""
    return random.choice(prepositions)+ " " + nounPhrases()
def main():
    """ Here it Allows the user to input the number of sentences
to generate."""
    number = int(input("Enter the number of Sentences: "))
    for count in range(number):
        print(sentences())

main()