"""
You are given a parentheses sequence, check if it's regular.

Example

For s = "()()(())", the output should be
validParenthesesSequence(s) = true;
For s = "()()())", the output should be
validParenthesesSequence(s) = false.

true if the sequence is as it is supposed to be () or (()) otherwise return false.
"""


def validParenthesesSequence(s):
    # input: string containing parenthesis characters
    # parsed_s = [char for char in s]  # Space Complexity Reduction to remove as the loop can iterate through the string. 
    # Iterate through the parsed string
    counter = 0
    is_closed = True  # True, default is closed
    # for every instance of '(' (DEC 40) there SHOULD BE a ')' (DEC 41) or another '('
    # Iterate parsed_s
    for char in range(len(s)):
        if is_closed == True and s[char] == ")":
            return False
    #  If "("  or "(" is next to "(", add one to counter
        if s[char] == "(":
            counter += 1
            is_closed = False  # Is not closed
    # If ")" OR if ")" and followed by ")", remove one from the counter.
        if s[char] == ")":
            counter -= 1
            if counter == 0:
                is_closed =  True # Is closed

    # If the closing bracket is followed by an opening bracket and the counter is not zero return False. 
        # if parsed_s[char] == ")" and parsed_s[char+1] == "(" and counter != 0:
        #     return False
    
    # If by the end of the sequence the counter is not 0, return False. (Doesn't matter if False is already returned)

    # output: boolean, TRUE if the sequence is as it is supposed to be () or (()) otherwise return FALSE.
    return is_closed



if __name__ == '__main__':
    # s = "()()()()()"
    s = "()"
    # s = "())"
    # s = "()()())"
    # s = ")("
    print(validParenthesesSequence(s))
    """
    The validParenthesisSequence function take a string of random open/closed
    parenthesis and traverses through the sequence. The string passed several 
    conditional statementst and a counter to determine if pythonic rules for
    having a parenthesis applies. If the output is True, then sttring contains
    a proper sequence ( ) ; inversely, if False, it does not ) (. 

    Important to note that when I initially approached this problem, I was
    attempting to use ord converstion. This problem CAN be solved in the fashion,
    but it is an extra step with additional considerations to factor. Keep the 
    problem simple. 
    """