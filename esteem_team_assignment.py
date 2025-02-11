# I feel that I am a person of worth, at least on an equal plane with others.
# I feel that I have a number of good qualities.
# All in all, I am inclined to feel that I am a failure.
# I am able to do things as well as most other people.
# I feel I do not have much to be proud of.
# I take a positive attitude toward myself.
# On the whole, I am satisfied with myself.
# I wish I could have more respect for myself.
# I certainly feel useless at times.
# At times I think I am no good at all.
def main():
    print("This program is an implementation of the Rosenberg Self-Esteem Scale.")
    print("This program will show you ten statements that you could possibly apply to yourself.")
    print("Rate how much you agree with each of the statements by responding with one of these four letters:")
    print(" ")
    print("D means you strongly disagree with the statement.")
    print ("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means that you strongly agree with the statement.")
    print(" ")

    one = input(f"I feel that I am a person of worth, at least on an equal plane with others. ")
    two = input(f"I feel that I have a number of good qualities. ")
    three = input(f"All in all, I am inclined to feel that I am a failure. ")
    four = input(f"I am able to do things as well as most other people. ")
    five = input(f"I feel I do not have much to be proud of. ")
    six = input(f"I take a positive attitude toward myself. ")
    seven = input(f"On the whole, I am satisfied with myself. ")
    eight = input(f"I wish I could have more respect for myself. ")
    nine = input(f"I certainly feel useless at times. ")
    ten = input(f"At times I think I am no good at all. ")
    
    score = (positive_statements(one,two,four,six,seven) + negative_statements(three,five,eight,nine,ten))

    print(f"Your score is {score}")
    print(f"A score below 15 may indicate problematic low self-esteem.")



def positive_statements(pos1,pos2,pos3,pos4,pos5):
    # Notice that five of the statements (numbers 1, 2, 4, 6, 7) are positive and are scored like this:
    # convert letter D d a A to a number value
    # Strongly Disagree	0
    # Disagree	1
    # Agree	2
    # Strongly Agree 3
    
    
    positive_value = 0
    #pos1
    if (pos1 == 'D'):
        positive_value += 0
    if (pos1 == 'd'):
        positive_value += 1
    if (pos1 == 'a'):
        positive_value += 2
    if (pos1 == 'A'):
        positive_value += 3
    #pos2
    if (pos2 == 'D'):
        positive_value += 0
    if (pos2 == 'd'):
        positive_value += 1
    if (pos2 == 'a'):
        positive_value += 2
    if (pos2 == 'A'):
        positive_value += 3
    #pos3
    if (pos3 == 'D'):
        positive_value += 0
    if (pos3 == 'd'):
        positive_value += 1
    if (pos3 == 'a'):
        positive_value += 2
    if (pos3 == 'A'):
        positive_value += 3
    #pos4
    if (pos4 == 'D'):
        positive_value += 0
    if (pos4 == 'd'):
        positive_value += 1
    if (pos4 == 'a'):
        positive_value += 2
    if (pos4 == 'A'):
        positive_value += 3
    #pos5
    if (pos5 == 'D'):
        positive_value += 0
    if (pos5 == 'd'):
        positive_value += 1
    if (pos5 == 'a'):
        positive_value += 2
    if (pos5 == 'A'):
        positive_value += 3
    
    return positive_value



def negative_statements(neg1,neg2,neg3,neg4,neg5):
    # The other five statements (numbers 3, 5, 8, 9, 10) are negative and are scored like this:
    # convert letter D d a A to a number value
    # Strongly Disagree	3
    # Disagree	2
    # Agree	1
    # Strongly Agree	0
    negative_value = 0
    # neg 1
    if neg1 == "D":
        negative_value += 3
    if neg1 == "d":
        negative_value += 2
    if neg1 == "a":
        negative_value += 1
    if neg1 == "A":
        negative_value += 0

    # neg 2
    if neg2 == "D":
        negative_value += 3
    if neg2 == "d":
        negative_value += 2
    if neg2 == "a":
        negative_value += 1
    if neg2 == "A":
        negative_value += 0
    
    # neg 3
    if neg3 == "D":
        negative_value += 3
    if neg3 == "d":
        negative_value += 2
    if neg3 == "a":
        negative_value += 1
    if neg3 == "A":
        negative_value += 0

    # neg 4
    if neg4 == "D":
        negative_value += 3
    if neg4 == "d":
        negative_value += 2
    if neg4 == "a":
        negative_value += 1
    if neg4 == "A":
        negative_value += 0

    # neg 5
    if neg5 == "D":
        negative_value += 3
    if neg5 == "d":
        negative_value += 2
    if neg5 == "a":
        negative_value += 1
    if neg5 == "A":
        negative_value += 0
        
    return (negative_value)

main()