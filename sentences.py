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
    else:
        verbs = ["ran", "jumped", "walked", "ate", "laughed", "danced"]
    
    return random.choice(verbs)

def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(tense)
    
    sentence = f"{determiner.capitalize()} {noun} {verb}."
    return sentence

def main():
    for _ in range(6):
        quantity = random.choice([1, 2])
        tense = random.choice(["present", "past", "future"])
        
       
        sentence = make_sentence(quantity, tense)
        print(sentence)

main()
