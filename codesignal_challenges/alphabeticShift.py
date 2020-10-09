"""
Given a string, your task is to replace each of its characters by the next one in the English alphabet;
i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz".
"""


def alphabeticShift(inputString):
    # input: a string of alphabetical characters
    # parse string in a dynamic list
    parsedstring = [char for char in inputString]
    # iterate through parsed string and use ord to grab the dec value (http://www.asciitable.com/)
    parsed_stringplusone = []
    for i in range(len(parsedstring)):
    # if the dec value is a-z (97-121)
        if ord(parsedstring[i]) >= 97 and ord(parsedstring[i]) <= 121:
        # parsed_stringplusone.append(ord(parsedstring[i]))  # Dec value of inputString
        # create a statement that thats the indexed character and adds one if letters are from a-y
        # chr() has an inverse relationship to ord()
            parsed_stringplusone.append(chr(ord(parsedstring[i])+1))  # Dec value of inputString PLUS 1
        
        # if the letter is z or (dec 122)
        elif ord(parsedstring[i]) == 122:
            parsed_stringplusone.append(chr(ord('a')))  # Dec value of inputString PLUS 1

    # output: return updated character to a list & use "".join(parsed string) to merge characters 
    # into a string mimiking the input with every letter being one alphabet more than inputString
    return "".join(parsed_stringplusone)


if __name__ == '__main__':
    inputString = "crazy"
    # inputString = "codesignal"
    print(alphabeticShift(inputString))
    """
    The output should take the inputString and return each character one
    alphabet higher than the previous. For example, if "a" the output would be be. 
    If "Amy", the output returned would be "Bnz".
    """