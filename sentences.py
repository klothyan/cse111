import random

name = input("Hello and welcome to the random sentence generator! Type your name here to get started: ")

def main():
    words = ["bird", "boy", "girl", "mouse", "cheese", "house"]

    word = random.choice(words)

    word = "horse"

    cap_word = word.capitalize()

    def get_determiner(determiner):
        if determiner == 1:
            words = ["a", "one", "the"]
        else:
            words = ["some", "many", "the"]

        word = random.choice(words)
        return word

    def get_noun(noun):
        if noun == 1:
            words = ["bird", "boy", "girl", "mouse", "cheese", "house"]
        else:
            words = ["birds", "boys", "girls", "mice", "cheeses", "houses"]
    def get_verb(verb, tense):
        if verb == 1:
            words = ["runs", "jumps", "walks", "eats", "laughs", "dances"]
        else:
            words = ["ran", "jumped", "walked", "ate", "laughed","danced"]

    def make_sentence(quantity, tense):
        quantity = 1
        tense = "past"
        make_sentence = (f"{get_determiner} {get_noun} {get_verb}.")
        return make_sentence
    print(f"{make_sentence} {1}")

print(f"Hello {name}, here are your random sentences generated below: ")


















main()