import random

def get_determiner(quantity):
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    
    return random.choice(determiners)

def get_noun(quantity):
    if quantity == 1:
        nouns = ["bird", "boy", "girl", "mouse", "cheese", "house"]
    else:
        nouns = ["birds", "boys", "girls", "mice", "cheeses", "houses"]
    
    return random.choice(nouns)

def get_verb(tense):
    if tense == "present":
        verbs = ["runs", "jumps", "walks", "eats", "laughs", "dances"]
    elif tense == "past":
        verbs = ["ran", "jumped", "walked", "ate", "laughed", "danced"]
    else:
        verbs = ["will run", "will jump", "will walk", "will eat", "will dance"]
    
    return random.choice(verbs)

def get_preposition():
    prepositions = ["in", "on", "at", "with", "under", "above", "after", "before"]
    return random.choice(prepositions)

def get_conjunction():
    conjunctions = ["and", "but", "or", "so", "yet"]
    return random.choice(conjunctions)

def get_prepositional_phrase(quantity):
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    return f"{preposition} {determiner} {noun}"

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(tense)
    conjunction = get_conjunction()
    prepositional_phrase = get_prepositional_phrase(quantity)

    if random.choice([True, False]):
        sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase} {conjunction} {get_determiner(quantity)} {get_noun(quantity)} {verb} {prepositional_phrase}."
    else:
        sentence = f"{determiner.capitalize()} {noun} {verb} {conjunction} {verb} {prepositional_phrase}."
    
    sentence = f"{determiner.capitalize()} {noun} {verb} {conjunction} {verb} {prepositional_phrase}."
    return sentence

def main():
        sentence_pattern = [
            (1, "past"),
            (1, "present"),
            (1, "future"),
            (2, "past"),
            (2, "present"),
            (2, "future"),
        ]

        for quantity, tense in sentence_pattern:
            sentence = make_sentence(quantity, tense)
            print(sentence)

main()
